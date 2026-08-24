namespace AviationIntelligence.WorkflowDomain;

public enum CaseStatus
{
    Draft,
    Open,
    InReview,
    Returned,
    Accepted,
    Rejected,
    Closed,
    Suspended
}

public sealed record CaseTransition(
    string From,
    string To,
    string Action,
    bool RequiresComment = false);

public sealed record RegulatoryCase(
    string Id,
    string CaseType,
    CaseStatus Status,
    string SubjectId,
    string? AssignedTo,
    IReadOnlyCollection<string> EvidenceIds,
    DateTimeOffset CreatedAt,
    DateTimeOffset UpdatedAt,
    string? LastComment = null);

public sealed record TransitionResult(
    bool Allowed,
    RegulatoryCase Case,
    string? Error = null);

public sealed class CaseEngine
{
    private static readonly IReadOnlyCollection<CaseTransition> Transitions =
    [
        new(CaseStatus.Draft.ToString(), CaseStatus.Open.ToString(), "submit"),
        new(CaseStatus.Open.ToString(), CaseStatus.InReview.ToString(), "start-review"),
        new(CaseStatus.InReview.ToString(), CaseStatus.Returned.ToString(), "return", true),
        new(CaseStatus.Returned.ToString(), CaseStatus.InReview.ToString(), "resubmit"),
        new(CaseStatus.InReview.ToString(), CaseStatus.Accepted.ToString(), "accept"),
        new(CaseStatus.InReview.ToString(), CaseStatus.Rejected.ToString(), "reject", true),
        new(CaseStatus.Accepted.ToString(), CaseStatus.Closed.ToString(), "close"),
        new(CaseStatus.Open.ToString(), CaseStatus.Suspended.ToString(), "suspend", true),
        new(CaseStatus.Suspended.ToString(), CaseStatus.Open.ToString(), "resume")
    ];

    public TransitionResult Transition(RegulatoryCase current, string action, string? comment = null)
    {
        var transition = Transitions.FirstOrDefault(item =>
            string.Equals(item.From, current.Status.ToString(), StringComparison.OrdinalIgnoreCase) &&
            string.Equals(item.Action, action, StringComparison.OrdinalIgnoreCase));

        if (transition is null)
            return new(false, current, $"Action '{action}' is not allowed from status '{current.Status}'.");

        if (transition.RequiresComment && string.IsNullOrWhiteSpace(comment))
            return new(false, current, "A comment is required for this transition.");

        if (!Enum.TryParse<CaseStatus>(transition.To, out var targetStatus))
            return new(false, current, $"Invalid target status '{transition.To}'.");

        var updated = current with
        {
            Status = targetStatus,
            UpdatedAt = DateTimeOffset.UtcNow,
            LastComment = comment ?? current.LastComment
        };

        return new(true, updated);
    }

    public IReadOnlyCollection<CaseTransition> GetAvailableTransitions(CaseStatus status) =>
        Transitions.Where(item => string.Equals(item.From, status.ToString(), StringComparison.OrdinalIgnoreCase)).ToArray();
}
