from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class AccessDecision(str, Enum):
    ALLOW = "allow"
    DENY = "deny"
    REDACT = "redact"


@dataclass(frozen=True, slots=True)
class Principal:
    subject: str
    roles: frozenset[str] = frozenset()
    authorities: frozenset[str] = frozenset()
    jurisdictions: frozenset[str] = frozenset()
    clearances: frozenset[str] = frozenset()


@dataclass(frozen=True, slots=True)
class DocumentPolicy:
    visibility: str = "public"
    required_roles: frozenset[str] = frozenset()
    required_clearance: str | None = None
    authority: str | None = None
    jurisdiction: str | None = None


def authorize(principal: Principal, policy: DocumentPolicy) -> AccessDecision:
    if policy.visibility == "public":
        return AccessDecision.ALLOW
    if policy.required_roles and not policy.required_roles.intersection(principal.roles):
        return AccessDecision.DENY
    if policy.required_clearance and policy.required_clearance not in principal.clearances:
        return AccessDecision.DENY
    if policy.authority and policy.authority not in principal.authorities:
        return AccessDecision.DENY
    if policy.jurisdiction and policy.jurisdiction not in principal.jurisdictions:
        return AccessDecision.DENY
    return AccessDecision.ALLOW
