namespace AviationIntelligence.WorkflowDomain;

public sealed record WorkflowCase(
    string Id,
    string WorkflowDefinitionId,
    string SubjectType,
    string SubjectId,
    string Status,
    string CurrentStage,
    DateTimeOffset CreatedAt,
    DateTimeOffset? ClosedAt);

public sealed record WorkflowStage(
    string Id,
    string Name,
    IReadOnlyCollection<string> AllowedTransitions,
    string? SlaPolicyId);

public sealed record WorkflowTask(
    string Id,
    string CaseId,
    string Type,
    string Status,
    string? AssignedTo,
    DateTimeOffset? DueAt);

public sealed record WorkflowDecision(
    string Id,
    string CaseId,
    string Transition,
    string DecidedBy,
    string DecisionType,
    string? Reason,
    DateTimeOffset DecidedAt);

public sealed record WorkflowAuditEvent(
    string Id,
    string CaseId,
    string EventType,
    string ActorId,
    DateTimeOffset OccurredAt,
    string? CorrelationId,
    string? MetadataJson);
