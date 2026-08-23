using AviationIntelligence.InspectionDomain;

namespace AviationIntelligence.InspectionDomain.Tests;

public class InspectionDomainTests
{
    [Fact]
    public void Finding_retains_standard_reference_and_evidence()
    {
        var finding = new InspectionFinding(
            "F-1",
            "A23",
            "Example finding",
            "Example description",
            "ICAO Annex 6 / applicable source",
            "Unclassified",
            "Open",
            new[] { "E-1" },
            new[] { "CA-1" });

        Assert.Equal("A23", finding.ItemCode);
        Assert.Equal("ICAO Annex 6 / applicable source", finding.StandardReference);
        Assert.Single(finding.EvidenceIds);
        Assert.Single(finding.CorrectiveActionIds);
    }

    [Fact]
    public void Scheme_registry_rejects_unknown_scheme()
    {
        var registry = new InspectionSchemeRegistry();
        Assert.Throws<KeyNotFoundException>(() => registry.Get("unknown"));
    }
}
