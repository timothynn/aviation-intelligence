namespace AviationIntelligence.InspectionDomain;

public sealed record Inspection(
    string Id,
    string Scheme,
    string Jurisdiction,
    string AuthorityId,
    string TargetOrganizationId,
    string? AircraftId,
    DateTimeOffset StartedAt,
    DateTimeOffset? CompletedAt,
    IReadOnlyList<InspectionItem> Items,
    IReadOnlyList<InspectionFinding> Findings);

public sealed record InspectionItem(
    string Id,
    string Code,
    string Title,
    string Status,
    string? EvidenceReference,
    string? Observation);

public sealed record InspectionFinding(
    string Id,
    string ItemCode,
    string Title,
    string Description,
    string? StandardReference,
    string Severity,
    string Status,
    IReadOnlyList<string> EvidenceIds,
    IReadOnlyList<string> CorrectiveActionIds);

public sealed record CorrectiveAction(
    string Id,
    string FindingId,
    string ActionType,
    string Status,
    DateTimeOffset? DueAt,
    DateTimeOffset? VerifiedAt,
    string? VerificationEvidenceId);

public interface IInspectionScheme
{
    string SchemeId { get; }
    IReadOnlyCollection<string> SupportedJurisdictions { get; }
    FindingAssessment AssessFinding(InspectionFinding finding);
}

public sealed record FindingAssessment(
    string Severity,
    IReadOnlyCollection<string> RequiredActions,
    IReadOnlyCollection<string> RequiredEvidence,
    string Rationale);
