# Software Requirements Specification (SRS) — PharmaSys

**Course:** Software Engineering — Practical Lab 02: Requirements Engineering  
**Academic Year:** 3rd Year, Fall 2026 / 2027  
**Faculty:** Faculty of Computers and Information, Damanhour University  
**Supervisor:** Prof. Dr. Amr Abohany  
**Project:** PharmaSys — SaaS Pharmacy Management Platform  
**Target Organization:** Damanhour University Hospital Pharmacy  
**Repository:** [https://github.com/AhmedELRomy8/PharmaSys](https://github.com/AhmedELRomy8/PharmaSys)  

---

## Team Members & Responsibilities

| Member Name | GitHub Account | Course Roles | Story Ownership |
|:---|:---|:---|:---:|
| **Ahmed Tamer Elromy** | [@AhmedELRomy8](https://github.com/AhmedELRomy8) | Team Lead & Git Master | 9 Stories + Core Architecture |
| **Ali Mahmoud Ali** | [@AliMahmoud25845](https://github.com/AliMahmoud25845) | QA Lead & Doc Lead | 9 Stories + Testing / CI |
| **Abdelrahman Mahmoud Ali** | [@AbdelrahmanMahmoud312005](https://github.com/AbdelrahmanMahmoud312005) | System Architect | 9 Stories + Packaging / ADRs |

---

## 1. Executive Overview & Stakeholder Roles

### 1.1 Problem Statement & Solution
Hospital pharmacies experience significant losses in time and revenue due to manual sales logs, dispensing expired or out-of-stock medications by error, lack of real-time inventory visibility, and adverse drug interaction risks during hurried emergency shifts.

**PharmaSys** is an engineered SaaS platform built specifically for the **Damanhour University Hospital Pharmacy**. It prioritizes a barcode-driven **Point of Sale (POS) sales invoice as the default landing screen** upon authentication. A cashier scans a medicine barcode; the item, dosage form, and price drop into the cart instantly; the total is calculated; payment is processed; stock decrements atomically; and an itemized invoice (A4 / 80 mm thermal receipt) is printed.

The platform is designed to be deployed in two modes from a single unified codebase:
1. **Multi-tenant Cloud Web Application (SaaS)** for centralized hospital management.
2. **Standalone Windows Desktop Application (`PharmaSys-Setup.exe`)** with zero runtime prerequisites, running offline-ready at pharmacy checkout counters.

### 1.2 User Roles & Personas
To ensure comprehensive domain coverage, PharmaSys models three primary internal user roles and accounts for the customer beneficiary:

1. **Super Admin (Hospital System Administrator):**
   - Owns system-wide configurations, tenant onboarding, global security policies, and technical diagnostics.
2. **Admin (Pharmacy Manager / Chief Pharmacist):**
   - Manages medicine catalog, sets dosage forms and package units, reviews low-stock and expiry alerts, approves discounts, audits shift hours, and generates financial/sales reports.
3. **Staff (Pharmacist / Cashier):**
   - Operates the POS checkout counter, scans barcodes, inputs customer details, handles cash/card payments, prints sales receipts, and checks for drug interactions.
4. **Customer / Patient (Beneficiary):**
   - Receives itemized invoices with clear medicine names, dosage forms, batch numbers, and expiry dates, preventing billing disputes and counterfeit/expired medications.

---

## 2. Product Backlog — 27 User Stories (INVEST & MoSCoW)

Every user story strictly adheres to the standard agile template:
$$\text{As a } \langle\text{role}\rangle, \text{ I want } \langle\text{goal}\rangle \text{ so that } \langle\text{benefit}\rangle$$

All stories satisfy the **INVEST** criteria:
- **Independent:** Can be developed and deployed in isolated vertical slices.
- **Negotiable:** Implementation nuances are refined in sprint planning.
- **Valuable:** Delivers measurable end-user value to hospital pharmacy staff.
- **Estimable:** Scoped to fit within one member's sprint allocation.
- **Small:** Concise functional units without hidden technical epics.
- **Testable:** Accompanied by verifiable Gherkin acceptance criteria.

| Story ID | User Role | User Story Statement | Priority (MoSCoW) | Owner | Target Sprint |
|:---:|:---|:---|:---:|:---:|:---:|
| **US-01** | Staff / Admin | **As a** staff member or admin, **I want to** authenticate with my email and password **so that** I can access the system securely based on my permissions. | **Must Have** | Ahmed | Sprint 2 |
| **US-02** | Admin | **As an** admin, **I want to** enforce role-based access control (RBAC) **so that** staff members cannot access administrative settings, dashboards, or cost reports. | **Must Have** | Ali | Sprint 3 |
| **US-03** | Admin | **As an** admin, **I want to** add new medicines specifying both dosage form and package unit **so that** medicines are accurately categorized and tracked in inventory. | **Must Have** | Abdelrahman | Sprint 3 |
| **US-04** | Admin | **As an** admin, **I want to** update medicine details (price, dosage, min-stock threshold) **so that** catalog information remains accurate. | **Should Have** | Ahmed | Sprint 5 |
| **US-05** | Admin | **As an** admin, **I want to** deactivate/soft-delete discontinued medicines **so that** they cannot be sold while historical invoices remain valid. | **Should Have** | Ali | Sprint 4 |
| **US-06** | Staff | **As a** staff member, **I want to** search medicines by trade name, generic name, or barcode **so that** I can locate products quickly during customer consultations. | **Must Have** | Abdelrahman | Sprint 3 |
| **US-07** | Staff | **As a** staff member, **I want to** scan medicine barcodes directly into the POS cart **so that** items are registered instantly with zero manual typing. | **Must Have** | Ahmed | Sprint 3 |
| **US-08** | Staff | **As a** staff member, **I want** the cart to calculate item totals, taxes, discounts, and net bill automatically **so that** billing errors are eliminated. | **Must Have** | Ali | Sprint 3 |
| **US-09** | Staff | **As a** staff member, **I want to** record patient/customer name and phone number on the sale **so that** prescriptions and hospital invoices are traceable. | **Should Have** | Abdelrahman | Sprint 4 |
| **US-10** | Staff | **As a** staff member, **I want to** finalize a sale, decrement stock atomically, and generate an invoice **so that** the transaction is completed and receipt printed. | **Must Have** | Ahmed | Sprint 4 |
| **US-11** | Staff | **As a** staff member, **I want to** start and end my work shift with a single click **so that** my attendance and active cash drawer are recorded. | **Should Have** | Ali | Sprint 4 |
| **US-12** | Admin | **As an** admin, **I want to** monitor stock levels with color-coded expiry alerts **so that** expired drugs are removed before reaching patients. | **Should Have** | Abdelrahman | Sprint 4 |
| **US-13** | Admin | **As an** admin, **I want to** generate sales and revenue reports filtered by date range **so that** I can analyze pharmacy turnover and profit. | **Should Have** | Ahmed | Sprint 5 |
| **US-14** | Admin | **As an** admin, **I want to** view staff working hours and shift logs **so that** payroll and counter coverage can be audited. | **Should Have** | Ali | Sprint 5 |
| **US-15** | Admin | **As an** admin, **I want to** create, edit, and deactivate staff member accounts **so that** only currently employed pharmacists access the hospital system. | **Should Have** | Ahmed | Sprint 5 |
| **US-16** | Admin | **As an** admin, **I want** an executive dashboard displaying today's revenue, invoice count, and low-stock alerts **so that** I get an instant operational overview. | **Should Have** | Abdelrahman | Sprint 5 |
| **US-17** | Staff | **As a** staff member, **I want to** scan barcodes using a web/tablet camera **so that** I have a working barcode reader if a hardware USB scanner is unavailable. | **Could Have** | Abdelrahman | Sprint 6 |
| **US-18** | Admin | **As an** admin, **I want to** process refunds for returned items and restore stock safely **so that** customer returns are properly accounted for in revenue. | **Could Have** | Ali | Sprint 6 |
| **US-19** | Staff | **As a** staff member, **I want to** generate and print barcode labels on adhesive sticker sheets **so that** unbarcoded medicines can be scanned at the POS. | **Should Have** | Ahmed | Sprint 6 |
| **US-20** | Admin | **As an** admin, **I want** the system to detect connected USB barcode scanners and thermal receipt printers automatically **so that** setup requires zero driver installs. | **Could Have** | Ali | Sprint 7 |
| **US-21** | Admin | **As an** admin, **I want** a standalone Windows installer (`PharmaSys-Setup.exe`) **so that** the software can be installed on any hospital PC with desktop shortcuts. | **Should Have** | Abdelrahman | Sprint 7–8 |
| **US-22** | Staff | **As a** clinical pharmacist, **I want** the POS to display an immediate warning banner when two scanned medications have a known severe drug-to-drug interaction **so that** hazardous dispensing errors are prevented. | **Could Have** | Ali | Sprint 6 |
| **US-23** | Staff | **As a** counter pharmacist, **I want to** click "Find Generic Alternative" on any out-of-stock medicine **so that** I can offer the patient an equivalent available medicine sharing the same active ingredient and dosage. | **Could Have** | Abdelrahman | Sprint 6 |
| **US-24** | Customer / Staff | **As a** patient or cashier, **I want to** send an electronic sales invoice link to the patient's WhatsApp or SMS **so that** patients have a digital receipt for health insurance claims without relying on paper rolls. | **Could Have** | Ahmed | Sprint 7 |
| **US-25** | Admin | **As a** shift supervisor, **I want to** perform cash drawer reconciliation at the end of each shift (expected cash vs actual physical cash counted) **so that** cash surpluses or deficits are audited and logged per cashier. | **Could Have** | Ali | Sprint 7 |
| **US-26** | Admin | **As an** inventory manager, **I want** the system to generate an automated draft purchase order (PO) for medicines falling below their minimum stock thresholds **so that** restocking orders with pharmaceutical distributors can be placed in one click. | **Could Have** | Ahmed | Sprint 7 |
| **US-27** | Staff | **As a** night-shift pharmacist, **I want to** toggle a high-contrast dark theme mode **so that** prolonged screen usage during 24-hour emergency hospital shifts reduces eye strain. | **Could Have** | Abdelrahman | Sprint 6 |

---

## 3. Acceptance Criteria in Gherkin (`Given / When / Then`)

In compliance with Lab 02 requirements, the **Top 5 Core Stories** contain formal Gherkin specifications including both **normal operational scenarios** and **explicit failure / edge-case scenarios**. Additionally, acceptance criteria are provided for the advanced hospital features.

---

### US-01: User Login and Authentication
```gherkin
Feature: User Login and Authentication
  As a staff member or admin
  I want to log in with my credentials
  So that I can access authorized pharmacy operations

  Scenario: Successful login with valid credentials (Normal Flow)
    Given an active user exists with email "pharmacist@pharmasys.app" and password "ValidPass123"
    When the user submits email "pharmacist@pharmasys.app" and password "ValidPass123"
    Then the system returns HTTP 200 OK
    And a signed JWT access token valid for 8 hours is issued
    And the user is redirected to the POS sales invoice screen

  Scenario: Login attempt with invalid password (Failure Scenario)
    Given an active user exists with email "pharmacist@pharmasys.app"
    When the user submits email "pharmacist@pharmasys.app" and password "WrongPassword"
    Then the system rejects the request with HTTP 401 Unauthorized
    And an error message "Invalid email or password" is displayed
    And no access token is issued

  Scenario: Login attempt with deactivated account (Failure Scenario)
    Given a user account with email "former_staff@pharmasys.app" is marked as deactivated
    When the user attempts to log in with correct credentials
    Then the system rejects the request with HTTP 403 Forbidden
    And an error message "Account is deactivated. Contact pharmacy administrator." is displayed
```

---

### US-03: Add Medicine with Dosage Form and Package Unit
```gherkin
Feature: Add Medicines to Inventory
  As a pharmacy admin
  I want to register a medicine with dosage form and package unit
  So that medicine catalog and stock records remain organized

  Scenario: Admin successfully registers a new medicine (Normal Flow)
    Given an authenticated user with role "admin"
    And a medicine with barcode "6221234567890" does not exist in inventory
    When the admin submits:
      | Trade Name       | Panadol Extra Tablets |
      | Generic Name     | Paracetamol + Caffeine |
      | Dosage Form      | Tablet                |
      | Package Unit     | Box (2 Strips)        |
      | Barcode          | 6221234567890         |
      | Selling Price    | 45.00 EGP             |
      | Initial Quantity | 100                   |
      | Expiry Date      | 2028-12-31            |
      | Min Stock Alert  | 10                    |
    Then the system returns HTTP 201 Created
    And the medicine is stored in the database
    And the inventory displays the new medicine as active

  Scenario: Duplicate barcode submission is rejected (Failure Scenario)
    Given a medicine with barcode "6221234567890" already exists in inventory
    When the admin attempts to create another medicine with barcode "6221234567890"
    Then the system rejects the creation with HTTP 409 Conflict
    And an error envelope with code "DUPLICATE_BARCODE" is returned
    And the existing record remains unaltered

  Scenario: Past or expired date submission is rejected (Failure Scenario)
    Given an authenticated user with role "admin"
    When the admin submits a medicine with an expiry date in the past "2024-01-01"
    Then the system rejects the creation with HTTP 422 Unprocessable Entity
    And an error message "Expiry date must be in the future" is returned
```

---

### US-07: Scan Barcodes into POS Cart
```gherkin
Feature: Barcode Scanning into POS Cart
  As a counter cashier
  I want to scan barcodes using a hardware scanner
  So that items are immediately added to the active sales cart

  Scenario: Active in-stock medicine barcode scanned (Normal Flow)
    Given the POS screen is active and the barcode input is auto-focused
    And an in-stock medicine "Cataflam 50mg" with barcode "6229988776655", price 35.00 EGP, and stock 50 exists
    When the cashier scans barcode "6229988776655"
    Then "Cataflam 50mg" is appended to the cart with quantity 1 and line total 35.00 EGP
    And a visual confirmation flash and audio beep are triggered
    And the barcode input is cleared and refocused for the next scan

  Scenario: Scanning the same barcode increments quantity (Normal Flow)
    Given "Cataflam 50mg" is already in the cart with quantity 1
    When the cashier scans barcode "6229988776655" again
    Then the quantity for "Cataflam 50mg" in the cart increments to 2
    And the line total updates to 70.00 EGP

  Scenario: Unrecognized barcode scanned (Failure Scenario)
    Given barcode "9999999999999" does not exist in the medicine catalog
    When the cashier scans barcode "9999999999999"
    Then the system rejects the item addition
    And a red error notification "Medicine not found in catalog" is displayed
    And the cart contents remain unchanged

  Scenario: Expired medicine barcode blocked (Failure Scenario)
    Given a medicine "Amoclan 1g" with barcode "6221122334455" has expiry date "2026-09-01" (expired)
    When the cashier scans barcode "6221122334455"
    Then the system strictly blocks adding the item to the cart
    And a critical alert "BLOCKED: Item is expired (Expiry: 2026-09-01)" is shown
    And an audio warning tone is played

  Scenario: Out-of-stock medicine barcode blocked (Failure Scenario)
    Given a medicine "Augmentin 625mg" with barcode "6225544332211" has quantity 0 in stock
    When the cashier scans barcode "6225544332211"
    Then the item is blocked from entering the cart
    And a warning "BLOCKED: Item is out of stock" is displayed
```

---

### US-08: Calculate Bills and Totals
```gherkin
Feature: Bill and Cart Calculation
  As a cashier
  I want bill totals to compute automatically
  So that customers are billed accurately with zero arithmetic errors

  Scenario: Subtotal and grand total computed from cart lines (Normal Flow)
    Given the cart contains:
      | Item                  | Unit Price | Quantity |
      | Panadol Extra Tablets | 45.00 EGP  | 2        |
      | Otrivin Adult Spray   | 25.00 EGP  | 1        |
    When the cashier reviews the bill summary
    Then the subtotal is calculated as 115.00 EGP
    And the grand total is 115.00 EGP

  Scenario: Admin applies authorized percentage discount (Normal Flow)
    Given an authenticated user with role "admin" is supervising the sale
    And the cart subtotal is 200.00 EGP
    When the admin enters a 10% discount
    Then the discount amount is calculated as 20.00 EGP
    And the net payable total updates to 180.00 EGP

  Scenario: Staff user attempts unauthorized discount (Failure Scenario)
    Given an authenticated user with role "staff"
    When the staff member attempts to edit the discount field
    Then the discount field is disabled / read-only
    And a permission notice "Admin authorization required for discounts" is displayed

  Scenario: Change calculation for cash payment (Normal Flow)
    Given the grand total of the sale is 85.00 EGP
    When the cashier enters cash received "100.00 EGP"
    Then the system displays the required change as "15.00 EGP"
```

---

### US-10: Complete Sale and Generate Invoice
```gherkin
Feature: Complete Sale and Print Invoice
  As a cashier
  I want to finalize sales and print invoices
  So that transactions are completed, inventory decrements, and receipts are delivered

  Scenario: Successful cash sale transaction (Normal Flow)
    Given the cart contains 2 units of "Panadol Extra" (current stock: 50 units)
    And total payable amount is 90.00 EGP
    When the cashier selects payment method "Cash"
    And clicks "Confirm Sale" (Shortcut F2)
    Then a Sale record is created in database with status "PAID"
    And stock for "Panadol Extra" decrements to 48 units atomically
    And a unique invoice number "INV-2026-00042" is generated
    And the printable invoice modal opens automatically

  Scenario: Attempting checkout with an empty cart (Failure Scenario)
    Given the POS cart contains 0 items
    When the cashier attempts to click "Confirm Sale"
    Then checkout is disabled
    And a prompt "Cart is empty. Scan an item first." is displayed

  Scenario: Thermal receipt format printing (Normal Flow)
    Given a sale has been confirmed with invoice number "INV-2026-00042"
    When the cashier sends the print command to an 80mm thermal printer
    Then the system generates a receipt containing:
      | Field            | Expected Value                  |
      | Header           | Damanhour University Hospital   |
      | Invoice #        | INV-2026-00042                  |
      | Cashier Name     | Current logged-in user          |
      | Items Breakdown  | Item, Qty, Unit Price, Line Total|
      | Net Total        | Formatted currency (EGP)        |
      | Barcode          | Scannable invoice barcode       |
```

---

### US-22: Drug-to-Drug Interaction Warning (Could Have)
```gherkin
Feature: Drug-to-Drug Interaction Warning
  As a clinical pharmacist
  I want to be alerted when two interacting drugs are added to the same sale
  So that patient health hazards are prevented before dispensing

  Scenario: Severe drug interaction detected between cart items (Warning Flow)
    Given "Warfarin 5mg" (Anticoagulant) is already in the POS cart
    When the pharmacist scans "Aspirin 100mg" (Antiplatelet)
    Then the system adds the item with a prominent red interaction banner:
      """
      CRITICAL WARNING: High risk of severe bleeding between Warfarin and Aspirin!
      """
    And requires the pharmacist to click "Acknowledge & Proceed" before checkout is enabled

  Scenario: No drug interaction between safe combinations (Normal Flow)
    Given "Panadol Extra" (Paracetamol) is in the POS cart
    When the pharmacist scans "Amoxil 500mg" (Amoxicillin)
    Then no drug interaction warning is triggered
    And checkout proceeds normally
```

---

### US-23: Generic Drug Alternative Suggester (Could Have)
```gherkin
Feature: Generic Drug Alternative Suggester
  As a counter pharmacist
  I want to find generic alternatives for out-of-stock items
  So that patients can receive equivalent therapy without returning to the clinic

  Scenario: Pharmacist locates active in-stock generic alternative (Normal Flow)
    Given the medicine "Voltaren 50mg Tablets" has stock 0
    When the pharmacist clicks "Find Generic Alternative"
    Then the system queries medicines matching active ingredient "Diclofenac Sodium" and dosage "50mg"
    And returns "Cataflam 50mg" (Stock: 25, Price: 35.00 EGP)
    And allows one-click replacement directly into the cart

  Scenario: No in-stock alternatives exist (Failure Scenario)
    Given an out-of-stock specialty medicine with zero generic equivalents in inventory
    When the pharmacist requests alternatives
    Then the system displays "No active generic substitutes currently available in inventory"
```

---

## 4. Measurable Non-Functional Requirements (NFRs)

### 4.1 What is an NFR and Why Does It Matter?
In Software Engineering, requirements are divided into two fundamental categories:
- **Functional Requirements (FR / User Stories):** Specify **what** the system does (the behaviors, actions, workflows, and screens).
- **Non-Functional Requirements (NFRs):** Specify **how well** the system performs (the quality attributes, constraints, performance, security, and operational limits).

> **The Core Rule for Lab 02:** Every NFR must be **Measurable (قابل للقياس)** and **Verifiable (قابل للاختبار)**. Vague statements like *"The system should be fast and secure"* are rejected because a QA engineer cannot write a test case for them. An NFR must define a **metric**, a **numerical threshold**, and a **workload condition**.

---

### 4.2 Measurable NFR Specifications for PharmaSys

| ID | Quality Dimension | Measurable Statement / Numerical Constraint | Verification & Testing Method |
|:---:|:---|:---|:---|
| **NFR-01** | **Performance & Latency** | **1.** USB barcode scan-to-cart latency must be **$\le 500 \text{ ms}$**.<br>**2.** Catalog search across $10,000$ medicine records must return paginated results in **$< 2.0 \text{ seconds}$**.<br>**3.** Thermal receipt print dispatch must initiate in **$< 1.5 \text{ seconds}$** after payment confirmation. | Measured using automated API performance profiling in `pytest-benchmark` and browser devtools network timing under a loaded SQLite/PG catalog. |
| **NFR-02** | **Security & Authentication** | **1.** Passwords must be hashed using `bcrypt` with work factor (cost) **$\ge 12$**.<br>**2.** Auth tokens must use JWT signed with HMAC-SHA256 (`HS256`) with a strict **$8\text{-hour}$ expiry window**.<br>**3.** Role-based guards on `/api/v1/admin/*` must reject non-admins with HTTP 403. Zero plaintext credentials. | Verified via automated security unit tests (`pytest tests/test_auth.py`), JWT token inspection, and attempting unauthorized role requests. |
| **NFR-03** | **Usability & Ergonomics** | **1.** A trained cashier must complete a 3-item sale (scan, pay, print) in **$< 60 \text{ seconds}$**.<br>**2.** Barcode input field must maintain **permanent auto-focus** upon page load and after every scan with zero mouse clicks required.<br>**3.** Visual expiry alerts must display high-contrast color badges: Yellow for $< 90 \text{ days}$, Red for $< 30 \text{ days}$ or expired. | Usability timing trials in a simulated counter setup; automated frontend tests asserting `document.activeElement === barcodeInput`. |
| **NFR-04** | **Availability & Fault Tolerance** | **1.** The SaaS system must maintain **$\ge 99.0\%$ uptime** during 24/7 hospital operating hours.<br>**2.** Desktop application must support **offline checkout mode** with local SQLite storage, auto-syncing when internet returns.<br>**3.** All sale checkouts must run inside an **atomic database transaction** (`COMMIT/ROLLBACK`) ensuring zero partial stock decrements. | Automated chaos testing: simulating abrupt power/network drops during checkout and verifying complete rollback without inventory corruption. |
| **NFR-05** | **Portability & Packaging** | The desktop program must package as a standard single installer (`PharmaSys-Setup.exe`) under **$< 150 \text{ MB}$**, installing to `C:\Program Files\PharmaSys` on Windows 10/11 x64 with **zero external prerequisites** (no pre-installed Python, Node.js, or manual runtime). | Tested on a fresh clean virtual machine (Windows 10 Sandbox) verifying install, launch, POS checkout, and clean uninstallation. |
| **NFR-06** | **Data Integrity & Auditability** | Every inventory mutation must be immutably linked to an authorized `user_id`, a `sale_id`, or an `inventory_adjustment_id`. **Zero orphan inventory adjustments** are permitted. Audit logs must be retained for at least 365 days. | Database foreign key constraints, triggers, and SQL consistency audit tests validating `SUM(sales_items) + current_stock === initial_stock`. |
| **NFR-07** | **Backup & Disaster Recovery** | Database snapshot backups must run automatically every **24 hours**. Recovery Time Objective (**RTO**) must be **$< 15 \text{ minutes}$**, and Recovery Point Objective (**RPO**) must be **$< 1.0 \text{ hour}$** of transactional data loss in case of hardware failure. | Disaster recovery drill: restoring from backup snapshot and asserting data parity against known checkpoint transactions. |

---

## 5. MoSCoW Prioritization & Minimum Viable Product (MVP) Scope

### 5.1 MoSCoW Distribution Summary (27 Stories Total)
- **Must Have (7 Stories):** US-01, US-02, US-03, US-06, US-07, US-08, US-10.
- **Should Have (10 Stories):** US-04, US-05, US-09, US-11, US-12, US-13, US-14, US-15, US-16, US-19, US-21.
- **Could Have (10 Stories):** US-17, US-18, US-20, US-22, US-23, US-24, US-25, US-26, US-27.
- **Won't Have (Deferred to Future Releases):** Direct electronic integration with Egyptian Universal Health Insurance (UHI) servers, robotic automated pill dispenser hardware integration.

### 5.2 Formal MVP Scope Definition (Lab 10 Demo Target)
The **Minimum Viable Product (MVP)** for PharmaSys comprises the essential vertical slice required to execute a live, end-to-end pharmacy checkout transaction during the final demonstration:

$$\text{MVP Scope} = \{\text{US-01, US-02, US-03, US-06, US-07, US-08, US-10}\} \cup \{\text{NFR-02 (bcrypt $\ge 12$)}\}$$

**The Core Demonstration Scenario:**
1. Staff logs in securely (**US-01**, **US-02**).
2. The POS screen appears as default with auto-focused scanner (**US-07**).
3. The cashier searches or scans medicines with dosage form & package verification (**US-03**, **US-06**).
4. System blocks any expired or zero-stock products (**US-07**).
5. The cart computes items, taxes, and grand total (**US-08**).
6. Cashier confirms payment; stock decrements atomically; and an itemized receipt is generated (**US-10**).
