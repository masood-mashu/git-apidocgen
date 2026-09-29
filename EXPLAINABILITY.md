# Explainability, Auditability & Decision Logic: GitApiDocGen

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitApiDocGen**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitApiDocGen** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Web**: Web framework source code (FastAPI, Express.js, Spring Boot, Gin).
- **OpenAPI**: OpenAPI Specification version 3.1.0 specification standards.
- **Authentication**: Authentication security scheme definitions (Bearer JWT, OAuth2, APIKey).
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **synthesize_openapi_spec**: Uses `openapi-spec-synthesizer` to calculate generates valid openapi 3.1.0 schema document from list of endpoints and methods.
   - **check_status_code_coverage**: Uses `status-code-coverage-checker` to calculate verifies that endpoint operations define documentation for standard client/server errors.
   - **generate_curl_example**: Uses `curl-example-generator` to calculate generates copy-paste executable curl command line string with headers and dummy body.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When an API repository is analyzed, the agent runs openapi_spec_synthesizer, status_code_coverage_checker, and curl_example_generator. If all routes are documented and schemas validate, it issues APPROVED. If undocumented 4xx/5xx responses exist, it issues NEEDS_REVIEW. If invalid path parameters or duplicate operation IDs are discovered, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on AST code parsing.
- **Does**: Does not execute live network traffic against target production APIs during doc generation.
- **Supports**: Supports REST and JSON-RPC APIs (GraphQL schemas require separate SDL generators).
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
