# -*- coding: utf-8 -*-

import pandas as pd

url = "http://bit.ly/uforeports"

data = pd.read_csv(url)
print(data)
print(data.columns)


print("****************************")

print(data[["City",
            "State",
            "Colors Reported",
            "Time",
            "Shape Reported"]].head())
#istediğim columsları ver ilk 5 tanesinin

print("****************************")

print(data.isnull().head(100))#boş olanlar true
print(data.notnull().head(100))#dolu olanlar true

print("****************************")

print(data.isnull().sum())#boşların sayısını ver

print("****************************")

print(data[data.City.isnull()])

print("****************************")

print(data[data.City.isnull()].head())

print("****************************")

print(data[data.Time.isnull()].head())

print("****************************")

#print(data.shape)#satır sütun sayısı
#data=data.dropna()#boş columnslara sahipleri yok et
#print(data.shape)
#print(data)
#
#print("****************************")
#
#print(data.shape)#satır sütun sayısı
#data=data.dropna(how = "any")#herhangi bir satırın herhangi bir değeri null ise
#print(data.shape)
#print(data)

print("****************************")

#print(data.shape)#satır sütun sayısı
#data=data.dropna(how = "all")#tamamen boş data var ise
#print(data.shape)
#print(data)

print("****************************")

#print(data.shape)#satır sütun sayısı
#data=data.dropna(subset = ["City","Colors Reported"],how = "all")
##şehir ve report rengi olmayanı gönder.
#print(data.shape)
#print(data)

print("****************************")

#print(data.shape)#satır sütun sayısı
#data=data.dropna(subset = ["City","Colors Reported"],how = "any")
##şehir veya report rengi olmayanı gönder.
#print(data.shape)
#print(data)

print("****************************")

data['Shape Reported'].fillna(value = 'BELİRSİZ', inplace = True)#nan olan değeri belirsiz olarak değiştir. inplace true bellektede değiştir 
print(data['Shape Reported'].value_counts(dropna=False))#shape reportta değerlerin sayısını ver droplama atma


