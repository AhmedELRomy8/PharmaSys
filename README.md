# PharmaSys

**A SaaS pharmacy management platform — built for the Damanhour University Hospital pharmacy.**

PharmaSys gives hospital pharmacies a barcode-driven point of sale, live inventory with expiry tracking, invoicing and barcode label printing, staff shift management, and sales reports — delivered as a web app (SaaS, multi-tenant) and as an installable Windows desktop application.

> Software Engineering Final Project · Faculty of Computers and Information, Damanhour University · 2027

## Vision

Hospital pharmacies lose time and money to manual sales logs, expired stock sold by mistake, and no visibility over revenue. PharmaSys digitizes the whole counter: the default screen is the **sales invoice** — the cashier scans a barcode, the item and price appear instantly, the bill totals itself, and stock decrements safely. Admins get a live dashboard, expiry and low-stock alerts, staff working hours, and period reports. The platform is multi-tenant by design: one deployment serves many pharmacies — the first tenant is the Damanhour University Hospital pharmacy.

## Features

- Login with role-based access control (super admin / admin / staff)
- Barcode-driven POS — scan → item + price in the cart; expired and out-of-stock items are blocked
- Inventory with dosage forms (tablets, syrup, drops, ointment…), package units, prices, expiry dates and low-stock thresholds
- Invoices (A4 + 80 mm thermal receipt) and printable barcode labels for medicines
- Admin dashboard, sales and inventory reports, staff working hours, shifts
- Devices (barcode scanner, thermal printer) detected automatically
- Ships as a standard Windows desktop app — `PharmaSys-Setup.exe`, desktop shortcut, zero prerequisites

## Team

| Member | GitHub | Lab roles |
| --- | --- | --- |
| Ahmed Tamer ELromy | [@AhmedELRomy8](https://github.com/AhmedELRomy8) | Team Lead · Git Master |
| Ali Mahmoud | [@AliMahmoud25845](https://github.com/AliMahmoud25845) | QA Lead |
| Abdelrahman Mahmoud | [@AbdelrahmanMahmoud312005](https://github.com/AbdelrahmanMahmoud312005) | Architect |

The working agreement — rules, story ownership, sprints — lives in [`docs/team/TEAM-PLAN.md`](docs/team/TEAM-PLAN.md), with one personal playbook per member in `docs/team/`.

## Tech stack

| Layer | Choice |
| --- | --- |
| Backend | Python · FastAPI · SQLAlchemy — layered: router → service → repository |
| Database | SQLite (development) · PostgreSQL (production) |
| Frontend | React · Vite · TypeScript · Tailwind CSS |
| Devices | WebHID / WebUSB with keyboard-mode fallback |
| Packaging | Electron + PyInstaller → NSIS installer |
| Quality | pytest · ruff · GitHub Actions |

Every significant decision is recorded as an ADR in `docs/adr/`.

## Repository layout

```
PharmaSys/
├── docs/
│   ├── team/          # TEAM-PLAN.md + a personal playbook per member
│   ├── diagrams/      # PlantUML sources (Labs 3–4)
│   ├── adr/           # architecture decision records
│   └── requirements.md
├── backend/           # FastAPI application (added in the Lab 4 sprint)
├── frontend/          # React application (added in the Lab 4 sprint)
├── tests/             # unit + integration tests (Labs 7–8)
└── .github/workflows  # CI pipeline (Lab 9)
```

## Workflow

Every change reaches `main` through a reviewed pull request (GitHub Flow):

1. branch — `feature/US-07-scan-barcode`
2. small conventional commits — `feat(pos): add scan to cart`
3. pull request — reviewed by a teammate (rotation defined in TEAM-PLAN)
4. merge — then the board card moves to Done

**Merge-conflict drill (Lab 1):** the three first PRs each append a row to `TEAM.md` on purpose, so a merge conflict is guaranteed during Sprint 0 and gets resolved hands-on. Each PR description documents how the conflict was resolved.

## Status

Sprint 0 — repository bootstrap. The roadmap and per-member ownership live in [`docs/team/TEAM-PLAN.md`](docs/team/TEAM-PLAN.md).
