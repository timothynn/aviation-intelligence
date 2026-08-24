using System.Collections.Immutable;
using AviationIntelligence.RegulatoryDomain;

namespace AviationIntelligence.PlatformServices;

public sealed record RegulatoryResolutionContext(
    string Jurisdiction,
    DateTimeOffset At,
    string? AuthorityId = null,
    string? OperationType = null,
    string? AircraftType = null,
    string? OperatorId = null);

public sealed record RegulatoryResolutionResult(
    IReadOnlyList<RegulatoryRule> Rules,
    bool RequiresHumanReview,
    string? ReviewReason);

public interface IRegulatoryRuleRepository
{
    IReadOnlyCollection<RegulatoryRule> GetAll();
}

public sealed class RegulatoryResolutionService
{
    private readonly IRegulatoryRuleRepository _repository;

    public RegulatoryResolutionService(IRegulatoryRuleRepository repository)
    {
        _repository = repository;
    }

    public RegulatoryResolutionResult Resolve(RegulatoryResolutionContext context)
    {
        ArgumentNullException.ThrowIfNull(context);

        var candidates = _repository.GetAll()
            .Where(rule => MatchesJurisdiction(rule, context.Jurisdiction))
            .Where(rule => IsEffective(rule, context.At))
            .Where(rule => MatchesAuthority(rule, context.AuthorityId))
            .Where(rule => MatchesScope(rule, context))
            .OrderByDescending(rule => AuthorityPriority(rule.Source.AuthorityId, context.AuthorityId))
            .ThenByDescending(rule => rule.EffectiveFrom)
            .ToList();

        var conflictingAuthorities = candidates
            .Select(r => r.Source.AuthorityId)
            .Where(id => !string.IsNullOrWhiteSpace(id))
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .Count() > 1;

        return new RegulatoryResolutionResult(
            candidates.ToImmutableArray(),
            conflictingAuthorities,
            conflictingAuthorities ? "Multiple authority sources are applicable; competent-authority precedence review is required." : null);
    }

    private static bool MatchesJurisdiction(RegulatoryRule rule, string jurisdiction) =>
        string.Equals(rule.Jurisdiction, jurisdiction, StringComparison.OrdinalIgnoreCase) ||
        string.Equals(rule.Jurisdiction, "GLOBAL", StringComparison.OrdinalIgnoreCase);

    private static bool IsEffective(RegulatoryRule rule, DateTimeOffset at) =>
        rule.EffectiveFrom <= at && (rule.EffectiveTo is null || rule.EffectiveTo >= at);

    private static bool MatchesAuthority(RegulatoryRule rule, string? authorityId) =>
        authorityId is null ||
        string.Equals(rule.Source.AuthorityId, authorityId, StringComparison.OrdinalIgnoreCase) ||
        string.Equals(rule.Source.AuthorityId, "ICAO", StringComparison.OrdinalIgnoreCase);

    private static bool MatchesScope(RegulatoryRule rule, RegulatoryResolutionContext context)
    {
        if (rule.Scope.Count == 0) return true;
        return rule.Scope.All(entry => entry.Value is null ||
            context.OperationType is null ||
            string.Equals(entry.Value, context.OperationType, StringComparison.OrdinalIgnoreCase) ||
            context.AircraftType is not null && string.Equals(entry.Value, context.AircraftType, StringComparison.OrdinalIgnoreCase));
    }

    private static int AuthorityPriority(string? source, string? requestedAuthority)
    {
        if (requestedAuthority is not null && string.Equals(source, requestedAuthority, StringComparison.OrdinalIgnoreCase)) return 100;
        if (string.Equals(source, "ICAO", StringComparison.OrdinalIgnoreCase)) return 80;
        return 60;
    }
}