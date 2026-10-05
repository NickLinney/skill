# NickLinneyDev - Organizational Git Procedures and Practices

**Document ID:** STD-NLD-GIT-001  
**Organization:** NickLinneyDev  
**Prepared By:** PM  
**Document Class:** Standards Document  
**Status:** Active  
**Version:** 0.1.0-alpha  
**Date:** Thursday, July 30, 2026  
**Audience:** Project Managers, developers, release managers, technical leads, and agentic workers

## 1. Purpose

This document defines the required Git operating practices for NickLinneyDev software projects.

Its purpose is to ensure that source control functions as:

- a development tool
- a release-control mechanism
- an auditable evidence system

## 2. Core Principle

At NickLinneyDev, the remote repository is not merely a synchronization target.

It is part of the project record.

Local-only work may be useful during implementation, but it is not sufficient as the final evidentiary form of completed work.

## 3. Repository Placement

- The code repository should exist as a subdirectory of the broader local project workspace.
- Enterprise knowledge, planning artifacts, and other non-code records may live outside the repository when separation of concerns requires it.
- Sensitive key material should not be placed inside the repository unless the project explicitly requires a safe and governed mechanism for doing so.

## 4. Minimum Branch Model

Unless a project is explicitly governed otherwise, the minimum branch topology should include:

- `main`
- `dev`
- `test`
- `staging`
- one or more feature or release-preparation branches as needed

Additional branches may be used when required by the product, release, or testing strategy.

## 5. Meaning of `main`

`main` should represent the latest good officially released state.

At NickLinneyDev:

- `main` is not the default scratch space for active development unless the project explicitly adopts that model
- `main` should be updated through official release movement
- if a project uses a different model, that exception must be declared during kickoff

## 6. Meaning of Release Branches

Release branches, milestone branches, and release-preparation branches may exist as historical and governance artifacts.

Their existence does not replace the requirement that the official released state be reflected on `main` unless the project has explicitly adopted another release model.

## 7. Commit and Push Discipline

- Dev work must be committed at meaningful completed task boundaries.
- Completed task-boundary commits must be pushed to the remote repository promptly.
- Whole features, major phases, or release milestones should not remain local-only.
- The PM and Release Manager should treat extended local-only drift as a process defect.

## 8. Review Requirement for Merges

Every merge should be reviewed by another qualified role in the following order of preference:

1. another Dev
2. Release Manager
3. PM

If the preferred reviewer is unavailable, the next valid reviewer in the order may perform the gate.

The reviewer should evaluate:

- correctness
- release readiness
- configuration integrity
- documentation truthfulness
- evidence sufficiency

## 9. Release Completion Rule

A release is not complete merely because a release branch exists or a branch-specific tag exists.

Unless a project explicitly states otherwise, official release completion requires:

1. reviewed release branch or release candidate readiness
2. formal promotion through the required branch path
3. merge of the official release state into `main`
4. release tag created on the authoritative released commit
5. remote repository updated to reflect that final state

## 10. Tagging Practice

- Release tags should use the organization’s agreed naming convention.
- Tags should be created on the authoritative released commit.
- Mistaken tags should be corrected promptly and transparently.
- A project should avoid ambiguous or duplicate release tags that point to different states.

## 11. Remote Authenticity Rule

The remote repository should tell the truth about the project state.

That means:

- work should not appear complete locally while remaining absent remotely for too long
- review artifacts and release evidence should be preserved where appropriate
- branch and tag state should match the real release story

## 12. Governance Exceptions

If a project needs to deviate from this standard, the deviation should be documented explicitly at project start or at the moment of governance change.

Examples include:

- trunk-based development
- protected release branches that do not merge back into `main`
- monorepo-specific flow variations
- regulated environments with alternate evidence systems

## 13. PM Operating Expectations

The PM should confirm during kickoff:

- branch topology
- meaning of `main`
- release-path completion rules
- tag naming convention
- review expectations
- commit/push cadence expectations
- whether governance artifacts live inside or outside the repository

## 14. Agentic Workforce Expectations

Agentic workers should not assume industry-default Git behavior is sufficient.

They should confirm and then follow:

- branch semantics
- review order
- release completion semantics
- evidence expectations

When corrected by the sponsor or governing authority, the updated Git practice should be treated as immediately binding.

## 15. Closing Rule

Git at NickLinneyDev is both an engineering mechanism and an institutional memory system.

The organization should therefore optimize not only for code movement, but also for truthful, reviewable, and auditable release history.
