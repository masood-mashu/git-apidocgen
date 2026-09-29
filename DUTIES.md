# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitApiDocGen** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitApiDocGen Automation Engine`
* **Responsibilities**:
  * Inspects route decorators, synthesizes OpenAPI YAML definitions, and generates test cURL commands.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitApiDocGen Verification & Policy Enforcer`
* **Responsibilities**:
  * Validates schema types against JSON Schema Draft 2020-12 standards.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `API Architect / Developer Experience Lead (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
