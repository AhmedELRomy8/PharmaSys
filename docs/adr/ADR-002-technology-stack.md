# ADR-002: Technology Stack & Core Framework Selection

* **Status:** Accepted
* **Date:** 2026-10-30 (Sprint 2 / Lab 04)
* **Deciders:** Ahmed EL-Romy (Lead), Abdelrahman Mahmoud (Architect), Ali Mahmoud (QA)

---

## 1. Context

PharmaSys requires an end-to-end technology stack that satisfies stringent operational constraints:
1. **Sub-200ms POS Response Time:** Barcode scans must resolve medicine details, price, and expiry status near-instantaneously at the hospital counter.
2. **Dual Deployment Mode:** The application must function as a multi-tenant cloud web service for hospital administrators while providing an installable, single-click Windows desktop application (`PharmaSys-Setup.exe`) for pharmacy cashiers with local hardware access (barcode scanners, thermal printers).
3. **Data Integrity & Concurrency:** Real-time atomic inventory deduction during simultaneous checkouts without phantom reads or negative stock.
4. **Student Team Productivity:** A cohesive stack allowing 3 developers to deliver clean code, architectural diagrams, unit tests, and CI/CD pipelines within a 10-week academic schedule.

---

## 2. Decision

We choose the following unified technology stack:

| Component | Selected Technology | Primary Justification |
|:---|:---|:---|
| **Backend Language & Runtime** | **Python 3.12+** | Robust standard library, type annotations (`typing`), fast development speed, native ecosystem for data analysis and pharmaceutical audits. |
| **Backend API Framework** | **FastAPI** | High-performance asynchronous execution (Starlette + Uvicorn), native Pydantic v2 data validation, and automatic OpenAPI / Swagger documentation out of the box. |
| **Object-Relational Mapping (ORM)** | **SQLAlchemy 2.0 (Async)** | Industry-standard typed query builder with complete decoupling between domain models and database engines. |
| **Frontend Framework & Tooling** | **React 19 + TypeScript + Vite** | Strict component-level type safety, rapid HMR build cycles, and rich component ecosystem for complex medical dashboards and POS grids. |
| **Styling & Design System** | **Tailwind CSS** | Utility-first CSS ensuring lightweight bundles, rapid custom UI construction, and clean responsive layouts for desktop and tablet screens. |
| **Database Engines** | **SQLite (Dev & Offline Desktop)**<br>**PostgreSQL 16 (Cloud Multi-Tenant)** | SQLite with WAL mode provides zero-configuration embedded storage for local desktop installations; PostgreSQL provides ACID multi-tenant tenancy in production. |
| **Desktop Shell** | **Electron + PyInstaller (NSIS)** | Packages the React frontend and embedded FastAPI engine into a native Windows executable with direct WebHID / USB scanner access. |

---

## 3. Alternatives Considered

### Option A: Django + Django REST Framework (DRF) (Rejected)
* **Description:** Traditional batteries-included Python web framework.
* **Reason for Rejection:** Synchronous execution model by default; heavy memory footprint; rigid monolithic structure makes embedded desktop distribution heavier and slower to start; ORM is tightly bound to Django's internals, hindering repository abstraction.

### Option B: Node.js + Express / NestJS (Rejected)
* **Description:** JavaScript/TypeScript full-stack across client and server.
* **Reason for Rejection:** While offering a single language, Node.js lacks Python's native strength in scientific data processing and automated financial reporting; NestJS introduces heavy dependency injection boilerplate that exceeds the requirements of a 10-week project.

### Option C: Native Windows C# / .NET (WPF / WinUI 3) (Rejected)
* **Description:** Pure native Windows desktop development.
* **Reason for Rejection:** Vendor lock-in prevents cross-platform cloud/web deployment; violates the multi-tenant SaaS requirement for remote hospital administrators; team has higher collective velocity in Python and TypeScript.

---

## 4. Consequences

### Positive (Gains):
* **High Performance & Low Latency:** FastAPI's asynchronous event loop easily meets the $< 200\text{ ms}$ barcode scanning SLA.
* **Strict Type Safety:** Pydantic v2 and TypeScript eliminate runtime type mismatches between frontend API calls and backend domain handlers.
* **Interactive Documentation:** Automatic OpenAPI documentation (`/docs`) accelerates frontend-backend integration and API testing (Lab 08).
* **Dual Deployment Parity:** The exact same React/FastAPI codebase powers both the SaaS cloud portal and the standalone Windows desktop app.

### Negative & Trade-offs (Accepted Costs):
* **Asynchronous SQLAlchemy Learning Curve:** Requires explicit management of async sessions and transaction context managers (`async with session.begin()`).
* **Packaging Size:** Bundling Python runtime and Chromium via Electron produces a larger setup file size (~80–120 MB) compared to a pure native C++ or C# application.
