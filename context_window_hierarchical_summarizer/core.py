"""Core Hierarchical Context Summarizer."""
from typing import List, Dict, Optional, Any

class ContextNode:
    def __init__(self, level: int, content: str, children: Optional[List["ContextNode"]] = None):
        self.level = level
        self.content = content
        self.children = children or []

class HierarchicalSummarizer:
    def __init__(self, branch_factor: int = 3):
        self.branch_factor = branch_factor
        self.leaves: List[ContextNode] = []
        self.root: Optional[ContextNode] = None

    def add_turn(self, turn_content: str):
        self.leaves.append(ContextNode(level=0, content=turn_content))
        self._rebuild_pyramid()

    def _rebuild_pyramid(self):
        curr_level = self.leaves
        level_idx = 1
        while len(curr_level) > 1:
            next_level = []
            for i in range(0, len(curr_level), self.branch_factor):
                group = curr_level[i:i + self.branch_factor]
                summary = f"Summary(L{level_idx}): " + "; ".join(g.content[:30] for g in group)
                parent = ContextNode(level=level_idx, content=summary, children=group)
                next_level.append(parent)
            curr_level = next_level
            level_idx += 1
        self.root = curr_level[0] if curr_level else None

    def render_context(self, max_tokens_approx: int = 500) -> str:
        if not self.root:
            return ""
        # Return root executive summary + last 2 verbatim leaves
        recent = [l.content for l in self.leaves[-2:]]
        return self.root.content + chr(10) + "Recent Details:" + chr(10) + chr(10).join(recent)
