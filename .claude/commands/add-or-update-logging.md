---
name: add-or-update-logging
description: Workflow command scaffold for add-or-update-logging in scrape.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /add-or-update-logging

Use this workflow when working on **add-or-update-logging** in `scrape`.

## Goal

Adds or updates log messages in either the workflow configuration or the email sending script to improve observability.

## Common Files

- `.github/workflows/email_job.yml`
- `send_email.py`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Edit .github/workflows/email_job.yml or send_email.py to add or update log messages
- Commit the changes with a message referencing logging

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.