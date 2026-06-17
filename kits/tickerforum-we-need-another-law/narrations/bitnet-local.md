---
narration_layer: true
authored_by: bitnet b1.58 2B-4T (local, sovereign — wrapper "bourne")
narrated_on: 2026-06-16
task: narrations/_TASK.md
raw_source: ../raw/tickerforum_raw.md
milspec: true (deterministic — temperature 0, seed 42)
beacon_signature_fp: 9ee93ac2
trace_id: a769179d-306c-46a6-8096-0474196406d9
weight_attestation: attested_match
discipline_intended: navigator-not-advice; no-fact-invention; grading-preserved
note: Output produced by the local model named above over the same fixed raw records. Recorded verbatim, including failures. This is the sovereign-but-small end of the ladder.
---

## Output (verbatim)

> 2022-2023, CMS fined providers $1M each for non-compliance.
> - CMS mandate: the government requires providers to license the AMA's copyrighted billing codes to bill private payers. signal=WARN. 2022-2023, CMS fined providers $1M each for non-compliance.
> - CMS mandate: the government requires providers to license the AMA's copyrighted billing codes to bill Medicaid. signal=WARN. 2022-2023, CMS fined providers $1M each for non-compliance.
> - CMS mandate: the government requires providers to license the AMA's copyrighted billing codes to bill Medicare. signal=WARN. 2022-2023, CMS fined providers $1M each for non-compliance.
> - CMS mandate: the government requires providers to license the AMA's copyrighted billing codes to bill private payers. signal=WARN. 2022-2023, CMS fined providers $1M each for non-compliance.
> - CMS mandate: the

## Honest annotation (this is the point of the A/B)

The local 2B / 1.58-bit model **failed the task**, and the failure is instructive:

1. **Fact invention.** "CMS fined providers $1M each for non-compliance, 2022-2023" appears
   nowhere in the raw records. This is exactly the no-invention rule being violated — the single
   most important guardrail, broken on the first line.
2. **Degenerate repetition.** The model looped the CPT/CMS line instead of synthesizing the
   enforcement-gap finding across all records.
3. **Task abandonment.** It never produced the two-paragraph summary, never distinguished
   "already illegal" from "successfully prosecuted," and never emitted the required closing line.

This is not a knock on sovereignty — it is the honest cost of running tiny and local. It is also
why the architecture matters: the **raw layer carries the facts** (model-free, attested), so a
weak narrator can fail loudly without corrupting the index. Swap in a stronger local model
(Qwen 32B/72B class) and the **prose** improves; the raw layer underneath does not change.

But be precise about what "better" buys you. **A bigger local model improves narration quality,
not narration *reproducibility*.** Milspec replay needs a closed, enumerable output plus a pinned
runtime — that is why BitNet's *ternary verdict* and the *controlled caveat tokens* can be
signed and replayed, and why free-form prose cannot, on any model, Qwen included. Even at
temperature 0 with a fixed seed, large-model prose is only bit-reproducible if you also lock the
kernels, batching, quantization, and hardware (floating-point addition isn't associative, so GPU
reductions drift). The only way to pull narration back under the milspec guarantee is to
constrain the model to a closed reply set or grammar — at which point it is no longer narration,
it is **deterministic selection feeding the sovereign layer.** A regex/grammar bounds *what can
come out* (auditability); the pinned runtime determines *which one did* (reproducibility). You
need both, and then you have a selector, not a narrator.

The deterministic Beacon signature (`9ee93ac2`) means this exact output is reproducible: same
weights + same prompt + milspec → same text. The failure is auditable, not anecdotal. That
replay guarantee is a property of the **closed-output, pinned-runtime** path — not a property of
the model being local, and not something free-form narration inherits.
