namespace AviationIntelligence.PlatformServices;

public sealed record SearchQuery(
    string Text,
    int Limit = 10,
    string? Authority = null,
    string? Jurisdiction = null,
    string? Status = null,
    DateTimeOffset? EffectiveAt = null,
    IReadOnlyDictionary<string, string>? Filters = null);

public sealed record SearchDocument(
    string Id,
    string Title,
    string Text,
    string? Authority,
    string? Jurisdiction,
    string? Version,
    string? Locator,
    string? SourceUrl,
    double Score);

public interface ILexicalSearchProvider
{
    Task<IReadOnlyList<SearchDocument>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default);
}

public interface IVectorSearchProvider
{
    Task<IReadOnlyList<SearchDocument>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default);
}

public interface IHybridSearchProvider
{
    Task<IReadOnlyList<SearchDocument>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default);
}

public sealed record SearchProviderCapabilities(
    bool SupportsLexical,
    bool SupportsVector,
    bool SupportsHybrid,
    bool SupportsMetadataFiltering,
    bool SupportsSemanticReranking);
