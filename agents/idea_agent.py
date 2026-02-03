#!/usr/bin/env python3
"""
Idea Agent - Generates project ideas and ships them to GitHub.

Usage:
    python idea_agent.py [optional_theme]
    
If no theme provided, picks a random useful tool category.
"""

import subprocess
import random
import string
import sys
import os
from datetime import datetime

# Categories of useful micro-projects that could get stars
IDEA_SEEDS = [
    {
        "category": "CLI Tools",
        "ideas": [
            ("quickclip", "Lightning-fast clipboard manager for the terminal", "A minimal CLI clipboard history tool. Copy once, paste forever."),
            ("jsonpretty", "Pretty-print and validate JSON from the command line", "Pipe JSON in, get beautiful formatted output. Validates syntax too."),
            ("portfinder", "Find what's running on any port instantly", "Simple CLI to check which process is hogging a port. Kill it if you want."),
        ]
    },
    {
        "category": "Developer Utilities",
        "ideas": [
            ("gitquick", "Git shortcuts for the lazy developer", "Aliases and scripts that make git operations stupidly fast."),
            ("envcheck", "Validate your .env files before deployment", "Catches missing variables, type mismatches, and secrets in wrong places."),
            ("depaudit", "Audit your dependencies for issues", "Quick scan for outdated, vulnerable, or unused packages."),
        ]
    },
    {
        "category": "Productivity",
        "ideas": [
            ("todocli", "Dead-simple todo list in your terminal", "No apps, no sync, no BS. Just todos in a file, managed from CLI."),
            ("focusblock", "Block distracting sites while you work", "Add sites to blocklist, set a timer, get stuff done."),
            ("timelog", "Track where your time actually goes", "Lightweight time tracking that doesn't get in your way."),
        ]
    },
    {
        "category": "Data Tools",
        "ideas": [
            ("csvknife", "Slice and dice CSV files from the terminal", "Filter, sort, select columns - all without opening Excel."),
            ("logparse", "Extract insights from messy log files", "Regex-powered log analysis for when grep isn't enough."),
            ("datasampler", "Generate realistic sample data fast", "Names, emails, addresses, timestamps - whatever you need for testing."),
        ]
    }
]


def generate_unique_suffix():
    """Add a short random suffix to avoid repo name collisions."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))


def pick_idea(theme=None):
    """Pick a random project idea, optionally filtered by theme."""
    if theme:
        # Try to match theme to category
        for cat in IDEA_SEEDS:
            if theme.lower() in cat["category"].lower():
                name, tagline, desc = random.choice(cat["ideas"])
                return name, tagline, desc, cat["category"]
    
    # Random pick
    category = random.choice(IDEA_SEEDS)
    name, tagline, desc = random.choice(category["ideas"])
    return name, tagline, desc, category["category"]


def generate_readme(name, tagline, description, category):
    """Generate a README for the project."""
    return f"""# {name} 🚀

> {tagline}

## What is this?

{description}

## Installation

```bash
# Coming soon
pip install {name}
```

## Usage

```bash
# Coming soon
{name} --help
```

## Why?

Because sometimes you just need a tool that does one thing well.

## Category

{category}

## Status

🌱 **Just planted** — This repo was created by an AI agent as part of the [AgentsCreate](https://github.com/Yoakshat/AgentsCreate) experiment.

---

*Built by agents, judged by stars.* ⭐
"""


def create_repo(name, tagline, readme_content):
    """Create the GitHub repo and push the README."""
    # Create temp directory
    repo_dir = f"/tmp/{name}"
    os.makedirs(repo_dir, exist_ok=True)
    
    # Write README
    readme_path = os.path.join(repo_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_content)
    
    # Git init and commit
    subprocess.run(["git", "init"], cwd=repo_dir, capture_output=True)
    subprocess.run(["git", "add", "README.md"], cwd=repo_dir, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", f"Initial commit: {tagline}"],
        cwd=repo_dir,
        capture_output=True
    )
    
    # Create GitHub repo and push
    result = subprocess.run(
        [
            "gh", "repo", "create", name,
            "--public",
            "--source=.",
            "--push",
            "--description", tagline
        ],
        cwd=repo_dir,
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        # Extract URL from output
        for line in result.stdout.split('\n') + result.stderr.split('\n'):
            if 'github.com' in line:
                return True, line.strip()
        return True, f"https://github.com/Yoakshat/{name}"
    else:
        return False, result.stderr


def main():
    theme = sys.argv[1] if len(sys.argv) > 1 else None
    
    print("🤖 Idea Agent activated...")
    print()
    
    # Pick an idea
    base_name, tagline, description, category = pick_idea(theme)
    
    # Add suffix to make unique
    suffix = generate_unique_suffix()
    name = f"{base_name}-{suffix}"
    
    print(f"💡 Idea: {name}")
    print(f"📝 Tagline: {tagline}")
    print(f"📁 Category: {category}")
    print()
    
    # Generate README
    readme = generate_readme(base_name, tagline, description, category)
    
    print("🔨 Creating repository...")
    success, result = create_repo(name, tagline, readme)
    
    if success:
        print(f"✅ Success! Repository created:")
        print(f"   {result}")
    else:
        print(f"❌ Failed: {result}")
    
    print()
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
