# Contributing to ru-gost-crypto-lab

## Code Review Process

We use **Codex Code Review** to ensure quality and security.

1.  **Enable Code Review**: Ensure Codex Code Review is enabled for this repository.
2.  **Trigger Review**:
    *   Add a comment `@codex review` in your PR.
    *   Or `@codex review for security regressions` for specific checks.
3.  **Requirements**:
    *   All PRs MUST pass `scripts/lint.sh`.
    *   All PRs MUST pass `scripts/dev_run_all_tests.sh`.
    *   All PRs MUST pass `scripts/security_scan.sh`.
    *   All PRs MUST have a Codex Code Review run.

## Development Flow

1.  **TDD**: Write tests first. Ensure they fail. Then implement.
2.  **Security**: Do not commit real keys or proprietary binaries.
3.  **Style**: Follow PEP 8 for Python. Use the provided linters.
