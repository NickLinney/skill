# NickLinneyDev - DevOps Pipeline Branch Strategy

**Document ID:** STD-NLD-DEVOPS-001  
**Organization:** NickLinneyDev  
**Status:** Active  
**Version:** 0.1.0-alpha  
**Document Class:** Standards Document  
**Authoritative Context:** NickLinneyDev Standards Library  
**Date:** 2026-07-29  
**Audience:** NickLinneyDev-managed projects, products, repositories, and reusable operational practices

---

## 1. Purpose

This document defines the **branching, promotion, validation, and release movement strategy** used for software delivery pipelines governed by **NickLinneyDev**.

Its purpose is to:

- Establish a clear operational branching model
- Reduce ambiguity around promotion between environments
- Preserve release discipline
- Support deliberate validation gates
- Prevent accidental release-path contamination
- Keep operational authority legible across repositories

This document is a **NickLinneyDev standards artifact**.

It may be:

- Adopted directly by NickLinneyDev-managed repositories
- Referenced by external projects
- Reused by unrelated parties
- Incorporated selectively into other governance systems

It is **not** defined as an artifact of:

- Any other downstream implementation context

Those systems may consume this document, but they do not define its authority.

---

## 2. Scope

This standard applies to repositories and delivery pipelines where NickLinneyDev chooses to impose:

- Structured branch promotion
- Explicit test gating
- Release branch discipline
- Controlled movement into production authority

This standard may be used for:

- Personal software products
- Client-facing applications
- Experimental but governed projects
- Open source repositories
- Internal tooling

This standard does **not** require every repository to use every branch named here.

However, where this standard is adopted, the promotion logic and authority model should remain intact.

---

## 3. Foundational Principles

### 3.1 Promotion Must Be Deliberate

Code should move upward through an intentional chain of validation states.

Branches are not merely copies of code.

They represent:

- Levels of trust
- Validation status
- Operational intent
- Release authority

---

### 3.2 Release Authority Must Be Protected

The branch representing released or release-authoritative code must not serve as a general work surface.

This prevents:

- Accidental production drift
- Unreviewed release inclusion
- Loss of narrative clarity
- Weak release traceability

---

### 3.3 Validation Environments Are Real Governance Boundaries

The test branch is not a convenience branch.

It is a formal validation boundary where feature work is assembled and evaluated before promotion into a more trusted integration baseline.

---

### 3.4 Release Branches Are Feature Aggregation Vehicles

An active release branch may function as the **feature set vehicle** for a planned body of work.

Feature branches may merge upward into the release branch directly or into intermediary validation branches depending on repository needs.

The release branch exists to preserve:

- Scope clarity
- Release identity
- Controlled composition
- Promotion discipline

---

### 3.5 Branch Meaning Must Remain Stable

Branch names should communicate operational meaning, not convenience.

The value of the branching system depends on the stability of what each branch *means*.

---

## 4. Canonical Branch Roles

### 4.1 `main`

`main` is the **production-authoritative branch**.

It should contain only code that is considered formally released or release-approved.

Characteristics:

- Stable
- Protected
- Release-only
- Taggable
- Suitable for historical reference

Direct feature development on `main` is prohibited.

---

### 4.2 `dev`

`dev` is the **confirmed integration baseline**.

It represents work that has passed lower-level validation and has been confirmed suitable for broader integration confidence.

Characteristics:

- More permissive than `main`
- Still curated
- Not automatically releasable
- Used to accumulate validated work

Promotion into `dev` should require explicit confirmation that the relevant features are working as intended.

---

### 4.3 `test`

`test` is the **validation proving ground**.

It is a formal shared testing surface branching from `dev`.

Characteristics:

- Higher churn than `dev`
- Lower trust than `dev`
- Intended for validation rather than permanence
- Rebuildable from a healthier upstream if needed

If the branch becomes unstable, it may be reset or rebased from `dev` in accordance with repository needs and operator intent.

`test` is intended for **department-level testing coordination**, not for every intermediate working state of every feature.

It may be refreshed from `dev` and used as a coordinated testing surface without requiring every feature to merge into it as part of the primary promotion path.

---

### 4.4 `staging`

`staging` is the **user acceptance testing branch** when internal customer validation or broader acceptance testing is required.

It should branch from `main`.

Characteristics:

- Non-contributory
- Refreshable from `main`
- Suitable for internal customer or user acceptance testing
- Lower authority than `main`
- Not a source branch for promotion into `main`

Release branches may be merged into `staging` for acceptance testing.

`staging` should be refreshed from `main` from time to time, especially before new release merges, to preserve clarity and reduce drift.

`staging` must not be treated as a permanent integration lineage that contributes forward into `main`.

---

### 4.5 Release Branches

Release branches such as `pre-alpha-1`, `alpha-1`, `beta-2`, or similar are **named release-scope containers**.

They exist to:

- Delimit release scope
- Preserve release composition
- Act as controlled promotion sources
- Support release-specific validation and documentation

An active release branch may also serve as the primary **feature aggregation vehicle** where the repository intentionally groups a coherent body of work before broader promotion.

Completed release branches should generally be preserved for traceability.

In this model, release branches branch from `main` and act as the direct promotion source for:

- `dev`
- `staging`
- `main`

---

### 4.6 Top-Level Feature Branches

Top-level feature branches are **bounded implementation surfaces** that represent a meaningful body of coordinated work.

Canonical pattern:

```text
feature/<short-name>
```

Examples:

- `feature/release-bootstrap`
- `feature/crud-forms`
- `feature/knowledge-article-editor`
- `feature/canvas-updates-for-granite`

Characteristics:

- Scoped but potentially multi-part
- May act as a parent feature vehicle
- Merged upward into a defined target branch
- Often preserved at least until the associated release is merged and tagged

Top-level feature branches may be used when a **feature set** emerges during development and multiple meaningful sub-features need to be coordinated without cluttering shared validation surfaces.

In this model, top-level feature branches branch from `main` and merge upward into a release branch.

Example:

- `feature/canvas-updates-for-granite`

That top-level feature might contain subordinate work such as:

- redraw logic improvements after object movement
- drag-and-drop support for canvas interaction

This pattern is intentionally allowed.

---

### 4.7 Sub-Feature Branches

Sub-feature branches are **temporary branches created beneath a top-level feature vehicle**.

They exist to isolate narrowly scoped implementation tasks while preserving a coherent parent feature surface.

Examples:

- `feature/canvas-redraw-on-move`
- `feature/canvas-drag-interaction`

Characteristics:

- Very narrow in scope
- Temporary by default
- Branch from `main` in this model
- Merged into the parent feature branch rather than directly into release or shared validation branches
- Eligible for deletion after merge and confirmation of completion

Sub-feature branches help prevent `test` from becoming cluttered by incomplete or unrelated intermediate changes.

---

### 4.8 Personal Development Branches

A developer may branch from `dev` to create a **personal development branch** when isolation from other active work is useful.

These branches are not a replacement for release or department-level validation branches.

They are private or team-local working surfaces intended to reduce cross-feature contamination during active implementation.

They should not change the authority model of:

- `test`
- `dev`
- release branches
- `main`

---

### 4.9 Relationship Summary

The intended conceptual distinction is:

- sub-feature branches feed a parent top-level feature branch
- top-level feature branches feed release branches
- release branches preserve scoped release composition and promote outward
- `test`, `dev`, and `staging` are environment-governance surfaces, not arbitrary working copies

---

## 5. Canonical Promotion Flow

The default NickLinneyDev promotion sequence is:

```text
sub-feature  ->  top-level feature  ->  release branch  ->  dev
                                              |            |
                                              |            -> test (branch surface)
                                              -> staging
                                              -> main (release tag)
```

Where a release branch is also acting as the active feature set vehicle, work may first accumulate there before broader promotion logic is applied.

An example repository-specific pattern may be:

```text
feature/canvas-redraw-on-move  ->  feature/canvas-updates-for-granite  ->  pre-alpha-1
feature/canvas-drag-interaction ->  feature/canvas-updates-for-granite  ->  pre-alpha-1
pre-alpha-1 -> dev
pre-alpha-1 -> staging
pre-alpha-1 -> main
```

This is acceptable if:

- The release feature vehicle is intentional
- The merge path is documented
- Promotion authority remains explicit

---

## 6. Standard Operating Rules

### 6.1 No Direct Promotion to `main` Outside Release Events

`main` should only receive changes as part of an explicit release event.

That release event should include:

- Final validation confirmation
- Version confirmation
- Changelog or release note update
- Tag creation

---

### 6.2 `dev` Requires Human Confirmation

Feature work should not merge into `dev` merely because tests pass.

Promotion into `dev` should occur only after explicit confirmation that the feature behaves correctly in the relevant test context.

Automated validation informs the decision.

It does not fully replace operator judgment.

---

### 6.3 Feature Vehicles Should Merge into Release Branches

Top-level feature branches should generally merge into release branches.

This provides:

- A scoped release composition surface
- Clear separation between implementation grouping and broader validation branches
- A controlled path for promotion outward from release intent

Sub-feature branches should generally merge into their parent feature vehicle before release unless there is a strong reason to promote them differently.

---

### 6.4 `dev` Receives Promotion from Release Branches

`dev` branches from `main`, but in this model it receives validated release-scope work from release branches.

- `dev` remains a confirmed integration baseline
- release branches may merge into `dev`
- personal development and department testing surfaces may then branch from `dev`

This model allows `dev` to absorb intended release work while remaining a separately refreshable authority surface.

---

### 6.5 `staging` Is Non-Contributory

`staging` should not be merged into `main` at any point.

Instead:

- `staging` branches from `main`
- `staging` may be refreshed from `main`
- release branches may be merged into `staging` for acceptance testing
- `main` receives release branches directly during actual release events

This keeps staging useful for user acceptance testing without making it a historical source of release authority.

---

### 6.6 Release Branches Must Not Become Ambiguous

If a release branch exists, its scope should be understandable.

It should be possible to answer:

- What work belongs to this release?
- What has been validated?
- What remains open?
- What is excluded?

If these questions cannot be answered, release discipline is degrading.

---

### 6.7 Branch Retention Should Reflect Role

Branch retention should be guided by the branch's role in the delivery narrative.

Recommended default:

- preserve release branches
- preserve top-level feature branches at least until the associated release is merged and tagged
- allow sub-feature branches to be deleted after merge and confirmation of completion
- allow disposable personal development branches to be pruned when no longer useful

Implementors may choose to keep top-level feature branches longer when the added traceability is valuable.

---

### 6.8 `dev` Branches for Individual Developers Are Allowed

Repositories or teams may allow developers to create personal branches from `dev` for isolated implementation work.

This is especially useful when multiple contributors need freedom from unrelated feature changes contaminating their own working state.

These branches do not replace:

- feature vehicles
- `test`
- `staging`
- release branches

They are a practical isolation tool, not a governance tier.

---

### 6.9 Completed Feature Branches Should Generally Be Preserved

Where branch history contributes to traceability, completed **top-level feature branches** should generally be preserved at least through the associated release event.

If a repository uses disposable sub-feature or support branches beneath a feature vehicle, those subordinate branches may be deleted after merge and confirmation of completion.

The preservation choice should support clarity rather than clutter, and repository implementors may decide whether to retain top-level feature branches beyond the release lifecycle.

---

## 7. Branch Authority Model

Each branch corresponds to a different level of authority:

| Branch Type           | Primary Meaning                  | Trust Level | Deletion Expectation            |
| --------------------- | -------------------------------- | ----------- | ------------------------------- |
| Sub-feature           | Narrow implementation task       | Low         | Usually temporary               |
| Top-level feature     | Coordinated feature vehicle      | Low-medium  | Encourage preservation          |
| `test`                | Department testing surface       | Medium-low  | Rebuildable                     |
| `dev`                 | Confirmed integration baseline   | Medium      | Persistent                      |
| `staging`             | UAT surface from `main`          | Medium      | Refreshable                     |
| Release branch        | Scoped release authority         | Medium-high | Preserve                        |
| `main`                | Production/release authority     | High        | Preserve                        |

This hierarchy should remain conceptually stable even if repository-specific names vary.

---

## 8. Review and Approval Expectations

Promotion between governance boundaries should be accompanied by review notes.

Review records should identify:

- Scope
- Findings
- Risks
- Approval status

At minimum, branch promotions into release branches, `dev`, `staging`, or `main` should not occur silently.

This standard favors **legible approvals** over informal memory.

---

## 9. Rebuild and Recovery Strategy for `test`

`test` is intentionally recoverable.

If the test branch becomes noisy, polluted, or unreliable, it may be:

- Reset from `dev`
- Rebased from `dev`
- Reconstructed through fresh merge sequencing

This is not treated as a failure of the branching model.

It is an intentional resilience feature of the model.

The purpose is to ensure that the testing surface can be restored to a known-good baseline without corrupting higher-authority branches.

---

## 10. Staging Refresh Strategy

`staging` should be treated similarly to `test` in one important respect:

it is refreshable from its parent.

Recommended pattern:

1. Refresh `staging` from `main`
2. Merge an intended release branch into `staging`
3. Conduct user acceptance testing
4. If accepted, merge the release branch into `main`
5. Refresh `staging` again when appropriate for the next cycle

This keeps staging legible and prevents it from becoming a long-lived contributory branch with mixed authority.

---

## 11. Release Event Requirements

A release event should normally include:

1. Confirmation that release scope is complete
2. Confirmation that the promoted branch is functioning as intended
3. Update of version artifacts
4. Update of release notes or changelog
5. Merge into `main`
6. Creation of a release tag

Optional additions may include:

- Artifact signing
- Container publication
- Deployment notes
- Rollback references

---

## 12. Repository-Level Adaptation

Repositories may adapt this strategy to fit their operating realities.

Allowed adaptations may include:

- Using a release branch as the active feature aggregation vehicle
- Introducing sub-feature branches beneath a primary feature branch
- Allowing personal development branches from `dev`
- Omitting release branches for very small repositories
- Adding environment-specific branches where justified

However, adaptations should not erase:

- Promotion order
- Authority clarity
- Release discipline
- Validation boundaries

---

## 13. Non-Goals

This standard does **not** define:

- CI vendor implementation details
- Specific test automation frameworks
- GitHub-specific branch protection settings
- Semantic version policy in full
- Deployment platform mechanics

Those are governed by separate operational or repository-level documents.

---

## 14. Historical Notes

Earlier NickLinneyDev Git hygiene practices emphasized:

- preserving history as narrative
- treating releases as first-class artifacts
- maintaining a readable `main`
- avoiding premature squashing

Those ideas remain directionally aligned with this standard and continue to inform it where not contradictory.

However, this document is now the canonical articulation for:

- branch authority
- release-feature vehicle patterns
- `test` and `dev` roles
- non-contributory `staging`
- sub-feature branch disposal expectations

---

## 15. Closing Statement

This strategy exists to preserve **clarity, control, and recoverability** in software delivery.

Its goal is not procedural heaviness for its own sake.

Its goal is to ensure that code movement reflects intentional judgment, stable authority, and understandable release composition.

Where adopted, this standard should help repositories answer a simple but important question:

> *What exactly is trusted here, and why?*
