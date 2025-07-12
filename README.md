# Numerical Integration Experiments
_Berliner Hochschule für Technik – Numerik II project_

This repo contains a small reproducible study of **composite trapezoidal-rule convergence** (and a few related quadrature tricks) carried out for the Numerik II module.  All code is pure Python; the results are shown in a Jupyter notebook and summarised in the accompanying PDF report.

---

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
