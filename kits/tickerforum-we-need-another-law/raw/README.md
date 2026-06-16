# raw/ — the sovereign layer

Everything in this folder is produced **deterministically, with no model**, by `../build_raw.py`
from the controlled-token index (`../data/tickerforum_legal_index_v1.csv`). This is the layer a
local node, the webform, or plain `grep` can deliver on its own — and the portable payload you
feed to any LLM for narration.

| File | What it is |
|------|------------|
| `tickerforum_raw.md` | Human/LLM-readable raw dump — six-axis facts, controlled caveat **tokens**, primary-source links. No prose, no narration. |
| `tickerforum_raw.json` | Same records, machine-readable; caveats split into a token list. |
| `NARRATION_PROMPT.md` | The portable, model-agnostic prompt that turns the raw payload into a narrated study (Claude / Grok / Gemini / Qwen / Ollama / BitNet). |

## The two-layer contract

- **Raw (here):** facts, grades, signals, caveat tokens, source pointers. Sovereign,
  reproducible, no model in the result path. SHA-pinned via `source_csv_sha256`.
- **Narration (everything prose):** the six-axis study and any web-form copy. A *sweep* on top
  of the raw layer, written by a named model, attributed, swappable. Never the source of truth.

## Regenerate / run the sweep

```bash
python3 ../build_raw.py                                   # rebuild raw from the index
cat NARRATION_PROMPT.md tickerforum_raw.md | <your-llm>   # produce a narrated study, any model
```

Improve the **raw** layer (richer fields, sharper tokens, more records) and every downstream
narration improves with it — no matter which model writes the prose.

*Open the method; keep the model. Leads, not verdicts. Not legal advice.*
