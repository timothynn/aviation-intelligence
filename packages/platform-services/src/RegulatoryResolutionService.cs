using System.Collections.Immutable;
using AviationIntelligence.RegulatoryDomain;

namespace AviationIntelligence.PlatformServices;

public sealed record RegulatoryResolutionResult(
    IReadOnlyList<RuleResolution> Rules,
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

    public RegulatoryResolutionResult Resolve(RegulatoryContext context)
    {
        ArgumentNullException.ThrowIfNull(context);

        var resolved = RegulatoryRuleResolver.Resolve(_repository.GetAll(), context)
            .OrderByDescending(result => result.Score)
            .ThenByDescending(result => result.Rule.AuthorityPrecedence)
            .ThenByDescending(result => result.Rule.EffectiveFrom)
            .ToImmutableArray();

        var authorities = resolved
            .Select(result => result.Rule.AuthorityId)
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .Count();

        return new RegulatoryResolutionResult(
            resolved,
            authorities > 1,
            authorities > 1
                ? "Multiple applicable authorities were resolved; source precedence and competent-authority review are required."
                : null);
    }
}