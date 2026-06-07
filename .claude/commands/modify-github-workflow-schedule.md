---
name: modify-github-workflow-schedule
description: Workflow command scaffold for modify-github-workflow-schedule in scrape.
allowed_tools: ["Bash", "Read", "Write", "Grep", "Glob"]
---

# /modify-github-workflow-schedule

Use this workflow when working on **modify-github-workflow-schedule** in `scrape`.

## Goal

Adjusts the schedule or configuration of the email job GitHub Actions workflow, typically to test different cron timings or environment variables.

## Common Files

- `.github/workflows/email_job.yml`

## Suggested Sequence

1. Understand the current state and failure mode before editing.
2. Make the smallest coherent change that satisfies the workflow goal.
3. Run the most relevant verification for touched files.
4. Summarize what changed and what still needs review.

## Typical Commit Signals

- Edit .github/workflows/email_job.yml to change cron schedule or add variables
- Commit the changes with a message referencing the schedule or testing

## Notes

- Treat this as a scaffold, not a hard-coded script.
- Update the command if the workflow evolves materially.