```markdown
# scrape Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches you the core development patterns and workflows used in the `scrape` Python repository. The project is focused on scripting (not using a framework), with automation via GitHub Actions for tasks such as sending emails. You'll learn about the project's coding conventions, how to modify workflow schedules, enhance logging, and set up the project from scratch.

## Coding Conventions

- **File Naming:**  
  Use `snake_case` for all Python files and scripts.  
  _Example:_  
  ```
  send_email.py
  scrape_utils.py
  ```

- **Import Style:**  
  Prefer relative imports within the package.  
  _Example:_  
  ```python
  from .helpers import build_email_body
  ```

- **Export Style:**  
  Use named exports (define functions/classes explicitly, avoid wildcard `*` imports/exports).  
  _Example:_  
  ```python
  def send_email(...):
      ...
  ```

- **Commit Messages:**  
  Freeform, typically short (average 23 characters).  
  _Example:_  
  ```
  Update email job schedule
  Add logging to send_email
  ```

## Workflows

### Modify GitHub Workflow Schedule
**Trigger:** When you want to test or update the schedule/frequency or environment of the automated email job.  
**Command:** `/update-workflow-schedule`

1. Open `.github/workflows/email_job.yml`.
2. Edit the `schedule` section to change the cron timing, or add/update environment variables.
   ```yaml
   on:
     schedule:
       - cron: '0 8 * * *'  # Runs every day at 8 AM UTC
   ```
3. Commit the changes with a message referencing the schedule or testing.
   ```
   Update email job schedule to 8 AM UTC
   ```

### Add or Update Logging
**Trigger:** When you want to enhance logging for debugging or monitoring purposes.  
**Command:** `/add-logging`

1. Open either `.github/workflows/email_job.yml` or `send_email.py`.
2. Add or update log messages.
   - In Python:
     ```python
     import logging

     logging.info("Starting email send process")
     ```
   - In GitHub Actions:
     ```yaml
     - name: Log start
       run: echo "Starting email job"
     ```
3. Commit the changes with a message referencing logging.
   ```
   Add info log to send_email.py
   ```

### Initial Project Setup
**Trigger:** When starting a new project or repository.  
**Command:** `/init-project`

1. Create `.github/workflows/email_job.yml` for automation.
2. Create `send_email.py` as the main script.
3. Add `.gitignore` and `README.md` for housekeeping and documentation.
4. Commit all initial files.
   ```
   Initial project setup
   ```

## Testing Patterns

- **Framework:** Unknown (not explicitly detected).
- **File Pattern:** Test files are named with the pattern `*.test.*`.
  _Example:_  
  ```
  send_email.test.py
  ```
- **Note:** If you add tests, follow the above naming convention for consistency.

## Commands

| Command                   | Purpose                                                          |
|---------------------------|------------------------------------------------------------------|
| /update-workflow-schedule | Update or test the schedule/environment of the email job workflow |
| /add-logging              | Add or enhance logging in scripts or workflows                   |
| /init-project             | Set up the initial project structure                             |
```