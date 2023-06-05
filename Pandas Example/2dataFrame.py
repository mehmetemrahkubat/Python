# -*- coding: utf-8 -*-

import pandas as pd

print("----------1------------")
df= pd.DataFrame()#boş bir dataframe
print(df)
print("----------------------")

print("-----------2-----------")
data=[10,20,25,36,1,44,56,89]
df1=pd.DataFrame(data)#data grid view'e benzer.
print(df1)
print("----------------------")

print("------------3----------")
data2=[["Mehmet",33,"İstanbul"],["Saliha",32,"Sakarya"],["Hilmiye",50,"Giresun"]]
df2=pd.DataFrame(data2)
print(df2)
print("----------------------")

print("-----------4-----------")
data3=[["Mehmet",33,"İstanbul"],["Saliha",32,"Sakarya"],["Hilmiye",50,"Giresun"]]
df3=pd.DataFrame(data3,columns=["İsim","Yaş","Şehir"])
print(df3)
print("----------------------")

print("-----------5-----------")
data4=[["Mehmet",33,"İstanbul"],["Saliha",32,"Sakarya"],["Hilmiye",50,"Giresun"]]
df4=pd.DataFrame(data4,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df4)
print("----------------------")

print("------------6----------")
data5=[["Mehmet",33,"İstanbul"],["Saliha",32,"Sakarya"],["Hilmiye",50,"Giresun"]]
df5=pd.DataFrame(data5,columns=["İsim","Yaş","Şehir"],index=["a","b","c"])
print(df5)
print("----------------------")

print("-----------7-----------")
data6={"İsim":["Mehmet","Saliha","Hilmiye"],
       "Yaş":[33,32,50],
       "Şehir":["İstanbul","Sakarya","Giresun"]}
       
df6=pd.DataFrame(data6,columns=["İsim","Yaş","Şehir"],index=[1,2,3])
print(df6)
print("----------------------")

print("-----------8-----------")
print(df6["İsim"])
print("----------------------")

print("-----------9-----------")
print(df6["Yaş"])
print("----------------------")

print("-----------10-----------")
print(df6["Şehir"])
print("----------------------")

#print("-----------11-----------")
#del df6["Şehir"] #or pandas property (df6.pop("Şehir"))
#print(df6)
#print("----------------------")

print("-----------12-----------")
print(df6.loc[2])#no functions, this is an index
print("----------------------")

print("-----------13-----------")
print(df6.iloc[1])#bizim verdiğimiz index önemli değil sırası önemli 
print("----------------------")

print("-----------14-----------")
df6=df3.append(df4)#EKLE
print(df6)
print("----------------------")

print("-----------15-----------")
print(df6.head())#binlerce data olduğu zaman sadece fikir elde etmek için
#BAŞTAKİLERİ görmek istediğimiz zaman kullanılır.(BAŞ)
print("----------------------")

print("-----------16-----------")
print(df6.tail())#binlerce data olduğu zaman sadece fikir elde etmek için
#SONDAKİLERİ görmek istediğimiz zaman kullanılır.(KUYRUK)
print("----------------------")
    
