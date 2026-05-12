# Redocly → Mintlify Migration Plan

**Owner:** Carolina Portela (Solutions Engineering)
**Status:** In Progress
**Last updated:** May 2026

---

## Phase 0 — Foundation ✅ Complete

| Task | Status | Notes |
|---|---|---|
| Create Mintlify account + GitHub repo | ✅ Done | Personal account, needs org transfer to Lusha |
| Set up `docs.json` with full navigation | ✅ Done | 7-tab structure in place |
| Migrate OpenAPI spec (`openapi.json`) | ✅ Done | Path fix applied for `/bulk/company/v2` |
| Fix all 40 API Reference endpoint pages | ✅ Done | Added `openapi` frontmatter to all MDX files |
| Design landing page | ✅ Done | Needs final visual QA |
| Apply Lusha brand colors | ✅ Done | `#863fff` purple, `#141414` near-black |
| Scaffold all new sections | ✅ Done | Stubs in place for all 7 tabs |

---

## Phase 1 — Get Started & API Reference
**Priority:** High | **Estimated effort:** 3–5 days

| Task | Owner | Notes |
|---|---|---|
| Review and update `introduction.mdx` | TBD | Check links, add code examples |
| Review `authentication.mdx` — add Python and Node.js examples | TBD | |
| Review `rate-limiting.mdx` — confirm current limits with Eng | TBD | |
| Review `error-codes.mdx` — confirm error table with Eng | TBD | |
| Write `credits/overview.mdx` | TBD | Source from Billing team |
| Fill in actual credit costs per endpoint in `credits/costs.mdx` | TBD | Needs input from Product/Billing |
| Expand `credits/unified-credits.mdx` with plan details | TBD | Source from Sales/Product |
| Audit all 40 endpoint pages for content accuracy | TBD | Compare against live Redocly docs |
| Add multi-language code examples to endpoint pages | TBD | Currently only cURL |
| Validate OpenAPI spec paths against live API | Engineering | 1 path error already found — check for more |
| Add any missing endpoints to `openapi.json` | Engineering | Signals, Webhooks, Lookalikes may be incomplete |
| Review all request/response schemas for accuracy | Engineering | |

---

## Phase 2 — User Guide (Help Center Migration)
**Priority:** High | **Estimated effort:** 5–8 days

| Task | Owner | Notes |
|---|---|---|
| Dashboard & search | TBD | Migrate from Help Center |
| Search & lists | TBD | Migrate from Help Center |
| Chrome extension — install & setup | TBD | Migrate from Help Center |
| Chrome extension — usage | TBD | Migrate from Help Center |
| LinkedIn extension | TBD | Migrate from Help Center |
| Salesforce integration — setup | TBD | Migrate from Help Center |
| Salesforce integration — field mapping | TBD | Migrate from Help Center |
| HubSpot integration — setup | TBD | Migrate from Help Center |
| HubSpot integration — field mapping | TBD | Migrate from Help Center |
| Outreach / Salesloft / other integrations | TBD | Migrate from Help Center |
| Team management — inviting users | TBD | Migrate from Help Center |
| Team management — roles & permissions | TBD | Migrate from Help Center |
| Billing & plan management | TBD | Migrate from Help Center |
| Privacy & compliance (GDPR, CCPA, DNC) | TBD | Migrate from Help Center |

> CS/Support team should review all User Guide articles before publication and own this section long-term.

---

## Phase 3 — New Sections
**Priority:** Medium | **Estimated effort:** 5–10 days

### Data Catalog

| Task | Owner | Notes |
|---|---|---|
| Write contact identity, emails, phones, employment field pages | TBD | Generate drafts from OpenAPI response schemas, Engineering to review |
| Write company firmographics, technologies, funding field pages | TBD | Same approach |
| Expand `signal-types.mdx` with all signal names and lookback details | TBD | |

### MCP

| Task | Owner | Notes |
|---|---|---|
| Review `mcp/overview.mdx` with Product | TBD | |
| Write actual installation steps in `mcp/setup.mdx` | Product / DevRel | Blocked until MCP server is in public beta |
| Complete tool-by-tool reference in `mcp/tools.mdx` | Product / DevRel | |
| Test and confirm prompt examples in `mcp/examples.mdx` | TBD | |

### Changelog

| Task | Owner | Notes |
|---|---|---|
| Write historical entries for 2025 | TBD | Cover major API releases |
| Agree on changelog process — who writes it and when | TBD | Suggested: Eng drafts, SE/DevRel polishes |
| Decide on versioning format | TBD | Date-based vs. semantic version |

### FAQ

| Task | Owner | Notes |
|---|---|---|
| Expand `faq/api.mdx` with real customer questions | SE / Support | Pull from Zendesk ticket volume |
| Expand `faq/data.mdx` | SE / Support | |
| Expand `faq/billing.mdx` | SE / Billing | |
| Write `faq/mcp.mdx` | Product / DevRel | Write once MCP is live |

---

## Phase 4 — Technical Polish
**Priority:** Medium | **Estimated effort:** 3–4 days

| Task | Owner | Notes |
|---|---|---|
| Audit and fix all internal links | TBD | Run link checker once all content is in |
| Build full URL redirect map from old Redocly paths | Engineering | Critical before DNS cutover — see redirect table below |
| Implement redirects in `docs.json` | Engineering | |
| Validate OpenAPI spec completeness against live API | Engineering | |
| Set up custom domain (`docs.lusha.com` → Mintlify) | Engineering / DevOps | DNS change + Mintlify domain config |
| Configure analytics | Engineering | Mintlify supports Segment, Mixpanel, GA4 |
| SEO review — meta descriptions and page titles | Marketing | |
| Mobile and dark mode QA | TBD | |
| Transfer GitHub repo from personal account to Lusha org | Engineering | Must happen before launch |
| Set up branch protection and PR workflow on `main` | Engineering | |

---

## Phase 5 — Review & Launch
**Priority:** Critical | **Estimated effort:** 3–5 days

| Task | Owner | Notes |
|---|---|---|
| Internal review — API accuracy | Engineering | |
| Internal review — User Guide accuracy | Customer Success / Support | |
| Internal review — brand and design | Marketing | |
| Address review feedback | TBD | Buffer 2–3 days |
| Notify existing API users of URL changes and new features | Marketing / DevRel | |
| DNS cutover to Mintlify | Engineering / DevOps | Plan for zero downtime — test on staging domain first |
| Monitor for broken links and 404s for first 48 hours | TBD | |
| Deprecate or redirect old Redocly site | Engineering | After confirmed stable on Mintlify |

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
- [ ] Should the GitHub repo stay on a personal account or move to the Lusha org now?
- [ ] What is the target go-live date?
- [ ] Is the Help Center being fully deprecated after migration, or kept in parallel?
- [ ] Who is the permanent editor of the User Guide section?
- [ ] Does the changelog need historical entries before 2025?
- [ ] Is MCP in public beta at launch? If not, should the tab be hidden?
- [ ] What analytics platform is Lusha on — GA4, Segment, or Mixpanel?
- [ ] Are there SEO rankings on `docs.lusha.com` that need to be preserved?

---

## Estimated Timeline

| Phase | Work | Duration |
|---|---|---|
| Phase 0 | Foundation | ✅ Complete |
| Phase 1 | Get Started + API Reference | 1 week |
| Phase 2 | User Guide / Help Center migration | 2 weeks |
| Phase 3 | Data Catalog + MCP + Changelog + FAQ | 2 weeks |
| Phase 4 | Technical polish + redirects + domain | 1 week |
| Phase 5 | Review + launch | 1 week |
| **Total** | | **~7 weeks from Phase 1 start** |

> Assumes 1–2 people working part-time. Can be compressed by moving Phase 3 to a post-launch iteration.
