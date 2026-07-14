# Changelog

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and intends to use [Semantic Versioning](https://semver.org/spec/v2.0.0.html) for releases.

## [Unreleased]

### Added

- Automated Python, YAML, shell, Compose, dependency, CodeQL, dependency review, and OpenSSF Scorecard checks.
- Tests for SDK contracts, evaluation utilities, observability instrumentation, configuration security, and import safety.
- Standard contribution, support, security, conduct, citation, and release documentation.

### Changed

- Langfuse examples use the v4 observation, propagation, and query APIs.
- OpenTelemetry examples use current GenAI semantic attributes and low-cardinality span names.
- LiteLLM and PostgreSQL images are pinned by release and digest.
- Proxy scripts apply timeouts, fail on HTTP errors, avoid hard-coded keys, and store generated virtual keys with mode `0600`.
- Provider model IDs and budget limits are operator-supplied values.
