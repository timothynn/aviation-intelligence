namespace AviationIntelligence.ComplianceDomain;

public enum ComplianceResult
{
    NotAssessed,
    Compliant,
    PartiallyCompliant,
    NonCompliant,
    NotApplicable,
    RequiresReview
}

public sealed record ComplianceRequirement(
    string Id,
    string Title,
    string AuthorityId,
    string Jurisdiction,
    string? Version,
    DateTimeOffset EffectiveFrom,
    DateTimeOffset? EffectiveTo,
    string? ApplicabilityExpression,
    string SourceDocumentId,
    string Locator);

public sealed record ComplianceAssessment(
    string Id,
    string RequirementId,
    string SubjectId,
    ComplianceResult Result,
    IReadOnlyCollection<string> EvidenceIds,
    string? Rationale,
    string AssessedBy,
    DateTimeOffset AssessedAt);

public interface IComplianceEvaluator
{
    ComplianceAssessment Evaluate(
        ComplianceRequirement requirement,
        string subjectId,
        IReadOnlyCollection<string> evidenceIds,
        string assessor,
        DateTimeOffset at);
}

public sealed class EvidencePresenceComplianceEvaluator : IComplianceEvaluator
{
    public ComplianceAssessment Evaluate(
        ComplianceRequirement requirement,
        string subjectId,
        IReadOnlyCollection<string> evidenceIds,
        string assessor,
        DateTimeOffset at)
    {
        var result = evidenceIds.Count > 0
            ? ComplianceResult.RequiresReview
            : ComplianceResult.NotAssessed;

        return new(
            Guid.NewGuid().ToString("N"),
            requirement.Id,
            subjectId,
            result,
            evidenceIds,
            "Reference evaluator: evidence presence alone is insufficient for a final regulatory determination.",
            assessor,
            at);
    }
}
