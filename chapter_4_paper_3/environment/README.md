# Computational Environment

The Chapter 4 notebook was written in Python and uses the packages listed in `requirements.txt`. The dependency ranges document a compatible analytical stack for spatial data processing, global and localized multivariate analysis, spatial diagnostics, clustering, nighttime-light comparisons, and aggregate-preserving spatial downscaling.

To create an isolated environment from the repository root, run:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r chapter_4_paper_3/environment/requirements.txt
jupyter lab
