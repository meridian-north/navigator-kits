# TickerForum post — draft (copy-ready)

*Draft for the thread. Edit freely — this is your voice plus a few tightened lines. Not legal advice.*

---

I'm building an offline index over U.S. primary legal sources — a research **navigator**. The
intent is that it surfaces statute text and the questions worth asking, not verdicts.

Here's the honest part of how it works. I run a **deterministic model** first: its results can be
proven by math to be repeatable — same input, same output, every time. But that model isn't smart
enough to *score* or explain anything. So I had an LLM make a second pass to add the **narration**.
Every record is graded, caveated, and SHA-256 pinned, so any output traces back to a signed
version of the data — the "milspec replayability" part.

Which means: **the small model is replayable, but the narration is not.** And I want to be precise
about that, because it's where people overclaim.

A bigger local model (Qwen 32B/72B class) makes the *prose* better — it does **not** make the prose
*reproducible*. Milspec replay needs a closed, enumerable output **plus** a pinned runtime. That's
why a deterministic *verdict* or a *controlled caveat token* can be signed and replayed, and why
free-form prose can't — on any model, Qwen included. Even at temperature 0 with a fixed seed,
large-model prose is only bit-for-bit reproducible if you also lock the kernels, batching,
quantization, and hardware (floating-point addition isn't associative, so GPU reductions drift).
The only way to drag narration back under the milspec guarantee is to **constrain it to a fixed
reply list or a grammar** — at which point it's no longer narration, it's *deterministic selection*
feeding the sovereign layer. A regex bounds *what can come out*; the pinned runtime decides *which
one did*. You need both, and then you've got a selector, not a narrator.

That's also why the architecture is built the way it is: the **raw layer carries the facts**
(model-free, attested), so a weak narrator can fail *loudly* without corrupting the index. When I
ran the narration task through a tiny local 1.58-bit model, it hallucinated a fact that wasn't in
the records and looped — and that failure is **Beacon-signed and reproducible** (`9ee93ac2`): same
weights + same prompt + milspec → same text. The failure is auditable, not anecdotal. The facts
underneath never moved.

## For the nerds — compute split

Same narration task, both ends measured (token counts ~estimates, ≈4 chars/token; the point is the
provenance, not the digits):

- **Local / sovereign (BitNet b1.58 2B, milspec):** ~622 tokens, deterministic, Beacon-signed
  `9ee93ac2`, weight-attested. The part you can *prove*.
- **Cloud narration (same task):** ~854 tokens, not signed, attributed. Better prose, no replay
  guarantee. Guardrailed with a fixed prompt: no fact invention, preserve grades,
  navigator-not-advice, self-attribution.

And the headline number — **what it took to score the whole legal corpus locally on BitNet:
~41 million tokens** (estimate; tens of millions). That's 6,381 U.S. Code sections across five
editions — 46,001 statute units — read, routed, and ternary-verdicted on a 2-billion-parameter
model running *offline*, where every verdict is byte-replayable and signable. The math is open in
`COMPUTE_ESTIMATE.md`; tune the knobs yourself. Put it next to the cloud number and the whole
thesis is in two figures: **~41,000,000 sovereign, signed local tokens did the deterministic
lifting; ~28,000 cloud tokens wrote the prose on top.** The provable work is the heavy work.

And the whole-kit build, honestly:

- **Model-free compute: 0 LLM tokens.** The three figures (matplotlib), the raw export, and the
  SHA manifest are pure Python — they regenerate forever at zero model cost.
- **Cloud authoring (shipped files): ~28,300 tokens** — the floor, i.e. the text actually sitting
  in the kit's `.md` / `.html` / `.csv` / `.py` / `.json`.
- **True end-to-end cloud session: more than that, and I won't pretend to a precise number** —
  research, web lookups, tool output, and reasoning across the build add up to several× the floor
  once input context is counted. Estimate, not measurement.

So the shape of it: the **sovereign, provable part is cheap and reproducible** — ~622 signed local
tokens, plus a raw layer that rebuilds for **zero** model tokens. The expensive part was the cloud
*authoring* — which is exactly the part that is **not** milspec, which is why it's fenced in by the
raw layer and the guardrail prompt so it can't quietly rewrite the record.

## Scope, and the honest gaps

- **Federal only — no state law.** No state statutes, constitutions, or municipal codes. For most
  issues people actually face, state law is where the action is. That's the biggest hole.
- **Partial even federally:** a couple of U.S. Code titles in the deep layer across historical
  editions (~1994–2018), not all 54; the antitrust material is a hand-built kit, not full Title 15.
- **Not real-time:** deep-layer editions stop around 2018 — always check the live source it links to.
- **Case law and regulations are mostly pointers** (links out), not rehosted full text.
- **The readable write-ups are AI-narrated and labeled as such;** the facts underneath are the
  model-free, signed layer.

Bottom line: a useful compass for finding and *dating* federal primary sources — not a substitute
for a lawyer, and not yet a state-law tool. Leads, not verdicts.

---

*The content here is provided without warranty and is not legal advice. For advice specific to your
situation, contact a licensed professional in your jurisdiction.*
