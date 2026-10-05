from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
MANIFEST = ROOT / "packet.manifest.json"
EVIDENCE = ROOT / "validation" / "package-validation.json"

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def schema_ok(value, schema, location="$", errors=None):
    errors = [] if errors is None else errors
    expected = schema.get("type")
    if expected == "object" and not isinstance(value, dict): errors.append(f"{location}: expected object")
    if expected == "array" and not isinstance(value, list): errors.append(f"{location}: expected array")
    if expected == "string" and not isinstance(value, str): errors.append(f"{location}: expected string")
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value: errors.append(f"{location}: missing {key}")
        for key, child in schema.get("properties", {}).items():
            if key in value: schema_ok(value[key], child, f"{location}.{key}", errors)
    if isinstance(value, list) and isinstance(schema.get("items"), dict):
        for i, item in enumerate(value): schema_ok(item, schema["items"], f"{location}[{i}]")
    if "const" in schema and value != schema["const"]: errors.append(f"{location}: expected {schema['const']}")
    return errors

def main():
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks = []
    required = [
        "packet.manifest.json", "ABSTRACT-OBJECT-SPECIFICATION.md", "abstract-specification.md",
        "implementation-abstract.md", "contract.md", "applicability.json", "lifecycle.json", "agents/openai.yaml",
        "unresolved-state.json", "catalog/source-register.json", "objects/skill-abstract-object.record.json",
        "schemas/object-record.schema.json", "schemas/package.manifest.schema.json", "scripts/validate_package.py",
        "validation/README.md"
    ]
    missing = [p for p in required if not (ROOT / p).exists()]
    checks.append({"check": "STRUCTURAL_PASS", "status": "PASS" if not missing else "FAIL", "missing": missing})

    parse_failures = []
    for p in ROOT.rglob("*.json"):
        if p == EVIDENCE: continue
        try: json.loads(p.read_text(encoding="utf-8"))
        except Exception as exc: parse_failures.append({"path": str(p.relative_to(ROOT)), "error": str(exc)})
    checks.append({"check": "PARSE_PASS", "status": "PASS" if not parse_failures else "FAIL", "failures": parse_failures})

    schema_failures = []
    for binding in manifest["schema_bindings"]:
        artifact = ROOT / binding["artifact"]
        schema = json.loads((ROOT / binding["schema"]).read_text(encoding="utf-8"))
        value = json.loads(artifact.read_text(encoding="utf-8"))
        errors = schema_ok(value, schema)
        if errors: schema_failures.append({"binding": binding, "errors": errors})
    checks.append({"check": "SCHEMA_CONFORMANCE_PASS", "status": "PASS" if not schema_failures else "FAIL", "failures": schema_failures})

    semantic = json.loads((ROOT / "objects/skill-abstract-object.record.json").read_text(encoding="utf-8"))
    semantic_errors = []
    if not semantic.get("capability_bearing_object", {}).get("required"): semantic_errors.append("capability-bearing Object is required")
    if not semantic.get("execution_model", {}).get("required"): semantic_errors.append("Execution Model is required")
    if semantic.get("contract_ref") != "contract.md": semantic_errors.append("contract reference is not inspectable")
    if "SkillAbstractObject" != semantic.get("kind"): semantic_errors.append("wrong abstract Object kind")
    checks.append({"check": "SEMANTIC_INVARIANT_PASS", "status": "PASS" if not semantic_errors else "FAIL", "failures": semantic_errors})

    inventory = {item["path"]: item for item in manifest["files"]}
    excluded = set(manifest["integrity"]["content_inventory_excludes"])
    integrity_failures = []
    if "packet.manifest.json" in inventory or "packet.manifest.json" not in excluded:
        integrity_failures.append("manifest must be excluded from ordinary inventory")
    for path, item in inventory.items():
        actual = ROOT / path
        if not actual.exists(): integrity_failures.append(f"missing {path}"); continue
        if path in excluded: continue
        if actual.stat().st_size != item["bytes"] or sha256(actual) != item["sha256"]:
            integrity_failures.append(f"digest mismatch {path}")
    checks.append({"check": "INTEGRITY_PASS", "status": "PASS" if not integrity_failures else "FAIL", "failures": integrity_failures, "inventory_entries": len(inventory), "excluded": sorted(excluded)})

    identity_errors = []
    if manifest["object_id"] != semantic["object_id"]: identity_errors.append("manifest/object record identity mismatch")
    if manifest["entrypoint"] != "ABSTRACT-OBJECT-SPECIFICATION.md": identity_errors.append("wrong entrypoint")
    checks.append({"check": "IDENTITY_AND_ENTRYPOINT_PASS", "status": "PASS" if not identity_errors else "FAIL", "failures": identity_errors})

    failures = [c for c in checks if c["status"] != "PASS"]
    evidence = {
        "validator_version": "skill-abstract-object-validator-1.0.0",
        "package": manifest["object_id"],
        "scope": "exact working-tree package at validation time",
        "checks": checks,
        "state": "VALIDATED_WITH_EXPLICIT_EVIDENCE" if not failures else "VALIDATION_FAILED",
        "claims_proved": [c["check"] for c in checks if c["status"] == "PASS"],
        "nonclaims": ["behavioral validation", "independent validation", "authorization", "installation", "activation", "deployment", "canonical adoption", "release publication"]
    }
    EVIDENCE.write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: Skill Abstract Object package validation" if not failures else "FAIL: Skill Abstract Object package validation")
    for check in checks: print(f"{check['status']}: {check['check']}")
    raise SystemExit(1 if failures else 0)

if __name__ == "__main__": main()
