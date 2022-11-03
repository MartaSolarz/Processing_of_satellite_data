"""Klasa zapisująca obraz do pliku tiff."""

from typing import Any, List

import rasterio as rio


class SaveToTiff:
    def __init__(self, bands: List[str], band_to_save: Any, save_path: str) -> None:
        self.bands_list = bands
        self.crs = None
        self.transform = None
        self.shape = []
        self.dtype = None
        self.save_path = save_path
        self.band_to_save = band_to_save

    def get_parameters(self) -> None:
        with rio.open(self.bands_list[1], 'r') as reader:
            band = reader.read(1)
            self.crs = reader.crs
            self.transform = reader.transform
            self.shape = band.shape
            self.dtype = band.dtype
        
    def save(self) -> None:
        self.get_parameters()
        with rio.open(self.save_path,
                    'w',
                    driver='GTiff',
                    height=self.shape[0],
                    width=self.shape[1],
                    count=1,
                    dtype=self.dtype,
                    crs=self.crs,
                    transform=self.transform
                    ) as dst:
            dst.write(self.band_to_save, 1)
            
            
def save_resampled_image(new_band: Any, base_crs: Any, base_transform: Any, save_path: str) -> None:
    """Zapisanie obrazu po resamplingu."""
    with rio.open(save_path,
                    'w',
                    driver='GTiff',
                    height=new_band.shape[0],
                    width=new_band.shape[1],
                    count=1,
                    dtype=new_band.dtype,
                    crs=base_crs,
                    transform=base_transform
                    ) as dst:
        dst.write(new_band, 1)
