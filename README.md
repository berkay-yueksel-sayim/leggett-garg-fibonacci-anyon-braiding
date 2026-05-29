# LGI Letter v1.1 — Zenodo Build (Corrections to v1.0)

**Title:** Leggett-Garg saturation and structural signatures in Fibonacci-anyon braiding
**Author:** Berkay Yuksel Sayim
**ORCID:** [0009-0004-4993-7352](https://orcid.org/0009-0004-4993-7352)
**Affiliation:** Independent Research, Germany
**Version:** 1.1
**Date:** 2026-05-28
**Resource type:** Preprint
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## v1.1 Changes (corrections to v1.0)

This release corrects four items in v1.0 (Zenodo Concept-DOI
[10.5281/zenodo.20372744](https://doi.org/10.5281/zenodo.20372744)).
**No numerical results, no figures, and no other body claims are affected.**

1. **Fourier-harmonic correction (envelope vs fixed-word).**
   v1.0 reported the dominant Fourier harmonic of $K_3(\delta)$ as $k=6$
   (period $2\pi/6$), based on a sample at $L_{\max} = 9$. Independent
   reproducer runs at $L_{\max} = 7$ and a pre-v1.1 sanity re-run at
   $L_{\max} = 8$ both find $k=3$ as the dominant harmonic of the
   *envelope* $K_{3,\max}(\delta) = \max_{|w| \leq L} K_3(\delta;\,w)$,
   with stable $k=3/k=6$ amplitude ratio 1.061 → 1.063. The algebraic
   $2\pi/6$ identity applies to each *fixed* word
   (six $R$-matrix insertions in $(\sigma_1\sigma_2)^3$); the envelope
   shows optimal-word reshuffling on a finer scale. Both periodicities
   are now stated separately in the abstract, overview, figure caption,
   and §III.D body.

2. **Hou et al. → Clarke-Sau-Das Sarma (PRX 6, 021005).** The
   bibliography entry previously labeled "Hou et al." at PRX 6, 021005
   (2016) is corrected to its true attribution: D. J. Clarke, J. D. Sau,
   and S. Das Sarma, *A practical phase gate for producing Bell
   violations in Majorana wires*. Body text "Hou–Shtengel split" is
   updated to "Clarke–Sau–Das-Sarma split" throughout. Body content
   (Clifford-only Ising braiding, missing non-Clifford direction) is
   unchanged — only the attribution is fixed.

3. **Sorella 2023 bibliography entry corrected.** Title corrected from
   the v1.0 placeholder *"Representation dependence of the Tsirelson
   bound"* to the verified title *"On the representations of Bell's
   operators in Quantum Mechanics"*; publication venue updated to
   Foundations of Physics 53, 59 (2023), DOI
   [10.1007/s10701-023-00699-6](https://doi.org/10.1007/s10701-023-00699-6).

4. **Minev 2025 bibliography entry corrected.** Author list expanded to
   the full 8-author form (with K. Najafi as second author, not "S.
   Najafi" as in v1.0); title updated to *"Realizing string-net
   condensation: Fibonacci anyon braiding for universal gates and
   sampling chromatic polynomials"*; article number 6225 added.

## Abstract

We numerically test the three-time Leggett–Garg inequality
$K_3 \leq 1$ for the standard B$_3$ Fibonacci-anyon braiding
representation on the two-dimensional fusion space of three $\tau$
anyons. Exhaustive enumeration over all $4^L$ braid words up to
$L = 11$ and random sampling to $L = 40$ show that $K_3$ saturates
the Lüders bound $3/2$ to $99.998\%$, with the first violation
already at $L = 3$. Three structural signatures accompany the
saturation. First, replacing Fibonacci by Ising generators on the
same 2D fusion space gives $K_3 = 1$ exactly for every $L \leq 40$,
a sharp split mirroring the Clarke–Sau–Das-Sarma no-Bell-violation
result for Ising braiding in the spatial CHSH setting. Second, the
sector phase $\delta$ tunes a singular point $\delta = 3\pi/5$ at
which the generator $\sigma_1$ collapses to a scalar to machine
precision and braiding becomes impossible. Third, the Fourier
spectrum of the envelope $K_{3,\max}(\delta)$ is dominated by the
$k=3$ harmonic (period $2\pi/3$); each individual fixed-word
$K_3(\delta;\,w)$ has the algebraically expected $2\pi/6$ period
from six $R$-matrix insertions in $(\sigma_1\sigma_2)^3$, but the
envelope shows optimal-word reshuffling on a finer scale. $K_3$ at
the optimal $L=11$ word is initial-state independent. To our
knowledge this is the first Leggett–Garg test specifically for
non-abelian Fibonacci-anyon braiding.

---

## What's in this archive

| File | Role |
|---|---|
| `main_v1.1.tex` | LaTeX source (RevTeX 4-2, PRX style) |
| `main_v1.1.pdf` | Compiled preprint (6 pages) |
| `lgi_letter_figure.png` | Two-panel preprint figure |
| `lgi_letter_figure.py` | Preprint-figure builder |
| `lgi_fibonacci.py` | Main Fibonacci LGI computation |
| `lgi_results.json` | Fibonacci raw results |
| `lgi_ising.py` | Ising LGI computation (universality split) |
| `lgi_ising_results.json` | Ising raw results |
| `lgi_period_and_purestate.py` | $K_3(\delta)$ period scan + pure-state robustness |
| `lgi_period_and_purestate_results.json` | period and pure-state raw results |
| `LICENSE` | CC BY 4.0 |
| `README.md` | This file |

## Reproduction

Deterministic. NumPy and Matplotlib only.

```bash
python lgi_fibonacci.py              # Fibonacci main, seed 20260524
python lgi_ising.py                  # Ising, seed 20260525
python lgi_period_and_purestate.py   # period + pure-state, seed 20260525
python lgi_letter_figure.py          # preprint figure
```

Sanity checks at the head of each script (unitarity, Yang–Baxter,
$(\sigma_1\sigma_2)^3$ scalar) must pass at machine precision; if they
do not, the generator conventions have been altered.

## Key numerical claims (independently verifiable from the JSON files)

| Claim | Value | File / field |
|---|---|---|
| Fibonacci $K_3^{\max}$ (exhaustive, $L=11$) | 1.499762 | `lgi_results.json` → `best` |
| Fibonacci $K_3^{\max}$ (random, $L \geq 22$) | 1.499964 | `lgi_results.json` → `random_convergence` |
| First Fibonacci LGI violation | $L=3$, $K_3=1.292$ | `lgi_results.json` → `exhaustive_delta0.3` |
| Ising $K_3^{\max}$ at $\delta=0$ over $L=1\ldots 40$ | 1.000000 (exact) | `lgi_ising_results.json` |
| Ising $K_3^{\max}$ over deformed sector $\delta$ | 1.500 at $\delta/\pi \approx 1.167$ | `lgi_ising_results.json` → `sector_sweep` |
| Envelope $K_{3,\max}(\delta)$ dominant Fourier harmonic (corrected) | $k=3$ (period $2\pi/3$); fixed-word $K_3(\delta;\,w)$ has $2\pi/6$ | `lgi_period_and_purestate_results.json` → `period_scan` |
| Pure-state $K_3$ at $L=11$ optimum (9 states) | 1.499762 ± 0 | `lgi_period_and_purestate_results.json` → `pure_state_check` |
| All sanity checks | $\leq 6 \times 10^{-16}$ | `*_results.json` → `sanity` |

---

## Zenodo upload metadata (v1.1 as New Version under existing Concept-DOI)

This is a **corrected New Version** of the existing record (Concept-DOI
[10.5281/zenodo.20372744](https://doi.org/10.5281/zenodo.20372744));
it should be uploaded as "New Version" of that record, not as a new
concept.

| Field | Value |
|---|---|
| **Resource type** | Preprint |
| **Title** | Leggett-Garg saturation and structural signatures in Fibonacci-anyon braiding |
| **Authors** | Berkay Yuksel Sayim (ORCID 0009-0004-4993-7352) |
| **Affiliation** | Independent Research, Germany |
| **Description** | (paste the v1.1 changes block + abstract above) |
| **Keywords** | Leggett-Garg inequality; Fibonacci anyons; non-abelian braiding; macrorealism; Lüders bound; topological quantum computation; modular tensor category; universality |
| **Publication date** | 2026-05-28 |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Related identifiers** | (none — this letter remains standalone) |
| **Version** | 1.1 |

## Upload steps (New Version)

1. Go to existing Zenodo record at <https://doi.org/10.5281/zenodo.20372744>.
2. Click "New version".
3. Upload all 12 files from this archive (everything in the v11_build ZIP):
   `LICENSE`, `README.md`, `main_v1.1.tex`, `main_v1.1.pdf`,
   `lgi_letter_figure.png`, `lgi_letter_figure.py`,
   `lgi_fibonacci.py`, `lgi_results.json`,
   `lgi_ising.py`, `lgi_ising_results.json`,
   `lgi_period_and_purestate.py`, `lgi_period_and_purestate_results.json`.
   Set Version = 1.1; keep all other metadata fields (Title, Authors,
   Resource type, License, Related identifiers) unchanged from v1.0.
4. Update Description with the v1.1 changelog (see above).
5. Save and Publish → new Version-DOI assigned under the same
   Concept-DOI 10.5281/zenodo.20372744.
6. Record the new Version-DOI in `zenodo_releases/10_ZENODO_STATUS_SNAPSHOTS.md`.

---

## Build

- LaTeX engine: MiKTeX pdfTeX-1.40.29 (3 × pdflatex passes, converged).
- Python: 3.12, NumPy and Matplotlib only.
- Sanity checks (unitarity, Yang–Baxter, $(\sigma_1\sigma_2)^3$ scalar)
  pass at machine precision in every reproduction script.
