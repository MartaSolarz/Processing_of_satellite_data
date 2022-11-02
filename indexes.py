"""Funkcje wyliczające wskaźniki dla danych z Sentinela 2"""

from typing import Any

import rasterio as rio


def get_ndvi(band4: Any, band8: Any) -> Any:
    """Funkcja wyliczająca wskaźnik NDVI."""
    
    with rio.open(band4) as b4src:
        b4 = b4src.read(1)
    
    with rio.open(band8) as b8src:
        b8 = b8src.read(1)
    
    ndvi = (b8 - b4) / (b8 + b4)

    return ndvi


def get_ndwi(band3: Any, band8: Any) -> Any:
    """Funkcja wyliczająca wskaźnik NDWI."""
    
    with rio.open(band3) as b3src:
        b3 = b3src.read(1)
    
    with rio.open(band8) as b8src:
        b8 = b8src.read(1)
    
    ndwi = (b3 - b8) / (b3 + b8)

    return ndwi


def get_sci(band8: Any, band11: Any) -> Any:
    """Funkcja wyliczająca wskaźnik SCI."""
    
    with rio.open(band11) as b11src:
        b11 = b11src.read(1)
    
    with rio.open(band8) as b8src:
        b8 = b8src.read(1)
    
    sci = (b11 - b8) / (b11 + b8)

    return sci