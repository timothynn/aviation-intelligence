namespace AviationIntelligence.RegulatoryDomain;

public enum RuleSourceKind
{
    Regulation,
    Standard,
    RecommendedPractice,
    Procedure,
    Amc,
    Guidance,
    Decision,
    Advisory,
    HistoricalReference
}

public sealed record RegulatoryRule(
    string Id,
    string Title,
    RuleSourceKind SourceKind,
    string AuthorityId,
    string Jurisdiction,
    string? Version,
    DateTimeOffset EffectiveFrom,
    DateTimeOffset? EffectiveTo,
    IReadOnlyCollection<string> AppliesTo,
    IReadOnlyCollection<string> Supersedes,
    string? SourceDocumentId,
    string? Locator,
    int AuthorityPrecedence = 0);

public sealed record RegulatoryContext(
    DateTimeOffset At,
    string Jurisdiction,
    string? AuthorityId = null,
    string? OperatorId = null,
    string? AircraftId = null,
    string? AircraftType = null,
    string? OperationType = null,
    IReadOnlyCollection<string>? Certifications = null,
    IReadOnlyCollection<string>? Tags = null);

public sealed record RuleResolution(
    RegulatoryRule Rule,
    bool Applicable,
    double Score,
    string[] Reasons,
    bool IsCurrent);

public static class RegulatoryRuleResolver
{
    public static IReadOnlyList<RuleResolution> Resolve(
        IEnumerable<RegulatoryRule> rules,
        RegulatoryContext context)
    {
        return rules
            .Where(rule => rule.EffectiveFrom <= context.At)
            .Where(rule => rule.EffectiveTo is null || context.At < rule.EffectiveTo)
            .Select(rule => Score(rule, context))
            .Where(result => result.Applicable)
            .OrderByDescending(result => result.Score)
            .ThenByDescending(result => result.Rule.AuthorityPrecedence)
            .ThenByDescending(result => result.Rule.EffectiveFrom)
            .ToArray();
    }

    private static RuleResolution Score(RegulatoryRule rule, RegulatoryContext context)
    {
        var score = 0d;
        var reasons = new List<string>();

        if (string.Equals(rule.Jurisdiction, context.Jurisdiction, StringComparison.OrdinalIgnoreCase))
        {
            score += 5;
            reasons.Add("jurisdiction-match");
        }
        else if (!string.IsNullOrWhiteSpace(rule.Jurisdiction) && rule.Jurisdiction != "GLOBAL")
        {
            return new(rule, false, 0, ["jurisdiction-mismatch"], false);
        }
        else
        {
            score += 2;
            reasons.Add("global-jurisdiction");
        }

        if (!string.IsNullOrWhiteSpace(context.AuthorityId) &&
            string.Equals(rule.AuthorityId, context.AuthorityId, StringComparison.OrdinalIgnoreCase))
        {
            score += 3;
            reasons.Add("authority-match");
        }

        if (rule.AppliesTo.Count == 0)
        {
            score += 1;
            reasons.Add("unrestricted-applicability");
        }
        else
        {
            var candidates = new[] { context.AircraftType, context.OperationType }
                .Where(value => !string.IsNullOrWhiteSpace(value))
                .Concat(context.Certifications ?? Array.Empty<string>())
                .Concat(context.Tags ?? Array.Empty<string>());

            var matches = candidates.Count(candidate => rule.AppliesTo.Contains(candidate!, StringComparer.OrdinalIgnoreCase));
            if (matches == 0)
                return new(rule, false, 0, ["scope-mismatch"], false);

            score += matches * 2;
            reasons.Add($"scope-match:{matches}");
        }

        score += rule.AuthorityPrecedence / 100d;
        return new(rule, true, score, reasons.ToArray(), true);
    }
}
