# User Guide style guide (internal — not published)

Working conventions for `user-guide/**/*.mdx`, applied section by section.
Underscore prefix keeps Mintlify from routing/publishing this file.

## Frontmatter
- `title`: sentence case ("How to reset your password", not "How To Reset Your Password").
  Keep existing question-form titles ("Why was my payment declined?") as-is — just fix casing.
- `description`: one sentence, sentence case, no trailing period change needed if already fine.
- No `icon` field (nav icons are set per-dropdown/group in docs.json, not per-page).

## Headings
- Body starts at `##` (H2). Never `#` (H1) — the frontmatter `title` is the H1.
- Sentence case for all headings ("How to access the Coaching tab", not "How To Access...").

## Callouts
Map ad-hoc patterns to real Mintlify components:
- `**Note:**` / blockquote asides → `<Note>...</Note>`
- `**Tip:**` → `<Tip>...</Tip>`
- `**Important:**` / anything cautionary (data loss, billing impact, irreversible action) → `<Warning>...</Warning>`
- Keep `<Info>` only for "see also / cross-reference" asides (existing usage).

## Step-by-step instructions
- A numbered markdown list (`1. `, `2. `, ...) where each item is a sequential
  action the reader performs in the product UI ("Click X", "Go to Y", "Select
  Z") → convert to `<Steps>` / `<Step title="...">...</Step>`. The step title
  is a short imperative summary of the action; the body is the existing
  explanatory text/links. Reference: `user-guide/dashboard.mdx`'s "Getting
  oriented" section.
- Do NOT convert a numbered list that isn't sequential UI steps: FAQ answers,
  reasons/causes (e.g. "why an email bounced"), requirements/prerequisites,
  or an enumeration of options. Leave those as plain numbered or bulleted
  markdown lists. If ambiguous, leave as-is rather than force it.

## Tables
- Markdown tables only (never raw `<table>`).
- Header row in Title Case, one-space-padded pipes: `| Field | Description |` / `| --- | --- |`
  (not aligned/padded dashes — keeps diffs small and consistent).

## Images
- Never hot-link `downloads.intercomcdn.eu` (or any third-party CDN) — download the asset,
  save under `/images/user-guide/<section>/<slug>.png`, reference locally.
- Wrap in `<Frame>`: `<Frame><img src="/images/user-guide/..." alt="Descriptive alt text" /></Frame>`.
- Every image gets real, descriptive `alt` text (never empty).

## Links
- Internal links: absolute path, all-lowercase-kebab-case, no file extension:
  `/user-guide/<section>/<slug>`.
- Fix any Title-Case/URL-encoded/space-containing path segments to plain kebab-case
  (update the actual folder/file only if safe + update docs.json references — otherwise
  leave path alone and just fix the link text/casing shown to the reader).

## Folder map (authoring reference — not a rename plan)

Several logical topics are split across multiple physical folders, a holdover from the
original Intercom export. The **nav labels in docs.json are the source of truth** for
what the reader sees; these folders are not renamed/merged (too much link-breakage risk
for a cosmetic win — see PR discussion). When adding a new article, file it under the
existing folder for its topic rather than creating a new one:

| Logical topic (nav) | Physical folder(s) |
| --- | --- |
| Getting Started | `getting-started/` |
| Workspace intro | `introduction-and-getting-started/` |
| Prospecting getting-started | `getting-started-with-prospecting/` |
| Conversations getting-started | `getting-started-with-conversations/` |
| Engage getting-started | `getting-started-with-engage/` |
| Team & admin | `account-and-team-management/`, `team-management/`, `team-and-administration/`, `manage-your-team-capabilities/`, `manage-your-users/` |
| Billing & plans | `billing-and-plans/`, `billing-and-payments/`, `plans-and-upgrades/` |

If you're about to create a folder starting with `getting-started-*`, `team-*`, or
`billing-*`/`plans-*`, check this table first — it almost certainly already exists.
