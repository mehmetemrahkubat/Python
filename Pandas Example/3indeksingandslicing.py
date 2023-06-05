# -*- coding: utf-8 -*-

import pandas as pd

notlar=pd.read_csv("grades.csv")
notlar.columns=["İsim","Soyisim","SSN"
                ,"Test1","Test2","Test3","Test4"
                ,"Final","Sonuc"]
print(notlar)
print("------1-------")
print(notlar.loc[:,"İsim"])
print("------2-------")
print(notlar.loc[:5,"İsim"])
print("------3-------")
print(notlar.loc[:5,"İsim":"Test4"])
print("------4-------")
print(notlar.loc[:5,["İsim","Final"]])
print("------5-------")
print(notlar.loc[:5,:"Test2"])
print("------6-------")
print(notlar.loc[::-1,"İsim"])
print("------7-------")