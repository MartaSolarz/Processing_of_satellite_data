"Loading selected bands from a directory and validating their names"

import os
from typing import List

PATH_DATA = r'.\data'


class LoadBands:

    def __init__(self, all_files: List[str], bands_list: List[str]) -> None:
        self.all_files = all_files
        self.bands = bands_list
        self.extract_bands = []

    def get_bands(self) -> List[str]:
        if self.is_given_object_valid():
            for band in self.bands:
                if self.is_name_valid(band) and self.is_syntax_valid(band):
                    self.create(band)
        my_bands = self.load_data()
        return my_bands

    def is_given_object_valid(self) -> bool:
        if not isinstance(self.bands, list):
            raise ValueError('Given object is not iterable. Even single band should be passed in a list')
        
        return True

    def is_name_valid(self, band: str) -> bool:
        if not isinstance(band, str):
            raise ValueError('Band name should be given as a string "BXX" where XX is a number. Eg. B05')
        
        return True

    def is_syntax_valid(self, band: str) -> bool:
        if (len(band) != 3) or not band.startswith('B'):
            raise ValueError('Band name should be given as a string "BXX" where XX is a number. Eg. B05')

        return True

    def create(self, band: str) -> None:
        for file in self.all_files:
            if band + '.tif' in file:
                self.extract_bands.append(file)
                break

    def load_data(self) -> List[str]:
        return [os.path.join(PATH_DATA, band) for band in self.extract_bands]
