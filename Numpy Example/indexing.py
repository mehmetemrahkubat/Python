# -*- coding: utf-8 -*-

import numpy as np

sayilar = np.array([0,5,10,25,30,40,41])
print(sayilar[::-1])#TEK BOYUTLU DİZİLER İÇİN tersten yaz
print(sayilar[6])
print(sayilar[0:3])

for row in sayilar:
    print(row)
    
sayilar2 = np.array([[0,5,10],[25,30,40]])
for row in sayilar2:
    print(row)

#for row in sayilar2.flat:
#    print(row)    

#sayilar2 = np.array([[0,5,10],[25,30,40]])
#print(sayilar2[0])#0.satırı ver
#print(sayilar2[1])#1.satırı ver
#print(sayilar2[0,2])
#print(sayilar2[:,2])#tüm satırlardaki 2. indeksi ver
#print(sayilar2[:,0:2])#0. sütundan 2. sutüna kadar 2 dahil deil tüm veriler
#print(sayilar2[-1,:])#en son satırda bütün sütunları ver
#print(sayilar2[:,-1])#en son sütündaki tüm satıları ver

#print(np.zeros((5,4)))#sıfırdan oluşan matris
#
#print(np.ones((5,4)))#1lerden oluşan matris
#
#print(np.eye((5)))#birim matris
    

  




