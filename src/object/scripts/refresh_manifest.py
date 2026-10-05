from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).parents[1]
MANIFEST = ROOT / "packet.manifest.json"
EXCLUDED = {"packet.manifest.json", "validation/package-validation.json"}

def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""): h.update(block)
    return h.hexdigest()

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
manifest["files"] = [
    {"path": str(path.relative_to(ROOT)), "bytes": path.stat().st_size, "sha256": digest(path)}
    for path in sorted(ROOT.rglob("*")) if path.is_file() and str(path.relative_to(ROOT)) not in EXCLUDED
]
MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"refreshed {len(manifest['files'])} inventory entries")
