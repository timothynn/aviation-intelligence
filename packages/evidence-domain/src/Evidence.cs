namespace AviationIntelligence.EvidenceDomain;

public enum EvidenceType
{
    Document,
    Photograph,
    Scan,
    Signature,
    Observation,
    Statement,
    TechnicalRecord,
    ExternalReference
}

public sealed record EvidenceItem(
    string Id,
    EvidenceType Type,
    string Title,
    string Uri,
    string ContentHash,
    string? MimeType,
    string? SourceDocumentId,
    string? Locator,
    DateTimeOffset CapturedAt,
    string CapturedBy,
    IReadOnlyCollection<string> Tags,
    bool IsSensitive = false);

public sealed record EvidenceLink(
    string EvidenceId,
    string TargetEntityId,
    string Relationship,
    string? Notes = null);

public interface IEvidenceRepository
{
    Task<EvidenceItem?> GetAsync(string evidenceId, CancellationToken cancellationToken = default);
    Task SaveAsync(EvidenceItem item, CancellationToken cancellationToken = default);
    Task LinkAsync(EvidenceLink link, CancellationToken cancellationToken = default);
}

public static class EvidencePolicy
{
    public static bool CanExpose(EvidenceItem item, bool hasSensitivePermission) =>
        !item.IsSensitive || hasSensitivePermission;
}
