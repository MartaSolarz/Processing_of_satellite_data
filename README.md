# Wykorzystanie pakietów pythona i narzędzi uczenia maszynowego do analizy obrazu satelitarnego

![Picture](https://th.bing.com/th/id/R.dfd389c03ec22d93ccaf303523debda5?rik=x6WXK7JOwXNWGQ&pid=ImgRaw&r=0)

Źródło: *https://th.bing.com/th/id/R.dfd389c03ec22d93ccaf303523debda5?rik=x6WXK7JOwXNWGQ&pid=ImgRaw&r=0*

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Spis treści: ##
**I. Wstęp**

**II. Etapy projektu**

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

**2. Wstępne zapoznanie się z danymi.**

- wczytanie kanałów;
- przycięcie sceny do zasięgu Warszawy i najbliższych okolic;
- wzmocnienie kontrastu kolorów na obrazie (wzmocnienie przestrzenne);
- kompozycje barwne RGB: 
 ```[4,3,2] (Barwy naturalne), [8,4,3] (Fałszywe kolory), [11,8,2] (Rolnictwo), [8,11,12]```.

**3. Obliczenie wskaźników NDVI, NDWI, SCI.**

**4. Stworzenie maski z Corine Land Cover, gdzie zera będą obszarami zabudowanymi, a jedynki niezabudowanymi, co przyda się w dalszym toku modelowania, podczas tworzenia modeli uczenia maszynowego.**

**5. Przygotowanie wsadu dla modeli - zestawienie ich w dataframe w module ```pandas```.**

**6. Transformacja danych wejściowych i podział na zbiór treningowy i testowy.**

**7. Trening różnych klasyfikatorów dostępnych w pakiecie ```scikit-learn``` - spróbuję wykorzystać metody: Drzewa decyzyjne, Lasy losowe, Naiwny Bayesowski klasyfikator, Ada Boost i prostą sieć neuronową.**

**8. Trening klasyfikatora opartego na uczeniu głębokim przy wykorzystaniu pakietu ```Keras```.**

**9. Zestawienie i porównanie wyników otrzymanych po zastosowaniu poszczególnych modeli.**

## III. Zawartość projektu i biblioteki ##

#### Plik główny projektu: #### 
- ```main.ipynb```

#### Dane: ####
- ```data/*```

#### Moduły własne: ####
- ```bands/basic_processing.py``` - wzmocnienie kontrastu na obrazie;
- ```bands/display.py``` - wyświetlanie obrazów satelitarnych;
- ```bands/load.py``` - wczytywanie kanałów;
- ```color_compositions.py``` - tworzenie komozycji barwnych;
- ```cut_image_processor.py``` - przycinanie obrazów satelitarnych;

#### Moduły zewnętrzne pythona:

Z biblioteki standardowej:
- ```os```
- ```typing```

Doinstalowane [```pip install -r requirements.txt```]: 
- ```matplotlib```
- ```numpy```
- ```rasterio```

## IV. Punkty kontrolne

1. Do 2.11 - etapy 1,2 - ZROBIONE
2. Do 16.11 - etapy 3,4
3. Do 30.11 - etapy 5,6
4. Do 22.12 - etapy 7,8,9 (cały projekt)

**Autor:** Marta Solarz
