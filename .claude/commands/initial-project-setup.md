---
name: initial-project-setup
description: Workflow command scaffold for initial-project-setup in scrape.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /initial-project-setup

Use this workflow when working on **initial-project-setup** in `scrape`.

## Goal

Sets up the initial project structure, including workflow configuration, main script, and documentation files.

## Common Files

- `.github/workflows/email_job.yml`
- `send_email.py`
- `.gitignore`
- `README.md`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Create .github/workflows/email_job.yml
- Create send_email.py
- Create .gitignore and README.md
- Commit all initial files

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.