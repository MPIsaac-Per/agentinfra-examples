# Agent infrastructure examples

## Working agreement

Finish the authorized task through verification and integration. Preserve existing edits and unresolved requests across interruptions. Make routine implementation decisions locally; ask only when a missing decision materially changes the outcome. Existing authorization persists across turns.

Use tools available in the current session. Skills provide task guidance; they do not impose unrelated workflows or authorize external actions. Keep runtime model selection in the harness. Commits, pushes, publishing, messages, credential changes, and destructive operations need authorization covering the action. Do not add agent or model attribution.

Run checks appropriate to the change and required repository gates. Broaden or repeat checks for new changes, failures, or unresolved concerns. Report the result, verification, and actual limitations concisely.

## Repository context and verification

Public companion examples are organized by article directory; each directory's README explains its contract. Read `CONTRIBUTING.md` before changing dependencies or adding examples. Keep imports free of network calls and credential requirements. Use synthetic fixtures and fakes; exclude private prompts, traces, provider responses, and customer data.

Code checks: `uv run ruff check .`, `uv run ruff format --check .`, `uv run pytest --cov=. --cov-report=term-missing`, and `shellcheck litellm-proxy-setup/*.sh`. Dependency changes also need `uv run pip-audit`. Documentation edits need reference and command checks. Do not start hosted examples or spend provider credits for routine verification.
