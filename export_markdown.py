"""
export_markdown.py
------------------
This file exports the storyboard as a clean Markdown (.md) file.
Think of it as a "quick summary" document — easy to read, easy to share.

It takes the same storyboard data used for Excel and PowerPoint,
and writes it into a simple, readable .md file.
"""

from e2e_test import build_storyboard


def export_markdown(storyboard: list, filename: str, topic: str = "Course Storyboard"):
    """
    Export the storyboard to a Markdown file.

    Parameters:
    - storyboard: List of screen dictionaries from build_storyboard()
    - filename:   Name of the .md file to save (e.g. "storyboard_ai.md")
    - topic:      The course topic name (e.g. "Artificial Intelligence")
    """

    # Start building the markdown content
    lines = []

    # Add the title and intro
    lines.append(f"# eLearning Storyboard — {topic}\n")
    lines.append(f"> Auto-generated storyboard with {len(storyboard)} screens.\n")
    lines.append("---\n")

    # Loop through each screen and add it to the markdown
    for i, screen in enumerate(storyboard, 1):
        stype  = screen["type"]
        title  = screen["title"]

        # Add screen heading
        lines.append(f"## Screen {i}: {title.title()}\n")
        lines.append(f"**Type:** {stype.upper()}\n")

        # Format content based on screen type
        if stype == "cyu":
            # Quiz screen — show question and options
            lines.append(f"**Question:** {screen.get('question', '')}\n")
            options = screen.get("options", {})
            correct = screen.get("correct_answer", "")
            for key, val in options.items():
                # Mark the correct answer with a tick
                tick = " ✓" if key == correct else ""
                lines.append(f"- {key}) {val}{tick}")
            lines.append(f"\n**Correct Answer:** {correct}\n")
        else:
            # All other screens — show content
            content = screen.get("content", "").strip()
            lines.append(f"{content}\n")

        # Add a divider between screens
        lines.append("---\n")

    # Join all lines into one big string
    markdown_content = "\n".join(lines)

    # Write to the .md file
    with open(filename, "w") as f:
        f.write(markdown_content)

    print(f"✅ Markdown saved: {filename}")
    return filename


# ── Run as standalone script ──────────────────────────────────────────────────
if __name__ == "__main__":
    # Process all 3 sample PDFs
    jobs = [
        ("sample.pdf",  "Artificial Intelligence",        "storyboard_ai.md"),
        ("sample2.pdf", "Cybersecurity and Data Privacy",  "storyboard_cybersecurity.md"),
        ("sample3.pdf", "Business and Digital Marketing",  "storyboard_marketing.md"),
    ]

    for pdf, topic, out in jobs:
        print(f"\n📄 Processing: {topic}")
        storyboard = build_storyboard(pdf)
        export_markdown(storyboard, out, topic)

    print("\n🎉 All 3 Markdown files created!")
