# Skill Abstract Object Specification

## Purpose

`Skill` is a technology-independent capability-bearing Object plus an associated Execution Model that describes how a consumer may interpret, consume, or execute that capability within an inspectable contract and authority boundary. This package specifies the type, not a runnable Skill.

## Minimum semantic model

Every conforming Skill has stable identity and version, capability intent, one primary capability-bearing Object, one associated Execution Model, an extensible execution/consumption mode, inspectable input/context and output/effect expectations, an inspectable contract, authority and side-effect boundaries, termination and failure behavior, typed dependencies, provenance, proportional integrity, qualified validation, lifecycle state, unresolved conditions, and explicit nonclaims.

The primary Object and Execution Model are semantically distinct even when represented in one file. Composition does not create inheritance, authority, or dependency ownership.

## Execution modes

`data` is passive and has no execution claim. `interpreted` and `declarative` require a consumer interpretation boundary. `runnable` requires an entrypoint, runtime requirements, permission boundary, side-effect classification, termination conditions, and behavior evidence appropriate to the claim. `hybrid` combines modes and inherits the strongest applicable obligations.

## Required versus conditional

Identity, purpose, capability Object, Execution Model, mode, expectations, contract, boundaries, provenance, lifecycle, unresolved state, and nonclaims are universal semantic obligations. Runtime entrypoints, schemas, permissions, integrity signatures, execution logs, and independent review are conditional on mode, risk, and claim scope. Filenames and serialization fields are implementation properties, not universal Skill semantics.

## Compatibility

The inspected evidence supports `Skill` being represented as a NickLinney Context Packet Object profile. It does not establish that Context Packet serialization is the universal abstract identity of every Skill. A conforming implementation may use the profile when the NickLinney ecosystem requires it.
