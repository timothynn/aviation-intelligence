from __future__ import annotations

from dataclasses import dataclass

from .models import EvidencePack


SYSTEM_PROMPT = """You are an aviation regulatory document assistant.
Use only the supplied evidence pack. Do not invent requirements, dates, applicability,
standards, or technical limits. Distinguish current from historical sources. When evidence
is insufficient or conflicting, say so and abstain. Every material claim must cite an evidence
item using [E1], [E2], etc. You are a decision-support tool, not the regulatory authority.
"""


@dataclass(frozen=True)
class GroundingPrompt:
    system: str
    user: str


def build_prompt(query: str, pack: EvidencePack) -> GroundingPrompt:
    evidence_blocks = []
    for idx, evidence in enumerate(pack.evidences, 1):
        evidence_blocks.append(
            f"[E{idx}] {evidence.title} | authority={evidence.authority} | jurisdiction={evidence.jurisdiction} "
            f"| status={evidence.status} | version={evidence.version} | section={evidence.section} "
            f"| paragraph={evidence.paragraph} | pages={evidence.page_start}-{evidence.page_end} "
            f"| source={evidence.source_url}\n{evidence.text}"
        )
    evidence_text = "\n\n".join(evidence_blocks) or "NO EVIDENCE"
    user = f"Question: {query}\n\nEvidence:\n{evidence_text}\n\nAnswer using only this evidence."
    return GroundingPrompt(system=SYSTEM_PROMPT, user=user)
