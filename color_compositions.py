"""Stworzenie kompozycji RGB"""

from typing import List

import numpy as np
import rasterio as rio


class RGBBuilder:

    def __init__(self, paths: List[str]) -> None:
        self.paths = paths
        self.bands = None
    
    def get_rgb(self) -> np.ndarray:
        self.bands = self.build_rgb()
        rgb = np.dstack(self.bands)

        return rgb

    def build_rgb(self) -> List[str]:
        bands = []
        for path in self.paths:
            self.open_band(bands, path)
        
        return bands

    def open_band(self, bands: List[str], path: str) -> None:
        with rio.open(path) as file:
            band = file.read(1)
            bands.append(band)
    
