# Numerical Integration Experiments
_Berliner Hochschule für Technik – Numerik II project_

This repo contains a small reproducible study of **composite trapezoidal-rule convergence** (and a few related quadrature tricks) carried out for the Numerik II module.  All code is pure Python; the results are shown in a Jupyter notebook and summarised in the accompanying PDF report.

---
## Numerical results

The notebook benchmarks three quadrature routines on two test functions  
*(all figures are generated automatically in `notebooks/2.Project_Numerical Experiments.ipynb`)*:

| Function | Definition | Interval |
|----------|------------|----------|
| **f₁(x)** | \(2 + \sin(x^{2})\) | \([0,5]\) |
| **f₂(x)** | \(4 + 2\sin(x) + \cos(3x)\) | \([0,2\pi]\) |

---

### Function f₁  — tolerance \(10^{-3}\)

<img src="images/f1_001.png" width="950">

*Summary*

* **Adaptive Trapezoidal Rule** – quickly adds points in high-variation regions  
  *error ≈ 5.5 × 10⁻⁵, evaluations = 91*
* **Summed Trapezoidal Rule** – needs many more points for similar accuracy  
  *error ≈ 3.2 × 10⁻⁴, evaluations = 257*
* **Adaptive Simpson’s Rule** – slightly better accuracy with fewer points  
  *error ≈ 2.5 × 10⁻³, evaluations = 45*

---

### Function f₂  — tolerance \(10^{-3}\)

<img src="images/f2_001.png" width="950">

*Summary*

* **Adaptive Trapezoidal Rule** – efficient again despite oscillations  
  *error = 0, evaluations = 85*
* **Summed Trapezoidal Rule** – highest accuracy with **very** few samples  
  *error = 0, evaluations = 5*
* **Adaptive Simpson’s Rule** – slightly worse here, more calls than f₁  
  *error ≈ 3.6 × 10⁻¹⁴, evaluations = 33*

---

*All errors are absolute; “evaluations” counts function calls.*




## Repository layout

| Path | Purpose |
|------|---------|
| `src/num_integ.py` | Re-usable quadrature routines (trapezoidal, adaptive, periodic variant, etc.) |
| `notebooks/2.Project_Numerical Experiments.ipynb` | Step-by-step experiments, figures, error plots |
| `report/Numerik_II___2_Project.pdf` | Final write-up turned in for assessment |
| `tests/` | (empty) placeholder for future unit tests |

---

## Quick start

```bash
# clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

# set up Python environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt    # installs numpy, matplotlib, …

# open the notebook
jupyter notebook notebooks/2.Project_Numerical\ Experiments.ipynb
