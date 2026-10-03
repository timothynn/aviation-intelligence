using AviationIntelligence.EvidenceDomain;

namespace AviationIntelligence.PlatformServices;

public sealed record GroundedRetrievalResult(
    string Query,
    IReadOnlyList<SearchDocument> Sources,
    bool Abstain,
    string? AbstainReason);

public interface IAccessEvaluator
{
    bool CanExpose(SearchDocument document, string principalId);
}

public sealed class GroundedRetrievalService
{
    private readonly IHybridSearchProvider _search;
    private readonly IAccessEvaluator _access;

    public GroundedRetrievalService(IHybridSearchProvider search, IAccessEvaluator access)
    {
        _search = search;
        _access = access;
    }

    public async Task<GroundedRetrievalResult> RetrieveAsync(
        SearchQuery query,
        string principalId,
        double minimumScore = 0.35,
        CancellationToken cancellationToken = default)
    {
        var hits = await _search.SearchAsync(query, cancellationToken);
        var evidence = hits
            .Where(hit => hit.Score >= minimumScore)
            .Where(hit => _access.CanExpose(hit, principalId))
            .ToArray();

        if (evidence.Length == 0)
        {
            return new GroundedRetrievalResult(
                query.Text,
                Array.Empty<SearchDocument>(),
                true,
                "No sufficiently strong, authorised evidence was retrieved.");
        }

        return new GroundedRetrievalResult(query.Text, evidence, false, null);
    }
}