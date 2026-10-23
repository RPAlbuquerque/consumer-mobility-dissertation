# Computational Environment

The Chapter 4 notebook was written in Python and uses the packages listed in `requirements.txt`. The dependency ranges document a compatible analytical stack for spatial data processing, global and localized multivariate analysis, spatial diagnostics, clustering, nighttime-light comparisons, and aggregate-preserving spatial downscaling.

To create an isolated environment from the repository root, run:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r chapter_4_paper_3/environment/requirements.txt
jupyter lab
```

Launch Jupyter from the repository root, the `chapter_4_paper_3` directory, or its `notebooks` directory. The notebook resolves the chapter structure from these locations and uses the project-relative input paths documented in `../data/README.md`.

Complete execution requires independently authorized access to the restricted tract-level mobility GeoPackage and local acquisition of the annual 2024 VIIRS nighttime-light raster. Depending on the operating system and Python distribution, geospatial packages such as GeoPandas, Rasterio, PyProj, and Shapely may also require compatible GDAL and PROJ system libraries.

The public notebook was checked for valid notebook structure, portable paths, cleared outputs, and syntactically valid Python cells, but it was not rerun from the restricted empirical inputs during repository packaging. The dependency ranges provide a compatible public environment rather than an exact lockfile for the original restricted computing environment.
