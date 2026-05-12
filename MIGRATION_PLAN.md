# Redocly → Mintlify Migration Plan

**Owner:** Carolina Portela (Solutions Engineering)
**Status:** In Progress
**Last updated:** May 2026

---

## Phase 0 — Foundation

| Task | Status | Owner | Notes |
|---|---|---|---|
| Create Mintlify account | To do | TBD | |
| Create GitHub repo and connect to Mintlify | To do | TBD | Repo should live under Lusha org |
| Set up docs.json with full navigation structure | To do | TBD | 7-tab structure: Get Started, User Guide, API Reference, Data Catalog, MCP, Changelog, FAQ |
| Migrate OpenAPI spec (openapi.json) from Redocly | To do | Engineering | Validate all paths against live API |
| Set up all API Reference endpoint pages | To do | TBD | Each page needs openapi frontmatter field to connect to the spec |
| Design landing page | To do | TBD | Audience-first card layout |
| Apply Lusha brand colors and logo | To do | TBD | Match docs.lusha.com |
| Scaffold all new sections with placeholder pages | To do | TBD | Create folder structure before filling content |

---

## Phase 1 — Get Started & API Reference
**Priority:** High | **Estimated effort:** 3–5 days

| Task | Status | Owner | Notes |
|---|---|---|---|
| Write introduction.mdx | To do | TBD | Quickstart, first API call |
| Write authentication.mdx | To do | TBD | Add cURL, Python, Node.js examples |
| Write rate-limiting.mdx | To do | TBD | Confirm current limits with Engineering |
| Write error-codes.mdx | To do | TBD | Confirm error table with Engineering |
| Write credits/overview.mdx | To do | TBD | Source from Billing team |
| Write credits/costs.mdx — credit costs per endpoint | To do | TBD | Needs input from Product/Billing |
| Write credits/unified-credits.mdx | To do | TBD | Source from Sales/Product |
| Write concept pages for Enrichment, Prospecting, Signals, Webhooks, Lookalikes | To do | TBD | One overview page per section |
| Write all 40+ API endpoint pages | To do | TBD | Parameters, request/response schemas, code examples |
| Add multi-language code examples to all endpoint pages | To do | TBD | cURL, Python, Node.js |
| Validate OpenAPI spec paths against live API | To do | Engineering | Check for path mismatches or missing endpoints |
| Review all request/response schemas for accuracy | To do | Engineering | |

---

## Phase 2 — User Guide (Help Center Migration)
**Priority:** High | **Estimated effort:** 5–8 days

| Task | Status | Owner | Notes |
|---|---|---|---|
| Dashboard & search | To do | TBD | Migrate from Help Center |
| Search & lists | To do | TBD | Migrate from Help Center |
| Chrome extension — install & setup | To do | TBD | Migrate from Help Center |
| Chrome extension — usage | To do | TBD | Migrate from Help Center |
| LinkedIn extension | To do | TBD | Migrate from Help Center |
| Salesforce integration — setup | To do | TBD | Migrate from Help Center |
| Salesforce integration — field mapping | To do | TBD | Migrate from Help Center |
| HubSpot integration — setup | To do | TBD | Migrate from Help Center |
| HubSpot integration — field mapping | To do | TBD | Migrate from Help Center |
| Outreach / Salesloft / other integrations | To do | TBD | Migrate from Help Center |
| Team management — inviting users | To do | TBD | Migrate from Help Center |
| Team management — roles & permissions | To do | TBD | Migrate from Help Center |
| Billing & plan management | To do | TBD | Migrate from Help Center |
| Privacy & compliance (GDPR, CCPA, DNC) | To do | TBD | Migrate from Help Center |

> CS/Support team should review all User Guide articles before publication and own this section long-term.

---

## Phase 3 — New Sections
**Priority:** Medium | **Estimated effort:** 5–10 days

### Data Catalog

| Task | Status | Owner | Notes |
|---|---|---|---|
| Write overview page | To do | TBD | Coverage summary, deprecated fields table |
| Write contact identity, emails, phones, employment field pages | To do | TBD | Generate drafts from OpenAPI response schemas, Engineering to review |
| Write company firmographics, technologies, funding field pages | To do | TBD | Same approach |
| Write signal types page | To do | TBD | All signal names, lookback window, examples |

### MCP

| Task | Status | Owner | Notes |
|---|---|---|---|
| Write overview page | To do | TBD | What MCP is, how it connects to Lusha |
| Write setup guide | To do | Product / DevRel | Installation steps, config file format, client-specific setup |
| Write tools reference | To do | Product / DevRel | Every tool name, input/output schema |
| Write prompt examples | To do | TBD | Test prompts for common tasks |

### Changelog

| Task | Status | Owner | Notes |
|---|---|---|---|
| Write historical entries | To do | TBD | Cover major API releases from the past year |
| Agree on changelog process — who writes it and when | To do | TBD | Suggested: Eng drafts, SE/DevRel polishes |
| Decide on versioning format | To do | TBD | Date-based vs. semantic version |

### FAQ

| Task | Status | Owner | Notes |
|---|---|---|---|
| Write API & integration FAQ | To do | SE / Support | Pull from Zendesk ticket volume |
| Write data & coverage FAQ | To do | SE / Support | |
| Write credits & billing FAQ | To do | SE / Billing | |
| Write MCP FAQ | To do | Product / DevRel | Write once MCP is live |

---

## Phase 4 — Technical Polish
**Priority:** Medium | **Estimated effort:** 3–4 days

| Task | Status | Owner | Notes |
|---|---|---|---|
| Audit and fix all internal links | To do | TBD | Run link checker once all content is in |
| Build full URL redirect map from old Redocly paths | To do | Engineering | Critical before DNS cutover — see redirect table below |
| Implement redirects in docs.json | To do | Engineering | |
| Set up custom domain (docs.lusha.com → Mintlify) | To do | Engineering / DevOps | DNS change + Mintlify domain config |
| Configure analytics | To do | Engineering | Mintlify supports Segment, Mixpanel, GA4 |
| SEO review — meta descriptions and page titles | To do | Marketing | |
| Mobile and dark mode QA | To do | TBD | |
| Transfer GitHub repo to Lusha org | To do | Engineering | Must happen before launch |
| Set up branch protection and PR workflow on main | To do | Engineering | Prevent direct pushes to main |

---

## Phase 5 — Review & Launch
**Priority:** Critical | **Estimated effort:** 3–5 days

| Task | Status | Owner | Notes |
|---|---|---|---|
| Internal review — API accuracy | To do | Engineering | |
| Internal review — User Guide accuracy | To do | Customer Success / Support | |
| Internal review — brand and design | To do | Marketing | |
| Address review feedback | To do | TBD | Buffer 2–3 days |
| Notify existing API users of URL changes and new features | To do | Marketing / DevRel | |
| DNS cutover to Mintlify | To do | Engineering / DevOps | Plan for zero downtime — test on staging domain first |
| Monitor for broken links and 404s for first 48 hours | To do | TBD | |
| Deprecate or redirect old Redocly site | To do | Engineering | After confirmed stable on Mintlify |

---

## URL Redirect Map

| Old Redocly URL | New Mintlify URL |
|---|---|
| `docs.lusha.com/apis/openapi/enrichment/searchsinglecontact` | `docs.lusha.com/api-reference/enrichment/search-single-contact` |
| `docs.lusha.com/apis/openapi/enrichment/searchsinglecompanyv2` | `docs.lusha.com/api-reference/enrichment/search-single-company` |
| `docs.lusha.com/apis/openapi/prospecting-search-and-enrich/...` | `docs.lusha.com/api-reference/prospecting/...` |
| `docs.lusha.com/apis/openapi/contact-filters` | `docs.lusha.com/api-reference/filters/contact-departments` |
| `docs.lusha.com/apis/openapi/signals/...` | `docs.lusha.com/api-reference/signals/...` |
| `docs.lusha.com/apis/openapi/webhooks/...` | `docs.lusha.com/api-reference/webhooks/...` |

> Action: Engineering to produce the complete redirect map and implement before DNS cutover.

---

## Stakeholders

| Team | Role | Contact |
|---|---|---|
| Solutions Engineering | Project lead, API accuracy | Carolina Portela |
| Engineering (API team) | OpenAPI spec, schema review, technical validation | TBD |
| Product | MCP docs, feature descriptions | TBD |
| Developer Relations / Tech Writing | Content quality, changelog process | TBD |
| Customer Success / Support | User guide review, FAQ sourcing | TBD |
| Marketing | Brand, SEO, launch comms | TBD |
| DevOps / Infra | DNS cutover, GitHub org transfer | TBD |

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Broken URLs break existing customer integrations | High | High | Full redirect map before DNS cutover |
| OpenAPI spec inaccuracies in new playground | Medium | High | Engineering audit before launch |
| User guide content goes stale with no clear owner | High | Medium | Assign CS/Support as permanent owner |
| MCP docs live before MCP is publicly available | Medium | Medium | Hide MCP tab until beta is confirmed |
| DNS cutover causes downtime | Low | High | Cutover in low-traffic window, test on staging first |
| Help center and new docs become two sources of truth | High | Medium | Set a deprecation date for help center articles |
| Mintlify limitations found mid-migration | Low | Medium | Most gaps solvable in MDX |

---

## Open Questions

- [ ] Who owns the Mintlify account billing and settings long-term?
- [ ] Should the GitHub repo live under a personal account or the Lusha org?
- [ ] What is the target go-live date?
- [ ] Is the Help Center being fully deprecated after migration, or kept in parallel?
- [ ] Who is the permanent editor of the User Guide section?
- [ ] Does the changelog need historical entries before 2025?
- [ ] Is MCP in public beta at launch? If not, should the tab be hidden?
- [ ] What analytics platform is Lusha on — GA4, Segment, or Mixpanel?
- [ ] Are there SEO rankings on docs.lusha.com that need to be preserved?

---

## Estimated Timeline

| Phase | Work | Duration |
|---|---|---|
| Phase 0 | Foundation | 1 week |
| Phase 1 | Get Started + API Reference | 1 week |
| Phase 2 | User Guide / Help Center migration | 2 weeks |
| Phase 3 | Data Catalog + MCP + Changelog + FAQ | 2 weeks |
| Phase 4 | Technical polish + redirects + domain | 1 week |
| Phase 5 | Review + launch | 1 week |
| **Total** | | **~8 weeks** |

> Assumes 1–2 people working part-time. Can be compressed by moving Phase 3 to a post-launch iteration.
