namespace AviationIntelligence.PlatformServices;

public enum ServiceHealthStatus
{
    Healthy,
    Degraded,
    Unhealthy
}

public sealed record ServiceHealth(
    string Service,
    ServiceHealthStatus Status,
    IReadOnlyDictionary<string, string> Details);

public interface IServiceHealthCheck
{
    Task<ServiceHealth> CheckAsync(CancellationToken cancellationToken = default);
}