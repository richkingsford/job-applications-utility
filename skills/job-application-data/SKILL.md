---
name: job-application-data
description: Store and retrieve reusable job-application facts from a local privacy-preserving profile without exposing personal data to Git.
---

Use this skill when an application needs recurring identity, resume, authorization, education, work-history, availability, or voluntary demographic answers.

- Read `profile.json` only when the user has authorized completing the application.
- Never commit `profile.json`, resumes, cover letters, secrets, or raw application exports.
- Keep reusable facts in the profile and role-specific facts in the application record.
- If a field is unknown or ambiguous, leave it unresolved rather than guessing.
- Validate with `python application_utility.py validate-profile` before opening a form.
- Use `python application_utility.py ashby-fields` to reduce repeated page inspection.
