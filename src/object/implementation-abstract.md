# NickLinney Implementation Abstract

This implementation maps the technology-independent Skill type onto the NickLinney/Object `1.0.0-alpha.1` package contract. The package uses `ABSTRACT-OBJECT-SPECIFICATION.md`, not `SKILL.md`, because this target represents an abstract type and is not itself an agent-executable Skill.

The package is self-describing through its manifest, abstract specification, implementation abstract, contract, applicability, package metadata, source register, schema bindings, object record, lifecycle, validation evidence, integrity inventory, and explicit nonclaims. It is provenance-bearing through source IDs, exact Object tag/commit, projection seals, comparison register, and source-to-rule mappings. It is structurally verifiable through JSON schemas and a deterministic validator.

The historical Skill identity fields (`skill_id`, `version`, `name`, `purpose`, `composition`, `execution_modes`, `embedded_contract`) are semantic Skill fields. The Object fields (`object_id`, `object_kind`, `entrypoint`, `applicability`, `schema_bindings`, `files`, `dependencies`, `nonclaims`) are package-envelope fields. `packet_id` is a Context Packet compatibility alias only when a concrete implementation elects that profile; it is not duplicated here as a second abstract identity.

No concrete execution or instantiation is materialized. `objects/skill-abstract-object.record.json` is the abstract type record, not a concrete Skill implementation. `SKILL.md` is explicitly not applicable; `agents/openai.yaml` is package metadata, not a runtime execution entrypoint.
