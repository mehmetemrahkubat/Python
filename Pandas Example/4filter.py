# -*- coding: utf-8 -*-

import pandas as pd

films=pd.read_csv("imdb-1000.csv")
print(films)
print("--------------------------1-------------------------")
print(films.columns)
print("-------------------------2--------------------------")
print(films.head())
print(films.tail())
print("------------------------3---------------------------")
print(films['title'])
print("------------------------4---------------------------")
print(films['title'].head())
print("-------------------------5--------------------------")
print(films.title)
print("---------------------------6------------------------")
print(films[['title',"star_rating"]].head())
print("-----------------------7----------------------------")
print(films[:9][['title',"star_rating"]])
print("------------------------8---------------------------")

print(films[
        (films['star_rating']>=8.5)&(films['star_rating']<=9.0)
        ][['title','star_rating']])
print("------------------------9---------------------------")

print(films[
        (films['star_rating']>=9.0)|(films['star_rating']<=7.5)
        ][['title','star_rating']])

print("--------------------------10-------------------------")

print(films.query('star_rating>=9.0 & star_rating<=9.2'
                  )[['title','star_rating']])
print("-------------------------11--------------------------")