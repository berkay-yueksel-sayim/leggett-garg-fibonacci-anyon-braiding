**Preprint archived on Zenodo:** https://doi.org/10.5281/zenodo.20372744
# LGI Letter v1.0 — Zenodo Build

**Title:** Leggett-Garg saturation and structural signatures in Fibonacci-anyon braiding
**Author:** Berkay Yuksel Sayim
**ORCID:** [0009-0004-4993-7352](https://orcid.org/0009-0004-4993-7352)
**Version:** 1.0
**Date:** 2026-05-25
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## Abstract (short)

We numerically test the three-time Leggett--Garg inequality
$K_3 \leq 1$ for the standard B$_3$ Fibonacci-anyon braiding
representation on the two-dimensional fusion space of three $\tau$
anyons. Exhaustive enumeration over all $4^L$ braid words up to
$L=11$ and random sampling to $L=40$ show that $K_3$ saturates the
Lüders bound $3/2$ to 99.998%, with the first violation already at
$L=3$. Three structural signatures accompany the saturation:
(i) replacing Fibonacci by Ising generators on the same 2D fusion
space gives $K_3=1$ exactly for every $L$ tested -- a sharp split
mirroring the Hou--Shtengel no-Bell-violation result for Ising
braiding; (ii) at the sector phase $\delta=3\pi/5$ the generator
$\sigma_1$ collapses to a scalar to machine precision and braiding
becomes impossible; (iii) the Fourier spectrum of $K_3(\delta)$
is dominated by the $2\pi/6$ harmonic, reflecting the six
R-matrix insertions per $(\sigma_1 \sigma_2)^3$ word rather than
the $\mathrm{Z}_5$ period of the central element. $K_3$ at
the optimal $L=11$ word is initial-state independent. To our
knowledge this is the first Leggett--Garg test specifically for
non-abelian, Fibonacci-anyon braiding; the Gómez-Ruiz \emph{et al.}
(2018) result applies to the abelian Kitaev-chain Majorana setting
and is methodologically distinct.

---

## What's in this archive

| File | Role |
|---|---|
| `main_v1.0.tex` | LaTeX source (RevTeX 4-2, PRX style) |
| `main_v1.0.pdf` | Compiled preprint (5 pages) |
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

Sanity checks at the head of each script (unitarity, Yang--Baxter,
$(\sigma_1\sigma_2)^3$ scalar) must pass at machine precision; if they
do not, the generator conventions have been altered.

## Key numerical claims (independently verifiable from the JSON files)

| Claim | Value | File / field |
|---|---|---|
| Fibonacci $K_3^{\max}$ (exhaustive, $L=11$) | 1.499762 | `lgi_results.json` → `best` |
| Fibonacci $K_3^{\max}$ (random, $L \geq 22$) | 1.499964 | `lgi_results.json` → `random_convergence` |
| First Fibonacci LGI violation | $L=3$, $K_3=1.292$ | `lgi_results.json` → `exhaustive_delta0.3` |
| Ising $K_3^{\max}$ at $\delta=0$ over $L=1..40$ | 1.000000 (exact) | `lgi_ising_results.json` |
| Ising $K_3^{\max}$ over deformed sector $\delta$ | 1.500 at $\delta/\pi \approx 1.167$ | `lgi_ising_results.json` → `sector_sweep` |
| $K_3(\delta)$ dominant Fourier harmonic | $k=6$ (period $2\pi/6$) | `lgi_period_and_purestate_results.json` → `period_scan.dominant_k` |
| Pure-state $K_3$ at $L=11$ optimum (9 states) | 1.499762 ± 0 | `lgi_period_and_purestate_results.json` → `pure_state_check` |
| All sanity checks | $\leq 6 \times 10^{-16}$ | `*_results.json` → `sanity` |

---

## Zenodo upload metadata (for reference at upload time)

These fields should be set when creating the Zenodo record. The
record will receive a fresh concept DOI (this is a new work, not a
new version of an existing record).

| Field | Value |
|---|---|
| **Resource type** | Preprint |
| **Title** | Leggett-Garg saturation and structural signatures in Fibonacci-anyon braiding |
| **Authors** | Berkay Yuksel Sayim (ORCID 0009-0004-4993-7352) |
| **Affiliation** | Independent researcher |
| **Description** | (paste the abstract above) |
| **Keywords** | Leggett-Garg inequality; Fibonacci anyons; non-abelian braiding; macrorealism; Lüders bound; topological quantum computation; modular tensor category; universality |
| **Publication date** | 2026-05-25 (or actual upload date) |
| **License** | Creative Commons Attribution 4.0 International (CC BY 4.0) |
| **Communities** | (optional — Zenodo physics communities if any apply) |
| **Related identifiers** | (none — this is a standalone work; leave the field empty) |

## Upload steps

1. Go to <https://zenodo.org/uploads/new>.
2. Set Resource type = **Preprint**.
3. Upload all 12 files from this archive (everything in the ZIP):
   `LICENSE`, `README.md`, `main_v1.0.tex`, `main_v1.0.pdf`,
   `lgi_letter_figure.png`, `lgi_letter_figure.py`,
   `lgi_fibonacci.py`, `lgi_results.json`,
   `lgi_ising.py`, `lgi_ising_results.json`,
   `lgi_period_and_purestate.py`, `lgi_period_and_purestate_results.json`.
   *Or* upload a single ZIP (see `sayim-2026-leggett-garg-fibonacci-anyon-braiding.zip`
   in `zenodo_releases/`, with the PDF as a separate top-level upload
   to be visible in the preview).
4. Fill in the metadata table above.
5. Save and Publish → new concept DOI is created.
6. Record the concept DOI and version DOI in
   `zenodo_releases/10_ZENODO_STATUS_SNAPSHOTS.md` (or equivalent).

---

## Build

- LaTeX engine: MiKTeX pdfTeX-1.40.29 (3 × pdflatex passes).
- Python: 3.12, NumPy and Matplotlib only.
- Sanity checks (unitarity, Yang–Baxter, $(\sigma_1\sigma_2)^3$
  scalar) pass at machine precision in every reproduction script.
