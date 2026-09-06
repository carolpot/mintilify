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
