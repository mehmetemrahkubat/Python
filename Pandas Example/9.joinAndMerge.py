# -*- coding: utf-8 -*-

import pandas as pd


data1= {
        'id':[1,2,3,4],
        'ad':["Mehmet","Saliha","Gülşah","Hilmiye"],
        'soyad':["Kubat","Bir","Kubat","Kubat"]
        }

data2= {
        'id':[1,3,7,10],
        'ad':["İsmail","Ahmet","Süleyman","Mert"],
        'soyad':["Kubat","Özkan","İpşir","Ulaş"]
        }

data1Df=pd.DataFrame(data1)
data2Df=pd.DataFrame(data2)

print(data1Df)

print("******************************")

print(data2Df)

print("******************************")

print(pd.merge(data1Df,data2Df,on="id",how="inner"))
#iki tane datada indeks değerleri aynı olanları yan yana getirerek yaz.

print("******************************")

print(pd.merge(data1Df,data2Df,on="id",how="left"))

print("******************************")

print(pd.merge(data1Df,data2Df,on="id",how="right"))

print("******************************")

print(pd.concat([data1Df,data2Df]))

print("******************************")

print(pd.concat([data1Df,data2Df],axis=1))