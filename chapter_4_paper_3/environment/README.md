# Python Environment

The notebook was prepared for a Python 3.11 environment with the packages listed in `requirements.txt`. The version ranges preserve the principal APIs used by the workflow without claiming bit-for-bit reproduction across every operating system and geospatial-library build.

From the `chapter_4_paper_3` directory, create and activate an isolated environment before installing the requirements:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r environment/requirements.txt
jupyter lab notebooks/consumer_mobility_market_access.ipynb
```

The notebook does not download empirical inputs automatically. Before execution, authorized users must place the files described in `data/README.md` at the expected project-relative paths.

Geospatial packages may rely on platform-specific binary libraries. Installation through a current Python distribution or environment manager that supplies compatible GDAL, GEOS, and PROJ builds may be preferable on systems where wheels are unavailable.
