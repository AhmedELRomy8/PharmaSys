# ADR-001: Use a 4-Tier Layered Architecture

* **Status:** Accepted
* **Date:** 2026-10-30 (Sprint 2 / Lab 04)
* **Deciders:** Ahmed EL-Romy (Lead), Abdelrahman Mahmoud (Architect), Ali Mahmoud (QA)

---

## 1. Context

PharmaSys is a multi-tenant pharmacy management platform serving the Damanhour University Hospital Pharmacy. The core business involves mission-critical transactions: barcode point-of-sale scanning, atomic stock decrements, expiry date enforcement, shift drawer balancing, and regulatory financial audits.

The project team consists of 3 developers working across a 10-week semester. The engineering requirements mandate that:
1. Business rules (e.g., expiry checks, atomic inventory reduction, discount limits) must be isolated from UI frameworks and delivery mechanisms.
2. In later labs (Lab 07 / Lab 08), the system must achieve high automated test coverage using unit tests with fake/mock data stores without spinning up a live database.
3. The platform must support both web access and an offline-resilient Windows desktop app with zero architectural divergence.

---

## 2. Decision

We adopt a **Strict 4-Tier Layered Architecture**:

```
Presentation (Routers / Controllers)
         ↓
Service Layer (Business Logic & Orchestration)
         ↓
Repository Layer (Data Access Interfaces & Implementations)
         ↓
Persistence Layer (SQLAlchemy ORM + Database / Hardware Drivers)
```

### Architectural Rules Enforced:
1. **Unidirectional Downward Dependency:** Each layer only depends on the layer immediately below it or on abstractions (interfaces). Dependencies never point upward.
2. **Controller/Router Isolation:** Routers handle HTTP request parsing, Pydantic validation, status codes, and response serialization. **Routers never execute business calculations and never query the database or repositories directly.**
3. **Repository Abstraction:** Service classes depend exclusively on repository interfaces (`IMedicineRepository`, `ISaleRepository`, `IUserRepository`), not on concrete database sessions.
4. **Data Transfer Objects (DTOs):** Information crosses architectural boundaries using strongly typed schemas/DTOs.

---

## 3. Alternatives Considered

### Option A: Monolithic Flat Scripts / "Smart Controllers" (Rejected)
* **Description:** Placing database queries and business validation directly inside endpoint route handlers (common in rapid prototyping or basic tutorials).
* **Reason for Rejection:** Makes unit testing impossible without an active database connection; duplicates logic between Web and Desktop interfaces; leads to code rot and tight coupling.

### Option B: Django-Style Fat Models / Active Record (Rejected)
* **Description:** Entities contain both business logic and persistence methods (`medicine.save()`, `sale.charge()`).
* **Reason for Rejection:** Couples the domain model directly to the database schema; makes unit testing slow and cumbersome; violates Single Responsibility Principle.

### Option C: Microservices Architecture (Rejected)
* **Description:** Splitting Auth, POS, Inventory, and Reporting into autonomous microservices communicating via gRPC/HTTP.
* **Reason for Rejection:** Unwarranted operational complexity for a 3-person team; introduces network latency that endangers the $< 200\text{ ms}$ barcode scanning SLA; distributed transactions across POS and Inventory would require complex two-phase commits or saga orchestrators.

---

## 4. Consequences

### Positive (Gains):
* **High Testability:** Business logic in the Service layer can be unit tested in milliseconds by injecting in-memory mock repositories (critical for Lab 07 TDD and Lab 08 integration).
* **Pluggable Persistence:** Switching between SQLite (local development and offline desktop mode) and PostgreSQL (cloud multi-tenant production) requires zero changes to the Service or Router layers.
* **Clear Team Boundaries:** Team members can work concurrently on Routers, Services, and Repositories with minimal merge conflicts.

### Negative & Trade-offs (Accepted Costs):
* **Boilerplate Overhead:** Requires creating explicit DTOs, interface protocols, and mapper functions across layers for even simple CRUD operations.
* **File Proliferation:** More files per feature (Router + Service + Repository + Model + Schema), requiring strict naming conventions and directory organization.
