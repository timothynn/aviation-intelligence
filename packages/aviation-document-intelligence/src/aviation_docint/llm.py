from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .models import EvidencePack


@dataclass(frozen=True, slots=True)
class GroundedPrompt:
    system: str
    user: str
    citations_required: bool = True


class LLMProvider(Protocol):
    def generate(self, prompt: GroundedPrompt) -> str: ...


SYSTEM_PROMPT = """You are an aviation regulatory knowledge assistant. Answer only from the supplied evidence pack. Do not invent regulatory requirements, dates, applicability, technical limits, or source citations. Distinguish current from historical material. If the evidence is insufficient or conflicting, say so and do not guess. Final regulatory, airworthiness, enforcement, operational-restriction, and finding decisions remain with the authorized human and rule engine."""


def build_grounded_prompt(question: str, pack: EvidencePack) -> GroundedPrompt:
    if pack.abstain:
        body = f"Question: {question}\n\nNo sufficient evidence was retrieved. Explain that the system cannot answer reliably."
    else:
        evidence = []
        for idx, item in enumerate(pack.evidences, 1):
            locator = " / ".join(x for x in [item.section, item.paragraph] if x)
            pages = f"pp. {item.page_start}-{item.page_end}" if item.page_start else ""
            evidence.append(
                f"[{idx}] {item.title} | {item.authority} | {item.jurisdiction} | {item.status} | {item.version}\n"
                f"Location: {locator} {pages}\nSource: {item.source_url}\n{item.text}"
            )
        body = f"Question: {question}\n\nEvidence:\n\n" + "\n\n---\n\n".join(evidence)
    return GroundedPrompt(SYSTEM_PROMPT, body)


class NullLLM:
    """Safe default provider for development and retrieval-only deployments."""

    def generate(self, prompt: GroundedPrompt) -> str:
        if "No sufficient evidence" in prompt.user:
            return "Insufficient authoritative evidence was retrieved to answer this question reliably."
        return "LLM provider not configured. Use the evidence pack directly or configure an approved provider."
