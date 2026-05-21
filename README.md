# Photodimerization-in-Water Scout

Public-safe HHMI proof artifact for an AI-assisted computational chemistry workflow.

This repository demonstrates a small, inspectable scout loop:

1. load public literature/demo rows;
2. preserve source anchors and caveats;
3. create an illustrative triage order;
4. write explanation cards and a visual summary;
5. name the next source check or experiment that would reduce uncertainty.

The scientific motivation is aqueous photodimerization: when can water, hosts,
micelles, or other local environments help photoreactive molecules find useful
encounter geometries?

## Why this exists

This is a proof artifact for an HHMI/Janelia AI Scientist - Computational
Chemistry application. It is intentionally modest: the scout is not a validated
predictive model. It is a runnable example of how I turn uncertain chemical
evidence into a transparent experiment-prioritization loop.

The long-term direction is a world model for light-responsive molecular systems:
molecule + environment + light -> assembly state -> encounter geometry ->
photochemical outcome -> next experiment.

## Public-data boundary

This repository contains only the public-safe demo layer. It does not include
non-public research rows, unpublished quantitative values, raw spectra, audit
tables, or the full verifier artifact.

Use these files for review:

- `data/public_demo_cases.csv` - the external sharing boundary.
- `scripts/run_public_scout.py` - dependency-free public scout script.
- `outputs/public_demo_ranked_candidates.csv` - generated illustrative order.
- `outputs/public_demo_explanation_cards.md` - generated explanation cards.
- `outputs/public_demo_rows.svg` - generated visual table.
- `docs/index.html` - human-facing overview page.
- `docs/triage_loop_plain_language.html` - nontechnical explanation of the loop.

## Run locally

```sh
python3 scripts/run_public_scout.py
python3 -m unittest discover -s tests
```

The script uses only the Python standard library. It rewrites the generated
public outputs from `data/public_demo_cases.csv`.

## What to look for

- The scout keeps caveats visible beside every row.
- The row order is illustrative triage, not model validation.
- The schema row is explicitly labeled as a mechanics demo, not evidence.
- The output points to the next source check rather than pretending the model is
  already complete.

## Application framing

This small repository is meant to show three things:

- chemistry depth: photochemistry, host-guest systems, aqueous organization, and
  light-responsive molecules;
- computational bridge: structured data, transparent scoring, generated cards,
  and reproducible outputs;
- scientific honesty: public-data boundaries, visible caveats, and explicit
  next experiments.
