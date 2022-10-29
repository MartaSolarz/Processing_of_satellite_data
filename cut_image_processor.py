"""Crop the scene to the selected window"""

from typing import Any, List

import rasterio as rio
from rasterio.windows import Window


class CutBands:

    def __init__(self, files_list: List[str]) -> None:
        self.files = files_list

    def get_cut(self) -> None:
        for file in self.files:
            self.resize(file)

    def resize(self, file: str) -> None:
        with rio.open(f'./data/{file}') as src:
            image = src.read(1, window=Window(8000, 0, 10000, 2000))
            
            self.save_new_file(image, file)
    
    def save_new_file(self, image: Any, file: str) -> None:
        with rio.open(f'data/clip_{file}', 'w', driver='GTiff', width=1300, height=1000, count=1, dtype=image.dtype) as dst:
            dst.write(image, indexes=1)
