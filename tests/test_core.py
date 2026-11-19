"""Tests for Hierarchical Summarizer."""
import unittest
from context_window_hierarchical_summarizer.core import HierarchicalSummarizer

class TestHierarchicalSummarizer(unittest.TestCase):
    def test_pyramid_construction(self):
        s = HierarchicalSummarizer(branch_factor=2)
        s.add_turn("Turn 1")
        s.add_turn("Turn 2")
        s.add_turn("Turn 3")
        s.add_turn("Turn 4")

        self.assertIsNotNone(s.root)
        self.assertEqual(s.root.level, 2)
        ctx = s.render_context()
        self.assertIn("Recent Details", ctx)
