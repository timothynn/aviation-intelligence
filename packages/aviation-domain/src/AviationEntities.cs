namespace AviationIntelligence.AviationDomain;

public sealed record Jurisdiction(
    string CountryCode,
    string? AuthorityId = null,
    string? Region = null);

public sealed record ValidityWindow(
    DateTimeOffset EffectiveFrom,
    DateTimeOffset? EffectiveTo = null)
{
    public bool Contains(DateTimeOffset instant) =>
        instant >= EffectiveFrom && (EffectiveTo is null || instant < EffectiveTo);
}

public sealed record Provenance(
    string SourceType,
    string SourceId,
    string? SourceVersion = null,
    DateTimeOffset? RetrievedAt = null,
    string? Locator = null);

public sealed record EntityRelationship(
    string Type,
    string TargetId,
    DateTimeOffset? ValidFrom = null,
    DateTimeOffset? ValidTo = null);

public abstract record AviationEntity(
    string Id,
    Jurisdiction Jurisdiction,
    Provenance Provenance,
    ValidityWindow? Validity = null);

public sealed record Organization(
    string Id,
    string Name,
    Jurisdiction Jurisdiction,
    Provenance Provenance,
    string? OrganizationType = null,
    ValidityWindow? Validity = null)
    : AviationEntity(Id, Jurisdiction, Provenance, Validity);

public sealed record Aircraft(
    string Id,
    string Registration,
    string TypeDesignator,
    Jurisdiction Jurisdiction,
    Provenance Provenance,
    string? Manufacturer = null,
    string? Model = null,
    string? SerialNumber = null,
    ValidityWindow? Validity = null)
    : AviationEntity(Id, Jurisdiction, Provenance, Validity);

public sealed record Certificate(
    string Id,
    string CertificateType,
    string HolderOrganizationId,
    string Status,
    Jurisdiction Jurisdiction,
    Provenance Provenance,
    DateTimeOffset? IssuedAt = null,
    DateTimeOffset? ExpiresAt = null,
    ValidityWindow? Validity = null)
    : AviationEntity(Id, Jurisdiction, Provenance, Validity);

public sealed record Approval(
    string Id,
    string ApprovalType,
    string HolderOrganizationId,
    string Status,
    Jurisdiction Jurisdiction,
    Provenance Provenance,
    IReadOnlyCollection<string> Limitations,
    ValidityWindow? Validity = null)
    : AviationEntity(Id, Jurisdiction, Provenance, Validity);

public static class AviationEntityValidation
{
    public static void EnsureTwoLetterCountryCode(Jurisdiction jurisdiction)
    {
        if (jurisdiction.CountryCode.Length != 2)
            throw new ArgumentException("CountryCode must be an ISO-style two-letter code.", nameof(jurisdiction));
    }
}
