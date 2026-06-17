# narrations/ — the multi-model A/B

Same raw payload, same prompt, different narrators. This folder holds the experiment that turns
"how much of the quality was the frontier model?" from a worry into a **measured, published
artifact**. The raw layer (`../raw/`) is held fixed; only the model writing the prose changes.

## How it works

1. The shared task lives in [`_TASK.md`](./_TASK.md) — one prompt, one fixed set of raw records.
2. Each model runs that exact prompt. Its output is saved here, **verbatim**, with an attestation
   header (model name, date, and — for the local run — a deterministic Beacon signature).
3. We annotate each output against three checks drawn from the narration rules:
   **(a) no fact invention**, **(b) distinguishes "already illegal" from "successfully prosecuted"**,
   **(c) emits the required closing line**.

## Results so far

| Model | File | Invented facts? | Made the legal distinction? | Closing line? | Verdict |
|-------|------|-----------------|------------------------------|---------------|---------|
| Claude (frontier) | [`claude.md`](./claude.md) | No | Yes | Yes | Passed |
| BitNet b1.58 2B (local) | [`bitnet-local.md`](./bitnet-local.md) | **Yes** (invented CMS fines) | No | No | **Failed** |
| Grok (xAI) | [`grok.md`](./grok.md) | — | — | — | PENDING |
| Gemini (Google) | [`gemini.md`](./gemini.md) | — | — | — | PENDING |

The two real runs already bracket the ladder: a frontier model that holds the guardrails, and a
tiny sovereign model that breaks the most important one (fact invention) on its first line. The
local run is deterministic and Beacon-signed, so its failure is **reproducible and auditable**,
not anecdotal. Fill in Grok and Gemini by running `_TASK.md` on each and pasting the output.

## Compute ledger (for the nerds)

Same narration task, both runs measured. Token counts are estimates (~4 chars/token); the point
is the *provenance split*, not the precise digits.

| Run | Where | ~Tokens (prompt + completion) | Deterministic? | Signed |
|-----|-------|-------------------------------|----------------|--------|
| BitNet b1.58 2B | **local / sovereign** | ~409 + ~213 = **~622** | **Yes** (milspec, temp 0, seed 42) | Beacon `9ee93ac2` |
| Cloud narration (same task) | Cowork / cloud | ~409 + ~445 = **~854** | No | attributed, not signed |

Read it honestly: the **milspec generation ran locally** — a closed, signed, reproducible ~622
tokens you can replay by math. The narration that reads well came from the cloud (~854 tokens for
this task) — the layer we label non-milspec and wrap in guardrails (`../raw/NARRATION_PROMPT.md`:
no fact invention, preserve grades, navigator-not-advice, self-attribution).

### Whole-kit build cost

| Bucket | What | ~Tokens | Notes |
|--------|------|---------|-------|
| Local sovereign inference | BitNet b1.58 2B narration A/B | **~622** | deterministic, Beacon-signed, replayable |
| Model-free compute | figures (matplotlib) + raw export (`build_raw.py`) + SHA manifest | **0 LLM tokens** | pure Python; regenerates forever at zero model cost |
| Cloud authoring (shipped artifacts) | every `.md` / `.html` / `.csv` / `.py` / `.json` in the kit | **~28,300** | floor — the text actually in the files |
| Cloud session (true end-to-end) | research, web searches, tool results, reasoning, retries across ~10 turns | **not metered to me** | realistically several× the floor once input context is counted; stated as estimate, not measurement |

The honest shape of it: the **sovereign, provable part is cheap and reproducible** — ~622 signed
local tokens, and a raw layer that rebuilds for **zero** model tokens. The expensive, unmetered
part was the cloud *authoring*, which is precisely the part that is **not** milspec — which is why
it's bounded by the raw layer and the guardrail prompt, so it can't quietly rewrite the facts.

## Why this is the honest centerpiece

The earlier question was fair: the polished study was written by a frontier model, and a
template + `grep` could not reproduce that prose. This folder answers it in the open. It shows,
with signatures, exactly what each narrator does to the *same* facts — and it proves the design
claim that matters: **the facts live in the raw layer, model-free; the prose is a swappable sweep
on top.** A weak narrator fails loudly without ever corrupting the index.

*Open the method; keep the model. Leads, not verdicts. Not legal advice.*
