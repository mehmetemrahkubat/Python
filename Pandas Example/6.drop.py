# -*- coding: utf-8 -*-

import pandas as pd

films = pd.read_csv("imdb-1000.csv")
print(films.columns)

print("*************1***************")

print(films.drop("content_rating",axis=1).head().columns)
#filmsdeki content rating columnsunu uçur.
#axis=1 sütun
#axis=0 satır
print(films.head())
#değişmedi...

print("***********2*****************")

films=films.drop("content_rating",axis=1)
print(films.head())

print("************3****************")

films=films.drop("actors_list",axis=1)
print(films)

print("*************4***************")

films=films.drop(2,axis=0)
print(films)

print("*************5***************")

rowsToDrop =[0,1,3,4,8,9,11,15,25,35]
films=films.drop(rowsToDrop,axis=0)
print(films.mean())


