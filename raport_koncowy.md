# RAPORT KOŃCOWY - INTERPRETACJA WYNIKÓW

## Czas trwania poszczególnych klasyfikacji:

| Nazwa | Czas |
|--------------|-------------|
| Drzewa decyzyjne | 21.7 s |
| Las losowy| 31.8 s |
| Naiwny Bayes | 0.9 s |
| Ada Boost| 1 min 15.7 s |
| Prosta sieć neuronowa | 6 min 4.7 s |
| Model oparty na głębokim uczeniu | 5 min 2.1 s |

## Porównanie wyników:

| Nazwa | Wynik | Dokładność całkowita | F1 |
| ----- | ------ |------------|-----|
| Drzewa decyzyjne | ![Tekst][1] | 0.7172959186093213 | 0.6928759302557961 |
| Las losowy| ![Tekst][2] | 0.7178681871026058 |  0.691040227320729 |
| Naiwny Bayes | ![Tekst][3] | 0.6620498963903533 | 0.6584603197612633 |
| Ada Boost| ![Tekst][4] | 0.7142776162672994 | 0.6859434623226246 |
| Prosta sieć neuronowa | ![Tekst][5]  | 0.7128579999227698 | 0.6992526785423694 |
| Model oparty na głębokim uczeniu | ![Tekst][6] | 0.7141303331973544 | 0.6948937171892664 |

Legenda do wyniku (macierzy błędu):
* 0 - obszar sklasyfikowany jako niezabudowany
* 1 - obszar sklasyfikowany jako zabudowany

[1]: results/drzewa_decyzyjne.png

[2]: results/las_losowy.png

[3]: results/bayes.png

[4]: results/ada.png

[5]: results/siec_neuronowa.png

[6]: results/keras.png

> Najlepsza dokładność całkowita: las losowy

> Najgorsza dokładność całkowita: Naiwny Bayes

> Najlepsza dokładność dla klasy obszaru niezabudowanego: Naiwny Bayes (0.68)

> Najgorsza dokładność dla klasy obszaru niezabudowanego: ADA (0.5)

> Najlepsza dokładność dla klasy obszaru zabudowanego: las losowy, ADA (0.86)

> Najgorsza dokładność dla klasy obszaru zabudowanego: Naiwny Bayes (0.65)
