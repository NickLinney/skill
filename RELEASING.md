# RELEASING.md
## Release Process Checklist

This document defines the **authoritative checklist** for preparing, validating, tagging, and publishing a new release of The System.

Every release — pre-alpha, alpha, beta, RC, or stable — must follow this process.

---

## 0. Preconditions

Before starting a release:

- All intended work for the release is complete
- All related Issues are closed or explicitly deferred
- The working tree is clean
- CI (if present) is passing
- The release scope is clearly defined

---

## 1. Version Planning

- [ ] Confirm the **target version** (e.g. `0.0.0-pre-alpha.11`, `0.1.0-alpha`)
- [ ] Confirm lifecycle phase (Pre-Alpha / Alpha / Beta / RC / Stable)
- [ ] Confirm compatibility expectations for this release
- [ ] Confirm whether this is:
  - Feature snapshot
  - Bugfix release
  - Architecture milestone

---

## 2. Documentation Updates (Required)

### Core Project Documents

These **must** be reviewed and updated as applicable:

- [ ] `VERSION.md`
  - Replace entirely with release-specific content
  - Describe what is unique to this version
- [ ] `CHANGELOG.md`
  - Add a new entry at the top
  - Accurately list all changes in this release
- [ ] `README.md`
  - Verify version string
  - Update status notes if lifecycle phase changed

### Architecture & Process Docs

Review for accuracy; update only if changes occurred:

- [ ] `ARCHITECTURE.md`
- [ ] `CONTRIBUTING.md`
- [ ] `VERSIONING.md`
- [ ] `ABSTRACT.md`

> These documents should only change when the underlying rules or philosophy change.

---

## 3. Git Branch Preparation

### Pre-Alpha Releases

- [ ] Ensure work is on `pre-alpha/N` branch
- [ ] Ensure branch represents a **feature-complete snapshot**
- [ ] Merge `pre-alpha/N` → `main` (fast-forward preferred)
- [ ] Delete branch after merge (optional)

### Alpha and Later Releases

- [ ] Create or update `release/x.y.z` branch
- [ ] Freeze feature work
- [ ] Allow only fixes and documentation changes

---

## 8. Commit Hygiene

- [ ] Ensure commits are logically grouped
- [ ] Ensure commit messages follow project conventions
- [ ] Avoid mixing unrelated changes
- [ ] Squash commits if necessary for clarity

---

## 9. Tagging

- [ ] Create an **annotated Git tag** matching the version exactly
- [ ] Tag must point to the merge commit on the correct branch
- [ ] Tags are immutable once created

Examples:

```bash
git tag -a 0.0.0-pre-alpha.10 -m "Pre-Alpha 10: architecture-stabilized snapshot"
git push --tags
```

------

## 10. Release Publication (Optional but Recommended)

If using a platform with releases (GitHub/GitLab/Gitea):

-  Publish a release from the tag
-  Copy summary from `VERSION.md`
-  Link to `CHANGELOG.md`
-  Clearly mark pre-release status if applicable

------

## 11. Post-Release Cleanup

-  Close remaining Issues tied to the release
-  Update milestone status (if used)
-  Verify documentation links remain correct
-  Prepare next development branch if applicable

------

## 12. Final Verification

Before declaring the release complete:

-  Repository builds cleanly
-  Documentation accurately reflects reality
-  Version identifiers are consistent everywhere
-  No uncommitted changes remain

------

## Release Invariant

A release must be:

- Internally consistent
- Architecturally compliant
- Accurately documented
- Reproducible from the tagged commit

If any of these conditions are not met, **do not release**.

------

## Closing Note

Releases are **communication artifacts**, not just code snapshots.

This checklist exists to ensure that every release:

- Can be trusted
- Can be understood
- Can be built upon

Follow it exactly.