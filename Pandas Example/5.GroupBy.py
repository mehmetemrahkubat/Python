# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb-1000.csv")

print(films.columns)
#columnsları ver
print("****************************")
print(films.head())
#ilk 5 indexi ver
print("****************************")
print(films.star_rating.mean())
#tüm filmlerin ortalama ratingini al
print("****************************")
print(films.groupby('genre').star_rating.mean())
#filmsi groupbya çevir daha sonra genre(tür)'e göre filmlerin ortalamalarını al

