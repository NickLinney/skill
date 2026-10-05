# Skill Abstract Object Contract

## Inputs

A consumer supplies or resolves a Skill identity, version, capability-bearing Object, Execution Model, mode, input/context expectations, output/effect expectations, contract, authority context, dependencies, provenance, and applicable validation evidence.

## Outputs

The consumer receives an inspectable Skill description and a qualified conformance state. A package validator may return structural, parse, schema, integrity, or declared semantic results only for the scope it actually tests.

## Invariants

1. The capability-bearing Object and Execution Model are both present and semantically distinguishable.
2. Contract inspection precedes consequential execution or side effects.
3. Identity and version are consistent across semantic records and package envelope.
4. Dependencies and composition do not inherit authority or permissions.
5. Artifact, validation record, execution event, authorization, lifecycle transition, and release evidence remain distinct.
6. A missing, stale, contradictory, or non-inspectable contract yields abstention or qualified failure.

## Authority and side effects

This contract grants no authority. A Skill implementation must declare side-effect class and required permissions where applicable. Consequential execution requires external authorization and runtime evidence.

## Failure, abstention, escalation, termination

Fail on missing universal semantics, inconsistent identity, absent/non-inspectable contract, or invalid package integrity. Abstain when evidence is insufficient. Escalate when a required authority or independent review is outside the mandate. Terminate when output obligations are met, a qualified terminal state is reached, or the smallest affected transition is blocked.
