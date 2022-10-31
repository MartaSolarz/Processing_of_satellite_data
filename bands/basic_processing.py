"""Image processing - enhancement of contrast by normalization"""

from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt


class BandProcessor:

    def __init__(self, band: str) -> None:
        self.band = band
        self.bins = 256

    def get_equalize(self) -> np.ndarray:
        cdf, bins = self.create_cumulative_distribution()
        image_equalized = np.interp(self.band.flatten(), bins[:-1], cdf)

        return image_equalized.reshape(self.band.shape)
    
    def create_cumulative_distribution(self) -> Tuple:
        image_histogram, bins = np.histogram(self.band.flatten(), self.bins, density=True)
    
        cdf = image_histogram.cumsum() # cumulative distribution function
        cdf = 255 * cdf / cdf[-1] # normalize

        return cdf, bins

    def show_processed_bands(self, normalize=True) -> None:
        self.band = (self.band * 255).astype(np.uint8)
        if normalize:
            self.band = self.get_equalize()
            self.band = self.band.astype(np.uint8)
        plt.figure(figsize=(12, 12))
        plt.imshow(self.band, cmap='gray')
        plt.plot()
