"""Funkcje wyświetlające w różny sposób obrazy satelitarne."""

from typing import Any, Tuple

import matplotlib.pyplot as plt
import numpy as np
import rasterio as rio

from bands.basic_processing import BandProcessor


def show_bands(band: Any) -> None:
    """Podstawowa funkcja wyświetlania obrazu satelitarnego."""
    plt.figure(figsize=(12, 12))
    plt.imshow(band, cmap='gray')
    plt.plot()


def show_band_index(band: Any, normalize=True, cmap='gray', cbar=False):
    """Wyświetlanie obrazu z możliwością ustawienia skali barwnej - parametr cmap."""
    if normalize:
        band = (band * 255).astype(np.uint8)
        band = BandProcessor(band).get_equalize()
        band = band.astype(np.uint8)
        
    plt.figure(figsize=(12, 12))
    plt.imshow(band, cmap=cmap)

    if cbar:
        plt.colorbar()
    
    plt.plot()
    

def display_parameters(band: Any) -> Tuple:
    """Wyświetlenie informacji o kanale."""
    with rio.open(band) as s2:
        base_band = s2.read(1)
        base_crs = s2.crs
        base_transform = s2.transform

        return base_band, base_crs, base_transform
