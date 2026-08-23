namespace AviationIntelligence.InspectionDomain;

public sealed class InspectionSchemeRegistry
{
    private readonly Dictionary<string, IInspectionScheme> _schemes = new(StringComparer.OrdinalIgnoreCase);

    public void Register(IInspectionScheme scheme)
    {
        ArgumentNullException.ThrowIfNull(scheme);
        _schemes[scheme.SchemeId] = scheme;
    }

    public IInspectionScheme Get(string schemeId) =>
        _schemes.TryGetValue(schemeId, out var scheme)
            ? scheme
            : throw new KeyNotFoundException($"Inspection scheme '{schemeId}' is not registered.");
}
