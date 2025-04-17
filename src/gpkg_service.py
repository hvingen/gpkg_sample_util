# gpkg_service.py
# Functions for listing and loading GPKG layers

try:
    import fiona
except ImportError as e:
    raise ImportError("Required module 'fiona' is not installed. Please run 'pip install fiona'")

from pathlib import Path

import geopandas as gpd


def list_gpkg_files(directory: Path):
    """Return a list of .gpkg files in the specified directory."""
    return list(directory.glob("*.gpkg"))


def list_gpkg_layers(gpkg_path: Path):
    """Return a list of layer names in the specified GPKG file."""
    return fiona.listlayers(gpkg_path)


def load_gpkg_layer(gpkg_path: Path, layer: str):
    """Load a specific layer from a GPKG file."""
    return gpd.read_file(gpkg_path, layer=layer)
