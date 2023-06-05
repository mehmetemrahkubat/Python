# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

s= pd.Series()
data = np.array(["Mehmet","Emrah","Kubat"])
s=pd.Series(data)#pandasla çalıştıracak ortama getiriyoruz
print(s)#indeks değerlerini getir diyoruz yaptığımız şey görselleştirme
#hızlı arama işlemleri için kullanılır.
print("------------------------")

a= pd.Series()
data1 = np.array(["Mehmet","Emrah","Kubat"])
a=pd.Series(data1, index=[5,2,3])#indeks değerlerini ben veriyorum kafana göre verme
print(a)#eğer indeks değerini dizimizin boyutundan az girersek hata olur.
print(a[5])
print("------------------------")


data2 = {"matematik":10, 
         "fizik":20, 
         "beden eğitimi":100
         }
a2=pd.Series(data2)
print(a2)
print(a2[0])
print(a2["matematik"])
print("------------------------")

data3 = {"matematik":10, 
         "fizik":20, 
         "beden eğitimi":100
         }
a3=pd.Series(data3, index=["fizik","matematik","beden eğitimi"])
print(a3)
print("------------------------")


a4=pd.Series(5, index=[1,2,3,4,5])
print(a4)
print("------------------------")