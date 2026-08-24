namespace AviationIntelligence.PlatformServices;

public sealed record RegulatoryChange(
    string SourceId,
    string? OldVersion,
    string? NewVersion,
    string ChangeType,
    IReadOnlyCollection<string> AffectedDocumentIds,
    DateTimeOffset DetectedAt);

public sealed record ChangeImpact(
    string ArtifactId,
    string ArtifactType,
    string Impact,
    string Reason,
    bool RequiresReview);

public interface IKnowledgeDependencyRepository
{
    IReadOnlyCollection<(string ArtifactId, string ArtifactType, string SourceId)> FindDependents(string sourceId);
}

public sealed class ChangeImpactService
{
    private readonly IKnowledgeDependencyRepository _dependencies;

    public ChangeImpactService(IKnowledgeDependencyRepository dependencies)
    {
        _dependencies = dependencies;
    }

    public IReadOnlyList<ChangeImpact> Assess(RegulatoryChange change)
    {
        var dependents = _dependencies.FindDependents(change.SourceId);
        return dependents
            .Select(item => new ChangeImpact(
                item.ArtifactId,
                item.ArtifactType,
                change.ChangeType,
                $"Source {change.SourceId} changed from {change.OldVersion ?? "unknown"} to {change.NewVersion ?? "unknown"}.",
                true))
            .ToArray();
    }
}