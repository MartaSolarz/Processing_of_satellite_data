# Using Python Packages and Machine Learning Tools to Analyze Satellite Images

![Picture](https://maxarv2-cms-production.s3.amazonaws.com/uploads/image/image_value/3708/constellation_beauty_shots_2-80.jpg)

Source: *https://maxarv2-cms-production.s3.amazonaws.com/uploads/image/image_value/3708/constellation_beauty_shots_2-80.jpg*

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## List of contents: ##
**I. Introduction**

**II. Project stages**

1. Download a satellite image from the Open Access Hub.
2. Initial reading of the data.
3. Calculation of NDVI, NDWI, SCI indicators and saving these files to the results folder.
4. Creating a mask with Corine Land Cover to prepare the mask for classification for ML algorithms
5. Preparing the input for models - compiling them in the dataframe in the ``pandas``` module.
6. Transformation of input data and division into training and testing sets.
7. Training of various classifiers available in the ```scikit-learn``` package.
8. Training of a classifier based on deep learning using the ```Keras``` package.
9. List and comparison of error matrix results obtained after applying individual methods.

**III. Project and library content**

**IV. Checkpoints**

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## I. Introduction

Machine learning has gained great popularity in issues related to the analysis and processing of images, including satellite images. In addition, easy access to tools for creating machine learning models allows for quick prototyping of new systems.

In this project I will combine several different machine learning tools and models. I will write a classifier whose task will be to guess one of the two main classes of surface type (whether a given surface is a built-up area or not), based on the Corine Land Cover set and three remote sensing indicator images (NDVI, NDWI and SCI).

## II. Project stages

**1. Downloading a satellite image from the Open Access Hub.**

About data:

- date of acquisition: 2020-09-14 09:50:29.024
- file name: S2B_MSIL1C_20200914T095029_N0209_R079_T34UDC_20200914T111045.SAFE
- identifier: S2B_MSIL1C_20200914T095029_N0209_R079_T34UDC_20200914T111045
- satellite: Sentinel-2B
- instrument: MSI
- area: around Warsaw

Sentinel 2 channels:

| Channel number | Name |
|--------------|-------------|
| Band 1 | Coastal aerosol |
| Band 2 | Blue	|
| Band 3 | Green |
| Band 4 | Red |
| Band 5 | Vegetation red edge	|
| Band 6 | Vegetation red edge	|
| Band 7 | Vegetation red edge	|
| Band 8 | NIR	|
| Band 8A | Narrow NIR	|
| Band 9 | Water vapour	|
| Band 10 | SWIR (Cirrus)	|
| Band 11 | SWIR |
| Band 12 | SWIR |

**2. Initial reading of the data.**

- loading channels;
- cutting the scene to Warsaw and the immediate vicinity;
- enhancing the color contrast in the image (spatial enhancement);
- RGB color compositions:
  ```[4,3,2] (Natural colors), [8,4,3] (False colors), [11,8,2] (Agriculture), [8,11,12]```.

**3. Calculation of NDVI, NDWI, SCI indicators and saving these files to the results folder.**

> **NDVI** = (NIR - Red) / (NIR + Red)

> **NDWI** = (Green - NIR) / (Green + NIR)

> **SCI** = (SWIR - NIR) / (SWIR + NIR)

**4. Creating a mask with Corine Land Cover to prepare the mask for classification for ML algorithms.**

> **Step 1** - image resampling (due to differences in the projection of images from Sentinel and Corine Land Cover);

> **Step 2** - creating a binary file, where zeros represent built-up areas and ones represent undeveloped areas;

> **Step 3** - saving the received image to a new file.

**5. Preparing input for models - compiling them in a dataframe in the ``pandas``` module.**

> **Step 1** - loading previously prepared files: clc, NDVI, NDWI, SCI;

> **Step 2** - filling empty `numpy array` with values;

> **Step 3** - transforming the array into a data frame from the `pandas` module.

**6. Transformation of input data and division into training and testing sets.**

> Using functions to divide data into a test and training set from the `scikit-learn` library.

**7. Training various classifiers available in the ```scikit-learn``` package.**

Methods used:
- Decision trees,
- Random forests,
- Naive Bayes classifier,
-Ada Boost,
- simple neural network.

**8. Training a deep learning-based classifier using the ```Keras``` package.**

**9. Summary and comparison of error matrix results obtained after applying individual methods.**

Listed in the file `raport_koncowy.md`.


## III. Project and library content ##

#### Main project files: #### 
- ```main_1.ipynb``` - etapy 1,2,3
- ```main_2.ipynb``` - etap 4
- ```main_3.ipynb``` - etap 5,6,7,8

#### Data: ####
- ```data/*```
- ```results/*```

#### My own helpful packages: ####
- ```bands/basic_processing.py``` - contrast enhancement in the image;
- ```bands/display.py``` - displaying satellite images;
- ```bands/load.py``` - loading channels;
- ```color_compositions.py``` - creating color compositions;
- ```cut_image_processor.py``` - cropping satellite images;
- ```indexes.py``` - calculation of remote sensing indices;
- ```reproject_raster.py``` - image resampling;
- ```save_data.py``` - saving images to a file;

#### Python external modules:

From the standard library:
- ```os```
- ```typing```

Installed:

```bash
$ pip install -r requirements.txt
```

- ```matplotlib```
- ```numpy```
- ```pandas```
- ```rasterio```
- ```scikit-learn```
- ```keras```
- ```tensorflow```

## IV. Checkpoints

1. November 2, 2022 - stages 1,2 - DONE
2. November 16, 2022 - stages 3,4 - DONE
3. November 30, 2022 - stages 5,6 - DONE
4. December 22, 2022 - stages 7,8,9 (entire project) - DONE

**Author:** Marta Solarz
