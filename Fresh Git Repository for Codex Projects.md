# Fresh Git Repository for Codex Projects

This document defines a practical baseline for how a **fresh Git repository** should be initialized when a project is being created or bootstrapped through **Codex** under NickLinneyDev-style governance.

It captures the conventions that should be present at the beginning of a governed project so that release discipline, branch authority, and remote hygiene are not retrofitted late.

This is a baseline document.

Projects may adapt it, but deviations should be intentional.

---

## Purpose

The purpose of this document is to ensure that a new Codex-managed repository starts with:

- clear remote ownership
- predictable Git authentication
- explicit branch topology
- release-aware naming and promotion surfaces
- clean initial history
- container-friendly development assumptions where applicable

This helps prevent a repository from beginning as an unstructured scratch space and then requiring governance repair later.

---

## 1. Remote Repository Expectations

Before substantial work begins, the project should have an intended remote repository destination.

That includes:

- repository name
- repository owner or organization
- authentication method
- expected default branch

If the remote already exists, Codex should treat that as the authoritative destination.

If the remote does not yet exist, Codex should avoid inventing ownership or publishing assumptions.

---

## 2. Preferred Authentication Model

For Codex-managed Git repositories, a **dedicated deploy key or dedicated repository SSH key** is the preferred baseline when the project owner provides one.

This is favored because it:

- isolates repository access from personal shell defaults
- makes intent explicit
- reduces ambiguity about which identity is pushing
- supports cleaner operational separation

Codex should prefer using:

```text
GIT_SSH_COMMAND='ssh -i /path/to/key -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new'
```

for remote push operations when a dedicated key is available.

Codex should not assume the user wants to rely on ambient SSH agent state if a project-specific key exists.

---

## 3. Local Git Initialization

When starting a brand-new repository, the recommended baseline is:

1. initialize Git explicitly
2. establish the default branch as `main`
3. set repository-local author identity if appropriate
4. stage the intended bootstrap files only
5. create a clean initial commit

The initial commit should represent a coherent repository starting state, not an accidental mix of half-finished exploration and missing governance files.

---

## 4. Initial Commit Expectations

The first commit should ideally include:

- repository structure
- baseline documentation
- ignore files
- Docker or runtime scaffolding, if already in scope
- branch and release governance where known
- project metadata such as version or changelog files where applicable

The initial commit should be understandable as a starting artifact in its own right.

Recommended style:

- one coherent initial commit
- concise but meaningful commit message

Example:

```text
feat: initial commit
```

---

## 5. Branch Topology Should Be Established Early

If the project already has a defined branch strategy, the primary branch topology should be created immediately after the initial commit rather than delayed.

That may include:

- `main`
- `dev`
- `test`
- one or more release branches
- an initial top-level feature vehicle

This helps avoid a situation where meaningful work starts on the wrong branch and must be reorganized later.

---

## 6. Release and Feature Surfaces

If the project is operating in a pre-alpha or governed early-development mode, Codex should treat branch identity and release identity as separate concerns.

Examples:

- branch: `pre-alpha-1`
- tag: `0.0.0-pre-alpha.1`

This allows the repository to maintain human-meaningful work surfaces without forcing SemVer identifiers into every branch name.

If a top-level feature vehicle is part of the working model, it should be created deliberately and named according to the actual planned feature set, release objective, or architectural workstream.

Examples:

- `feature/canvas-updates-for-granite`
- `feature/identity-service-foundation`
- `feature/reporting-workbench`

The important rule is not the specific wording pattern.

The important rule is that the branch name should communicate a coherent implementation surface that is meaningful in the context of the project.

Sub-feature branches may then merge upward into that feature vehicle before promotion into broader validation or release surfaces.

---

## 7. Push Order to the Remote

Once the local repository is initialized cleanly, the preferred push sequence is:

1. push `main`
2. push the foundational supporting branches
3. push the active feature vehicle branch

This preserves a readable remote history of repository establishment.

For example:

1. `main`
2. `dev`
3. `test`
4. `pre-alpha-1`
5. `feature/release-bootstrap`

This sequence helps the remote repository reflect the intended authority model from the outset.

---

## 8. Branch Tracking

After pushing, Codex should ensure the major working branches track their upstream counterparts.

That includes:

- `main`
- `dev`
- `test`
- active release branches
- active top-level feature branches

This makes subsequent repository operations less error-prone and keeps branch intent visible.

---

## 9. Docker-First Projects

If the project is intended to be developed with Docker-first isolation, repository bootstrap should reflect that immediately.

That may include:

- `.dockerignore`
- `docker-compose.yml`
- schema-only and sample-data database startup paths
- avoiding host-side dependency installation

If Codex discovers this preference early, it should use that mode from the start rather than introducing host-side package artifacts and cleaning them up afterward.

---

## 10. Sample Data and Clean Launch Support

If the repository includes a database-backed application, the fresh repository baseline should ideally support:

- clean schema-only launch
- populated sample-data launch

These should be defined in the repository itself rather than depending on undocumented manual seeding steps.

This makes the repository easier to:

- validate
- demo
- reset
- onboard into

---

## 11. Governance Documents Should Not Arrive Late

If the project already has known standards around:

- branching
- versioning
- releasing
- backup or restore
- repository structure

those documents should be added as early as practical.

A fresh repository should not wait until later phases to become legible if the operating model is already known.

---

## 12. Review and Release Readiness Mindset

Even in a new repository, Codex should work as though future release traceability matters.

That means:

- commits should be intentional
- branch roles should be explicit
- releases should be planned rather than improvised
- `main` should stay clean

Starting with these expectations costs little and prevents avoidable rework later.

---

## 13. Recommended Fresh-Repo Sequence

For a fresh Codex project with full standards context already available, the recommended sequence is:

1. inspect the workspace
2. confirm remote repository target
3. confirm whether a dedicated SSH deploy key is available
4. initialize Git on `main`
5. add repository-local Git identity if appropriate
6. establish repo scaffolding and governance files
7. make the initial commit
8. create branch topology
9. add remote
10. push `main`
11. push supporting branches
12. push the active feature vehicle branch
13. continue work from the agreed feature vehicle branch

This sequence results in a repository that starts life in a governed state rather than being repaired into one later.

---

## 14. Closing Note

Fresh repositories tend to become long-lived repositories faster than expected.

Because of that, Git bootstrap should be treated as part of system design rather than a trivial prelude.

When Codex has adequate standards context at the start, the repository should begin with:

- clear authority
- clean branch meaning
- explicit remote access
- reproducible launch assumptions
- release-aware structure

That is the baseline this document encourages.

