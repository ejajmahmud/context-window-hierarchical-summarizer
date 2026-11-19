"""CLI for Hierarchical Summarizer."""
import argparse
from .core import HierarchicalSummarizer

def main():
    parser = argparse.ArgumentParser(description="Context Window Hierarchical Summarizer CLI")
    parser.add_argument("--demo", action="store_true", help="Run summarizer demo")
    args = parser.parse_args()

    s = HierarchicalSummarizer(branch_factor=2)
    s.add_turn("User asked for database connection parameters")
    s.add_turn("Agent returned postgres://user:pass@localhost:5432/db")
    s.add_turn("User asked to run migrations on users table")
    s.add_turn("Agent completed migrations successfully")

    ctx = s.render_context()
    print("Multi-resolution Context:")
    print(ctx)

if __name__ == "__main__":
    main()
