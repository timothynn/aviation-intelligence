using AviationIntelligence.RegulatoryDomain;
using AviationIntelligence.PlatformServices;

namespace AviationIntelligence.PlatformServices.Tests;

public sealed class PlatformServicesTests
{
    [Fact]
    public void RegulatoryResolution_UsesCurrentApplicableRules()
    {
        var repository = new InMemoryRuleRepository(
        [
            new RegulatoryRule(
                "icao-1",
                "Global requirement",
                RuleSourceKind.Standard,
                "ICAO",
                "GLOBAL",
                "2026",
                new DateTimeOffset(2026, 1, 1, 0, 0, 0, TimeSpan.Zero),
                null,
                [],
                [],
                "doc-1",
                "Annex 6",
                80),
            new RegulatoryRule(
                "local-1",
                "Local requirement",
                RuleSourceKind.Regulation,
                "KCAA",
                "KE",
                "2026",
                new DateTimeOffset(2026, 2, 1, 0, 0, 0, TimeSpan.Zero),
                null,
                ["CAT"],
                [],
                "doc-2",
                "CAR",
                100)
        ]);

        var service = new RegulatoryResolutionService(repository);
        var result = service.Resolve(new RegulatoryContext(
            new DateTimeOffset(2026, 8, 1, 0, 0, 0, TimeSpan.Zero),
            "KE",
            "KCAA",
            OperationType: "CAT"));

        Assert.Contains(result.Rules, r => r.Rule.Id == "local-1" && r.Applicable);
        Assert.False(result.RequiresHumanReview);
    }

    [Fact]
    public async Task GroundedRetrieval_AbstainsWhenNoAuthorisedEvidence()
    {
        var service = new GroundedRetrievalService(
            new FakeSearchProvider([]),
            new AlwaysDenyAccess());

        var result = await service.RetrieveAsync(new SearchQuery("SAFA A17"), "inspector-1");

        Assert.True(result.Abstain);
        Assert.Empty(result.Sources);
    }

    [Fact]
    public async Task Pipeline_StopsOnFailure()
    {
        var pipeline = new DocumentProcessingOrchestrator(
        [
            new Step(DocumentProcessingStage.Downloaded),
            new FailingStep(DocumentProcessingStage.Normalized)
        ]);

        var result = await pipeline.ProcessAsync(new DocumentProcessingJob("j1", "src", "https://example.test/doc"));

        Assert.Equal(DocumentProcessingStage.Failed, result.Stage);
        Assert.NotNull(result.Error);
    }

    private sealed class InMemoryRuleRepository(IReadOnlyCollection<RegulatoryRule> rules) : IRegulatoryRuleRepository
    {
        public IReadOnlyCollection<RegulatoryRule> GetAll() => rules;
    }

    private sealed class FakeSearchProvider(IReadOnlyList<SearchDocument> documents) : IHybridSearchProvider
    {
        public Task<IReadOnlyList<SearchDocument>> SearchAsync(SearchQuery query, CancellationToken cancellationToken = default) =>
            Task.FromResult(documents);
    }

    private sealed class AlwaysDenyAccess : IAccessEvaluator
    {
        public bool CanExpose(SearchDocument document, string principalId) => false;
    }

    private sealed class Step(DocumentProcessingStage stage) : IDocumentProcessingStep
    {
        public DocumentProcessingStage Stage => stage;
        public Task<DocumentProcessingJob> ExecuteAsync(DocumentProcessingJob job, CancellationToken cancellationToken = default) =>
            Task.FromResult(job with { Stage = Stage });
    }

    private sealed class FailingStep(DocumentProcessingStage stage) : IDocumentProcessingStep
    {
        public DocumentProcessingStage Stage => stage;
        public Task<DocumentProcessingJob> ExecuteAsync(DocumentProcessingJob job, CancellationToken cancellationToken = default) =>
            throw new InvalidOperationException("simulated failure");
    }
}