namespace AviationIntelligence.RegulatoryDomain;

public sealed record RegulatorySource(
    string Id,
    string AuthorityId,
    string Jurisdiction,
    string InstrumentType,
    string Reference,
    string Version,
    DateTimeOffset PublishedAt,
    DateTimeOffset EffectiveAt,
    DateTimeOffset? ExpiresAt,
    string? SupersedesSourceId,
    string ProvenanceUri);

public sealed record RegulatoryRequirement(
    string Id,
    string SourceId,
    string RequirementReference,
    string Text,
    string ApplicabilityExpression,
    string Status,
    DateTimeOffset EffectiveAt,
    DateTimeOffset? RetiredAt);

public sealed record ComplianceAssessment(
    string Id,
    string RequirementId,
    string SubjectType,
    string SubjectId,
    string Result,
    double Confidence,
    IReadOnlyCollection<string> EvidenceIds,
    string AssessedBy,
    DateTimeOffset AssessedAt);
