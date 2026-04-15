#!/usr/bin/env python3
"""Export the scoring rubric from agent_prompt.md to a standalone markdown file."""

import pathlib


def main():
    script_dir = pathlib.Path(__file__).resolve().parent
    src = (script_dir / "agent_prompt.md").read_text()

    start = src.index("## Scoring Rubric")
    end = src.index("## Output Format")
    rubric = src[start:end].rstrip()

    out = pathlib.Path("artifacts/strat-rubric.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        "# Strategy Assessment Rubric\n"
        "\n"
        "> Exported from the assess-strat plugin. This is a read-only reference copy.\n"
        "> Source of truth: `scripts/agent_prompt.md` in the assess-strat plugin.\n"
        "\n"
        + rubric
        + "\n"
    )
    print(f"Wrote {out.resolve()}")


if __name__ == "__main__":
    main()
