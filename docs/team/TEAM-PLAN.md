# PharmaSys — Team Plan & Working Agreement

> One team, one product, ten labs. This file is our single source of truth for **who does what, when, and how it shows on GitHub**.
> Each member also has a personal playbook in this folder (`ahmed.md`, `ali.md`, `abdelrahman.md`) — that is the file you work from on your own machine every week.

---

## 1. The product in one paragraph

PharmaSys is a **SaaS pharmacy management platform**. Its first tenant is the **Damanhour University Hospital pharmacy**: a barcode-driven POS (the default screen after login), inventory with expiry & low-stock tracking, invoicing, barcode label printing, shifts and working hours, sales reports, and an admin dashboard. The finished product ships in two modes from one codebase: as a **web app** (SaaS, multi-tenant) and as an **installable Windows desktop application** (`PharmaSys-Setup.exe` → installs to `C:\Program Files`, desktop shortcut, runs on any PC with zero prerequisites).

**Stack (see ADRs):** FastAPI backend in layers (router → service → repository) · SQLite for dev, PostgreSQL for production · React + Vite + TypeScript + Tailwind frontend · Electron + PyInstaller for the desktop build · pytest + GitHub Actions for quality.

## 2. Team roles (Lab 1)

| Member | GitHub | Lab-1 roles | Owns |
|---|---|---|---|
| Ahmed Tamer | @AhmedELRomy8 | Team Lead + Git Master | board hygiene, meetings, demo script, branch protection, merges, release tags |
| Ali Mahmoud | @AliMahmoud25845 | QA Lead | test strategy, pytest infrastructure, coverage, CI quality gates |
| Abdelrahman Mahmoud | @AbdelrahmanMahmoud312005 | Architect | diagrams, ADRs, package structure, design consistency |

Doc Lead rotates per sprint (see §6). With 3 people and 5 lab roles, some members hold two roles — that is expected.

## 3. Ground rules (non-negotiable)

1. **No direct commits to `main`.** The only exception is the one-time repository initialization in Sprint 0. Everything else: branch → PR → review → merge.
2. **Branch naming:** `feature/US-07-scan-barcode` · `docs/requirements` · `test/US-08-bills` · `ci/pipeline` · `fix/pos-total-rounding`.
3. **Conventional commits:** `feat(pos): add barcode scan to cart`, `docs(adr): add ADR-001 layered architecture`, `test(auth): login failure scenarios`. Never `update`, `final2`.
4. **Small commits.** A story PR usually has 4–8 commits: model → repository → service → API → UI → tests → docs.
5. **Review rotation:** Ahmed's PRs → **Ali** reviews · Ali's PRs → **Abdelrahman** reviews · Abdelrahman's PRs → **Ahmed** reviews. Nobody reviews their own PR. Every review starts with a **10-minute verbal walkthrough** by the author — this is deliberate training for the oral exam.
6. **Definition of Done — every PR:**
   - [ ] Branch and commits follow rules 2–4
   - [ ] Layering respected (UI never touches the database; business rules live in services)
   - [ ] The story's Gherkin scenarios pass as tests
   - [ ] README/docs updated when the feature changes usage
   - [ ] Issue linked with `Closes #N`
   - [ ] Board card moved Review → Done after merge
7. **Board:** every issue sits on the project board and moves Backlog → To Do → In Progress → Review → Done. You move **your own** cards.
8. **Issues:** every issue gets a priority label (`must` / `should` / `could`), the `user-story` label, and an assignee. New issues are created **by their future owner** (bodies are ready to paste in each personal playbook).
9. **Honesty rule:** if you cannot finish your story in a sprint, say it in the weekly meeting and re-assign it visibly in this file. Silently dropping work breaks the team grade, not just yours.

## 4. Story ownership — 21 user stories, 7 per member

Every story is a **full-stack slice** (model + repository + service + API + UI + tests) owned end-to-end by one member. This satisfies the course rule *"every team member must actively contribute to all layers"*.

| Story | GitHub issue | Priority | Owner | Sprint |
|---|---|---|---|---|
| US-01 Login & authentication | #1 | Must | Ahmed | S2 |
| US-02 Role-based access control | #2 | Must | Ali | S3 |
| US-03 Add medicines | #3 | Must | Abdelrahman | S3 |
| US-04 Update medicines | #4 | Should | Ahmed | S5 |
| US-05 Delete medicines (admin only) | #5 | Should | Ali | S4 |
| US-06 Search medicines | #6 | Must | Abdelrahman | S3 |
| US-07 Scan barcodes → POS cart | #7 | Must | Ahmed | S3 |
| US-08 Calculate bills | #8 | Must | Ali | S3 |
| US-09 Record customer information | #9 | Should | Abdelrahman | S4 |
| US-10 Complete sales & generate invoices | #10 | Must | Ahmed | S4 |
| US-11 Manage staff shifts | #11 | Should | Ali | S4 |
| US-12 Monitor inventory (stock + expiry) | #12 | Should | Abdelrahman | S4 |
| US-13 Generate sales reports | #13 | Should | Ahmed | S5 |
| US-14 View staff working hours | #14 | Should | Ali | S5 |
| US-15 Manage staff accounts | new — Ahmed creates | Should | Ahmed | S5 |
| US-16 Admin dashboard | new — Abdelrahman creates | Should | Abdelrahman | S5 |
| US-17 Camera barcode scanning | new — Abdelrahman creates | Could | Abdelrahman | S6 |
| US-18 Sales refund | new — Ali creates | Could | Ali | S6 |
| US-19 Generate & print barcode labels | new — Ahmed creates | Should | Ahmed | S6 |
| US-20 Device hub (scanner & printer auto-detection) | new — Ali creates | Could | Ali | S7 |
| US-21 Desktop installer (setup.exe) | new — Abdelrahman creates | Should | Abdelrahman | S7–S8 |

**MVP scope (demoed from S4 onward):** US-01, US-02, US-03, US-06, US-07, US-08, US-10 + NFR-02 (bcrypt). Everything else layers on top.

## 5. Docs, diagrams, ADRs, tests and CI — who authors what

Authorship of documentation is contribution too — it rotates.

| Deliverable | Author | Reviewer(s) | Sprint |
|---|---|---|---|
| Repo init commit (README, .gitignore, LICENSE, TEAM.md, this file) | Ahmed | — (one-time direct init) | S0 |
| Personal playbook + TEAM.md profile — 3 PRs | each member | next in rotation | S0 |
| New issues US-15…US-21 (bodies ready in personal playbooks) | story owner | — | S0 |
| Labels + assignees on the existing 14 issues | issue owner | — | S0 |
| `docs/requirements.md` | Ahmed | Ali **and** Abdelrahman (2 approvals) | S1 |
| Gherkin comments on the top-5 stories (US-01, 03, 07, 08, 10) | story owners | — | S1 |
| `docs/use-cases/UC-login.md` / `UC-add-medicine.md` / `UC-calculate-bill.md` | Ahmed / Abdelrahman / Ali | rotation | S1 |
| `docs/diagrams/use-case.puml` (assembled) | Abdelrahman | Ahmed | S1 |
| `docs/diagrams/class.puml` | Abdelrahman | Ahmed | S2 |
| `docs/diagrams/sequence-sale.puml` + `state-sale.puml` | Ahmed | Ali | S2 |
| `docs/diagrams/sequence-add-medicine.puml` | Abdelrahman | Ali | S2 |
| `docs/diagrams/component.puml` | Abdelrahman | Ali | S2 |
| ADR-001 Layered architecture | Abdelrahman | Ahmed | S2 |
| ADR-002 Technology stack | Ali | Ahmed | S2 |
| ADR-003 Authentication strategy (JWT + bcrypt + roles) | Ahmed | Ali | S3 |
| ADR-004 Multi-tenancy (shared schema, `pharmacy_id` scoping) | Ahmed | Abdelrahman | S3 |
| Backend skeleton + US-01 vertical slice (reference implementation) | Ahmed | Ali | S2 |
| Frontend shell (layout, routing, auth context) | Ali | Abdelrahman | S2 |
| Base SQLAlchemy models (from the class diagram) | Abdelrahman | Ahmed | S2 |
| pytest infrastructure (conftest, fixtures, coverage config) | Ali | Ahmed | S5 |
| Tests for each story's Gherkin scenarios | story owner | rotation | S5–S6 |
| Seed script — realistic demo data (Egyptian medicines) | Ahmed | Ali | S4 |
| CI workflow (ruff lint + pytest on every PR) | Ali | Ahmed | S7 |
| ADR-005 Device access strategy (WebHID / WebUSB + keyboard fallback) | Ali | Abdelrahman | S7 |
| ADR-006 Desktop packaging (Electron + PyInstaller vs alternatives) | Abdelrahman | Ahmed | S7 |
| Desktop build + installer (US-21) | Abdelrahman | Ahmed | S7–S8 |
| Demo script + release notes + `v1.0.0` tag | Ahmed | both | S8 |
| SRS final report — Requirements ch. / Design ch. / Testing & CI ch. | Ahmed / Abdelrahman / Ali | each other | S8 |

## 6. Sprint calendar

Dates are approximate — adjust together when the real lab schedule differs, but never let this table go stale.

| Sprint | Dates (approx) | Lab focus | Milestones |
|---|---|---|---|
| S0 | Oct 25 – Oct 31 | finish Lab 1 & 2 gaps | repo init, branch protection, board, labels, 3 playbook PRs (conflict drill), new issues, requirements.md started. Each member receives a **personal kit** (double-click `.bat` scripts) that automates the git mechanics of Sprint 0 and the weekly loop. |
| S1 | Nov 1 – Nov 7 | Lab 3 | `docs/requirements.md` merged, Gherkin on issues, use-case docs + `use-case.puml` |
| S2 | Nov 8 – Nov 14 | Lab 4 | class / component / sequence / state diagrams, ADR-001 & ADR-002, backend skeleton + US-01, frontend shell, base models |
| S3 | Nov 15 – Nov 21 | Lab 5 | **MVP core:** US-02, US-03, US-06, US-07, US-08, ADR-003, ADR-004 |
| S4 | Nov 22 – Nov 28 | Lab 6 | **MVP complete:** US-10, US-05, US-09, US-11, US-12, seed data → first full demo |
| S5 | Nov 29 – Dec 5 | Lab 7 | US-13, US-14, US-15, US-16, US-04 + pytest week (everyone writes tests for their stories) |
| S6 | Dec 6 – Dec 12 | Lab 8 | US-19, US-18, US-17 + integration tests |
| S7 | Dec 13 – Dec 19 | Lab 9 | CI workflow, US-20 device hub, US-21 packaging starts, ADR-005 & ADR-006 |
| S8 | Dec 20 – Jan 2 | Lab 10 | installer final, clean-code pass, SRS report, demo rehearsal, `v1.0.0` |

## 7. How individual contribution is measured — and how this plan covers it

The lab grades 20% on **individual git history + oral questions**. The TA reads these signals on GitHub:

| Signal on GitHub | How this plan guarantees it |
|---|---|
| Commits per account (Insights → Contributors) | every member commits weekly, from their own machine, on their own branches |
| PRs opened & merged | ~13–14 merged PRs per member across the semester |
| Reviews given (approvals) | the rotation gives every member roughly one review per week |
| Issues authored / assigned / commented | the original 14 are already split 5/5/4 by author; the new 7 are created by their owners; Gherkin comments come from owners |
| Project board activity | each member moves their own cards through the columns |
| Balanced authorship | 7 stories each, plus rotating docs/diagram/ADR/test/CI authorship (§5) |

**About AI tools:** the course allows them, but every member must understand every line they merge — the instructors may ask for line-by-line explanation, live refactoring, or re-creation of deleted code. That is why rule 5 forces a verbal walkthrough on every PR, and why each personal playbook ends with oral-exam prep questions. **If you cannot explain it, do not merge it.**
