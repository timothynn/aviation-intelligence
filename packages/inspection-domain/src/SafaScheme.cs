namespace AviationIntelligence.InspectionDomain;

public enum SafaFindingCategory
{
    Category1,
    Category2,
    Category3,
    GeneralRemark
}

public enum SafaActionClass
{
    Class1,
    Class2,
    Class3
}

public sealed record SafaFinding(
    string Id,
    string ItemCode,
    string Description,
    SafaFindingCategory Category,
    SafaActionClass ActionClass,
    bool RequiresActionBeforeFlight,
    IReadOnlyCollection<string> EvidenceIds,
    string? StandardReference,
    string? PreDescribedFindingCode = null);

public static class SafaRules
{
    public static SafaActionClass MinimumActionClass(SafaFindingCategory category) => category switch
    {
        SafaFindingCategory.Category1 => SafaActionClass.Class1,
        SafaFindingCategory.Category2 => SafaActionClass.Class2,
        SafaFindingCategory.Category3 => SafaActionClass.Class3,
        SafaFindingCategory.GeneralRemark => SafaActionClass.Class1,
        _ => throw new ArgumentOutOfRangeException(nameof(category), category, null)
    };

    public static bool RequiresBeforeFlightAction(SafaFindingCategory category) =>
        category == SafaFindingCategory.Category3;

    public static bool IsValidAction(SafaFindingCategory category, SafaActionClass actionClass) =>
        actionClass >= MinimumActionClass(category);
}

public sealed class SafaInspectionScheme : IInspectionScheme
{
    public string SchemeId => "SAFA";

    public IReadOnlyCollection<string> SupportedJurisdictions { get; } = ["GLOBAL", "EU/EEA", "KE"];

    public FindingAssessment AssessFinding(InspectionFinding finding)
    {
        if (!Enum.TryParse<SafaFindingCategory>(finding.Severity, true, out var category))
            return new("Unknown", ["Human review"], ["Applicable standard", "Evidence"],
                "Finding severity is not a recognised SAFA category.");

        var requiredActions = category switch
        {
            SafaFindingCategory.Category1 => new[] { "Captain briefing" },
            SafaFindingCategory.Category2 => new[] { "Captain briefing", "Authority/operator notification", "Corrective action plan" },
            SafaFindingCategory.Category3 => new[] { "Captain briefing", "Authority/operator notification", "Immediate safety action" },
            _ => new[] { "Record general remark" }
        };

        var requiredEvidence = new[] { "Observation evidence", "Applicable standard reference" };
        var rationale = category == SafaFindingCategory.Category3
            ? "Category 3 is treated as potentially safety-critical and requires human-authorised immediate action before flight where applicable."
            : "SAFA AI support recommends actions but does not make the final regulatory decision.";

        return new(category.ToString(), requiredActions, requiredEvidence, rationale);
    }
}
