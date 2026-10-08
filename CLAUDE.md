# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The Lusha Knowledge Hub: a [Mintlify](https://mintlify.com) docs site (API docs, MCP docs, user guide, changelog). There is no application code, build step, or test suite - only MDX pages, `docs.json`, OpenAPI specs, and assets. Changes merged to `main` deploy automatically via the Mintlify GitHub app.

## Commands

The Mintlify CLI (`mint`) is not installed by default: `npm i -g mint`.

- `mint dev` - local preview at `http://localhost:3000` (run from the repo root, where `docs.json` lives)
- `mint broken-links` - check internal links
- `mint update` - update the CLI if the dev server misbehaves

## Architecture

**`docs.json` is the single source of truth for navigation.** A page only appears on the site if it is listed there; a new `.mdx` file that isn't added to `docs.json` is unreachable. Page references omit the extension (`"enrichment/search-contacts"`). The file also holds theme/branding, the API playground config, and a large `redirects` array (~90 entries) - when moving or renaming a page, update both the nav entry and add a redirect.

Top-level tabs: Home, Lusha Data, API Docs, MCP Docs, User Guide, Changelog. Key points:

- **API Docs has two versions** under one tab: V3 (default, `openapi.json`) and V2 Legacy (`v2/openapi.json`). V2 is a full parallel tree under `v2/` (its own `introduction`, `authentication`, `api-reference/`, etc.) - changes to V3 do not touch it.
- **Two page types per API feature, deliberately split:**
  - `api-reference/**` pages are thin: frontmatter with `openapi: "post /v3/contacts/search"` binds the page to an endpoint in `openapi.json`, which Mintlify renders (params, responses, playground). Hand-written prose is supplementary.
  - Conceptual/guide pages (`enrichment/`, `prospecting/`, `signals/`, `lookalikes/`, `filters/`, `credits/`, `buying-group/`, ...) are hand-written and link to the matching `/api-reference/...` page.
  - So an endpoint change usually means editing `openapi.json` **and** the guide page **and** possibly the `api-reference/` page.
- **`openapi.json` (~490 KB) is huge** - don't read it whole; grep for the path or schema name and read a narrow range.
- **User Guide** (`user-guide/`) was migrated from an Intercom help center. Its folder layout is intentionally messy (e.g. several `team-*` and `billing-*` folders); nav labels in `docs.json` define what readers see. Before creating a folder there, read the folder map in `user-guide/_STYLE_GUIDE.md` and file new articles under the existing folder for the topic. That file (underscore prefix = not published) also defines user-guide conventions: H2-start headings, `<Note>/<Tip>/<Warning>` callouts, `<Steps>` for sequential UI actions, markdown tables only, local images wrapped in `<Frame>` under `/images/user-guide/<section>/` (never hot-link Intercom's CDN), descriptive `alt` text, absolute kebab-case internal links.
- `MIGRATION_PLAN.md` tracks the Redocly → Mintlify migration status and owners; useful context for what is still stub content.
- `style.css` at the root is auto-included by Mintlify on every page (do not reference it from `docs.json`). `intercom.js` is likewise auto-loaded. Brand fonts live in `fonts/`, with the brand purple `#863fff` set in `docs.json`.

## Conventions

Follow `AGENTS.md` (read it - it is the canonical style guide). Highlights:

- Active voice, second person ("you"), concise sentences, sentence-case headings.
- Use a plain hyphen (`-`), never an em dash (`—`).
- Link the API key page as `https://dashboard.lusha.com/api/manage-api-keys`.
- Bold for UI elements (**Settings**); code formatting for file names, commands, paths, and code references.
- MDX frontmatter needs `title`, `sidebarTitle` (where nav label differs), and `description`.
- Internal links are root-relative without extension (`/enrichment/enrich-contacts`).
