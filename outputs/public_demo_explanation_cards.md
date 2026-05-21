# Public Demo Explanation Cards

Generated only from `data/public_demo_cases.csv`. These cards are public-safe literature/demo scaffolds for the HHMI proof packet; they are not a trained-model validation set and the order below is illustrative triage, not a predictive accuracy claim.

Public demo rows: 6 total.

## 1. 6-methylcoumarin - cucurbit[8]uril in water

- **Case ID:** CG-CB8-6MC-001
- **Row class / status:** public_crystal_water_comparison / public_now
- **What it shows:** CB8-catalyzed/supramolecular photodimerization reported
- **Why it matters:** host confinement / co-encapsulation
- **Geometry signal:** CCDC 814052 measured as crystal-distance-fail / aligned prior
- **Source anchor:** Pemberton et al. Chem. Commun. 2011 DOI 10.1039/C1CC11164G; RSC ESI CCDC 814052
- **Caveat:** Crystal contact is an interpretable prior from a host-guest CIF, not direct water-phase encounter geometry.
- **Next check:** Keep geometry caveat visible; next check is derivative/source caption verification before quantitative reuse.

## 2. coumarin - water direct UV

- **Case ID:** COUMARIN-WATER-DIRECT
- **Row class / status:** public_evidence / public_now
- **What it shows:** published direct aqueous photodimerization context
- **Why it matters:** aqueous heterogeneity / aggregation can support direct photodimerization
- **Geometry signal:** no measured public crystal prior in this row
- **Source anchor:** Jeyapalan et al. J. Photochem. Photobiol. A 2021 DOI 10.1016/j.jphotochem.2021.113492
- **Caveat:** Public-facing row is qualitative; do not attach unchecked quantitative values.
- **Next check:** Use as the public baseline aqueous row; paper-check any quantitative values before exposing them.

## 3. trans-cinnamic acids - gamma-cyclodextrin in water

- **Case ID:** TCA-GCD-FAMILY
- **Row class / status:** public_water_outcome_only / promote_public_demo
- **What it shows:** templated photodimerization of trans-cinnamic acids reported
- **Why it matters:** gamma-cyclodextrin host templating gives a host-contrast row
- **Geometry signal:** no substrate-specific crystal geometry assessed
- **Source anchor:** Pattabiraman et al. Organic Letters 2005 DOI 10.1021/ol047866k
- **Caveat:** Same paper family as the CB8 row; present as host-contrast scaffold rather than independent exhaustive evidence.
- **Next check:** Check whether public visual should split derivative-level behavior or keep this as a family-level host row.

## 4. trans-cinnamic acids - cucurbit[8]uril in water

- **Case ID:** TCA-CB8-FAMILY
- **Row class / status:** public_water_outcome_only / promote_public_demo
- **What it shows:** templated photodimerization of trans-cinnamic acids reported
- **Why it matters:** CB8 host templating organizes cinnamic-acid guests
- **Geometry signal:** no substrate-specific crystal geometry assessed
- **Source anchor:** Pattabiraman et al. Organic Letters 2005 DOI 10.1021/ol047866k
- **Caveat:** Family-level public row; do not imply all derivatives share one outcome or a measured crystal geometry.
- **Next check:** Extract derivative-specific substrate names/outcome classes from the article/SI if this becomes more than a demo row.

## 5. trans-cinnamic acid esters - water-soluble Pd nanocage

- **Case ID:** CESTER-PD-NANOCAGE-FAMILY
- **Row class / status:** public_water_outcome_only / promote_public_demo
- **What it shows:** templated photodimerization of trans-cinnamic acid esters reported
- **Why it matters:** water-soluble metal cage confinement
- **Geometry signal:** no substrate-specific crystal geometry assessed
- **Source anchor:** Karthikeyan and Ramamurthy J. Org. Chem. 2007 DOI 10.1021/jo0617722
- **Caveat:** Public nanocage precedent only; keep as family-level literature context rather than a validated model row.
- **Next check:** Extract ester list/qualitative selectivity labels from the source before adding derivative-level claims.

## 6. public-safe generic alkene schema - detached RDKit/scoring mechanics

- **Case ID:** SCHEMA-PUBLIC-MECHANICS
- **Row class / status:** schema_demo_only / public_schema_demo
- **What it shows:** not evidence — demonstrates row classes/status/caveat mechanics
- **Why it matters:** shows how source/status/caveat fields flow through the public export
- **Geometry signal:** no measured geometry; explicit schema-only row
- **Source anchor:** Generated from Scout v0 schema only; no source-evidence row attached
- **Caveat:** Schema row is visual mechanics only and must not be counted as literature evidence.
- **Next check:** Replace or demote once six or more source-checked public literature rows are available.
