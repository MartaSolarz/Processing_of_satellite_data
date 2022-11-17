# Wykorzystanie pakietów pythona i narzędzi uczenia maszynowego do analizy obrazu satelitarnego

![Picture](https://th.bing.com/th/id/R.dfd389c03ec22d93ccaf303523debda5?rik=x6WXK7JOwXNWGQ&pid=ImgRaw&r=0)

Źródło: *https://th.bing.com/th/id/R.dfd389c03ec22d93ccaf303523debda5?rik=x6WXK7JOwXNWGQ&pid=ImgRaw&r=0*

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Spis treści: ##
**I. Wstęp**

**II. Etapy projektu**

1. Pobranie obrazu satelitarnego z Open Access Hub.
2. Wstępne zapoznanie się z danymi.
3. Obliczenie wskaźników NDVI, NDWI, SCI oraz zapis tych plików do folderu results.
4. Stworzenie maski z Corine Land Cover w celu przygotowania maski do klasyfikacji dla algorytmów ML
5. Przygotowanie wsadu dla modeli - zestawienie ich w dataframe w module ```pandas```.
6. Transformacja danych wejściowych i podział na zbiór treningowy i testowy.
7. Trening różnych klasyfikatorów dostępnych w pakiecie ```scikit-learn``` - spróbuję wykorzystać metody: Drzewa decyzyjne, Lasy losowe, Naiwny Bayesowski klasyfikator, Ada Boost i prostą sieć neuronową.
8. Trening klasyfikatora opartego na uczeniu głębokim przy wykorzystaniu pakietu ```Keras```.
9. Zestawienie i porównanie wyników otrzymanych po zastosowaniu poszczególnych modeli.

**III. Zawartość projektu i biblioteki**

**IV. Punkty kontrolne**

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## I. Wstęp

Uczenie maszynowe zdobyło bardzo dużą popularność w zagadnieniach związanych z analizą i przetwarzaniem obrazów, w tym obrazów satelitarnych. Do tego łatwy dostęp do narzędzi umożliwiających tworzenie modeli uczenia maszynowego pozwala na szybkie prototypowanie nowych systemów.

W tym projekcie połączę kilka różnych narzędzi i modeli uczenia maszynowego. Napiszę klasyfikator, którego zadaniem będzie odgadnięcie jednej z dwóch głównych klas rodzaju powierzchni (czy dana powierzchnia jest obszarem zabudowanym czy nie), bazując na zbiorze Corine Land Cover i trzech obrazach wskaźników teledetekcyjnych (NDVI, NDWI i SCI).

## II. Etapy projektu

**1. Pobranie obrazu satelitarnego z Open Access Hub.**

O danych: 

- data pozyskania: 2020-09-14 09:50:29.024
- nazwa pliku: S2B_MSIL1C_20200914T095029_N0209_R079_T34UDC_20200914T111045.SAFE
- identyfikatorr: S2B_MSIL1C_20200914T095029_N0209_R079_T34UDC_20200914T111045
- satelita: Sentinel-2B
- instrument: MSI
- obszar: okolice Warszawy

Kanały Sentinela 2:

| Numer kanału | Nazwa |
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

**2. Wstępne zapoznanie się z danymi.**

- wczytanie kanałów;
- przycięcie sceny do zasięgu Warszawy i najbliższych okolic;
- wzmocnienie kontrastu kolorów na obrazie (wzmocnienie przestrzenne);
- kompozycje barwne RGB: 
 ```[4,3,2] (Barwy naturalne), [8,4,3] (Fałszywe kolory), [11,8,2] (Rolnictwo), [8,11,12]```.

**3. Obliczenie wskaźników NDVI, NDWI, SCI oraz zapis tych plików do folderu results.**

> **NDVI** = (NIR - Red) / (NIR + Red)

> **NDWI** = (Green - NIR) / (Green + NIR)

> **SCI** = (SWIR - NIR) / (SWIR + NIR)

**4. Stworzenie maski z Corine Land Cover w celu przygotowania maski do klasyfikacji dla algorytmów ML.**

> **Krok 1** - resampling obrazu (z powodu różnic w projekcji obrazów z Sentinela i Corine Land Cover);

> **Krok 2** - stworzenie pliku binarnego, gdzie zera reprezentują obszary zabudowane, a jedynki niezabudowane;

> **Krok 3** - zapisanie do nowego pliku otrzymanego obrazu.

**5. Przygotowanie wsadu dla modeli - zestawienie ich w dataframe w module ```pandas```.**

> **Krok 1** - wczytanie wcześniej przygotowanych plików: clc, NDVI, NDWI, SCI;

> **Krok 2** - wypełnienie pustej `numpy array` wartościami;

> **Krok 3** - transformacja tablicy do data frame z modułu `pandas`.

**6. Transformacja danych wejściowych i podział na zbiór treningowy i testowy.**

> Wykorzystanie funkcji do podziału danych na zbiór testowy i treningowy z biblioteki `scikit-learn`.

**7. Trening różnych klasyfikatorów dostępnych w pakiecie ```scikit-learn``` - spróbuję wykorzystać metody: Drzewa decyzyjne, Lasy losowe, Naiwny Bayesowski klasyfikator, Ada Boost i prostą sieć neuronową.**

**8. Trening klasyfikatora opartego na uczeniu głębokim przy wykorzystaniu pakietu ```Keras```.**

**9. Zestawienie i porównanie wyników otrzymanych po zastosowaniu poszczególnych modeli.**

## III. Zawartość projektu i biblioteki ##

#### Pliki główne projektu: #### 
- ```main_1.ipynb``` - etapy 1,2,3
- ```main_2.ipynb``` - etap 4
- ```main_3.ipynb``` - etap 5,6

#### Dane: ####
- ```data/*```
- ```results/*``` - dane wynikowe;

#### Moduły własne: ####
- ```bands/basic_processing.py``` - wzmocnienie kontrastu na obrazie;
- ```bands/display.py``` - wyświetlanie obrazów satelitarnych;
- ```bands/load.py``` - wczytywanie kanałów;
- ```color_compositions.py``` - tworzenie komozycji barwnych;
- ```cut_image_processor.py``` - przycinanie obrazów satelitarnych;
- ```indexes.py``` - obliczanie wskaźników teledetekcyjnych;
- ```reproject_raster.py``` - resampling obrazu;
- ```save_data.py``` - zapisywanie obrazów do pliku;

#### Moduły zewnętrzne pythona:

Z biblioteki standardowej:
- ```os```
- ```typing```

Doinstalowane:

```bash
$ pip install -r requirements.txt
```

- ```matplotlib```
- ```numpy```
- ```pandas```
- ```rasterio```
- ```scikit-learn```

## IV. Punkty kontrolne

1. Do 2.11 - etapy 1,2 - ZROBIONE
2. Do 16.11 - etapy 3,4 - ZROBIONE
3. Do 30.11 - etapy 5,6 - ZROBIONE
4. Do 22.12 - etapy 7,8,9 (cały projekt)

**Autor:** Marta Solarz
