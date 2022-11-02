"""Funkcje wyświetlające w różny sposób obrazy satelitarne."""

from typing import Any

import matplotlib.pyplot as plt
import numpy as np

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
