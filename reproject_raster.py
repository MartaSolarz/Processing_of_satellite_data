"""Resampling obrazu."""

from typing import Any

import numpy as np
from rasterio.warp import reproject, Resampling


def reproject_raster(reprojected_band: Any, reprojected_transform: Any, reprojected_crs: Any, reprojecting_band: Any, reprojecting_transform: Any, reprojecting_crs: Any) -> np.ndarray:
    """Reprojekcja obrazu rastrowego."""
    destination = np.zeros(reprojecting_band.shape) # Tworzymy pustą tablicę na obraz po reprojekcji

    reproject(reprojected_band, destination, src_transform=reprojected_transform, src_crs=reprojected_crs, dst_transform=reprojecting_transform, dst_crs=reprojecting_crs, resampling=Resampling.mode)
    
    return destination
