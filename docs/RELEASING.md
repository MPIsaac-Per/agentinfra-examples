# Releasing

1. Confirm `main` is green and the dependency audit has no unresolved findings.
2. Re-run import, SDK contract, Compose, and shell checks against the pinned versions.
3. Verify each container digest still resolves to the documented release.
4. Move relevant entries from `Unreleased` in `CHANGELOG.md` into a dated version section.
5. Update `project.version` in `pyproject.toml` and `version` in `CITATION.cff`.
6. Open and merge a release pull request.
7. Create a signed tag in the form `vMAJOR.MINOR.PATCH` from the merge commit.
8. Create a GitHub release from the tag and copy the matching changelog section into the release notes.
9. Verify the release page, source archive, and workflow results.

The repository does not publish a package artifact. Releases identify tested example snapshots.
