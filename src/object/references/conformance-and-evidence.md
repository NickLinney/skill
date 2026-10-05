# Conformance and evidence model

| Claim class | Required evidence | What it supports | What it does not support |
|---|---|---|---|
| identity/version | manifest, object record, consistency check | stable declared identity | external ownership or release |
| source/derivation | source register, projection seals, comparison register | traceable derivation | truth of source claims |
| contract | readable `contract.md`, parse-before-execution rule | inspectability | safe execution |
| structure/parse/schema | validator results | package shape and declared bindings | semantic truth |
| integrity | SHA-256 inventory excluding manifest/evidence | unchanged ordinary contents | authenticity or authorization |
| semantic invariant | rule checks and qualified review | checked invariants in scope | arbitrary runtime behavior |
| behavior | execution evidence from named environment/method | behavior for that execution scope | all future executions |
| independent review | independent actor/method record | independent validation claim | authorization |
| lifecycle/authorization | external state-transition record | authorized state transition | inference from package text |
| release | tag/release envelope | release identity | canonical adoption |

Evidence is bound to identity, version, scope, method, actor, and time. Material changes invalidate downstream evidence unless re-run.
