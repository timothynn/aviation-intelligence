namespace AviationIntelligence.PlatformServices;

public enum DocumentProcessingStage
{
    Discovered,
    Downloaded,
    Normalized,
    Parsed,
    Chunked,
    Indexed,
    GraphUpdated,
    Complete,
    Failed
}

public sealed record DocumentProcessingJob(
    string JobId,
    string SourceId,
    string Uri,
    DocumentProcessingStage Stage = DocumentProcessingStage.Discovered,
    int Attempt = 0,
    string? Error = null);

public interface IDocumentProcessingQueue
{
    Task EnqueueAsync(DocumentProcessingJob job, CancellationToken cancellationToken = default);
    Task<DocumentProcessingJob?> DequeueAsync(CancellationToken cancellationToken = default);
}

public interface IDocumentProcessingStep
{
    DocumentProcessingStage Stage { get; }
    Task<DocumentProcessingJob> ExecuteAsync(DocumentProcessingJob job, CancellationToken cancellationToken = default);
}

public sealed class DocumentProcessingOrchestrator
{
    private readonly IReadOnlyList<IDocumentProcessingStep> _steps;

    public DocumentProcessingOrchestrator(IEnumerable<IDocumentProcessingStep> steps)
    {
        _steps = steps.OrderBy(step => step.Stage).ToArray();
    }

    public async Task<DocumentProcessingJob> ProcessAsync(
        DocumentProcessingJob job,
        CancellationToken cancellationToken = default)
    {
        var current = job;
        foreach (var step in _steps)
        {
            cancellationToken.ThrowIfCancellationRequested();
            if (step.Stage <= current.Stage || current.Stage == DocumentProcessingStage.Failed)
                continue;

            try
            {
                current = await step.ExecuteAsync(current, cancellationToken);
            }
            catch (Exception ex)
            {
                return current with
                {
                    Stage = DocumentProcessingStage.Failed,
                    Attempt = current.Attempt + 1,
                    Error = ex.Message
                };
            }
        }

        return current with { Stage = DocumentProcessingStage.Complete, Error = null };
    }
}