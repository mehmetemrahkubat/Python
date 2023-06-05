# -*- coding: utf-8 -*-

import numpy as np #numpy yazmak yerine np olarak çağırıyoruz.

#havaDurumu = [12,26,36,4,5,12,25,17]
#print(havaDurumu)

a = np.arange(15)#0 dan başladı 15e kadar değerli liste(tamamen değil) oluşturdu.
print(a)
#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]
print(type(a))

a = np.arange(15).reshape(3,5)#3satır 5 sütun
print(a)

print("Dimension Count =" + str(a.ndim))
#*Dimension Count =Boyut Sayısı


b=np.arange(10)
print(b.shape)#tek satır 10 eleman tek boyut
print(b)
print("Dimension Count =" + str(b.ndim))

#.shape →Numpy array nesnesinin kaç satır ve sütundan oluştuğunu gösteren bir 
#tupple nesnesi döndürür.

#Dizinin satır ve sütun sayısını değiştirmek : ndarray.reshape()

#np.arange() →Python’daki range() fonksiyonuna benzer. Belirtilen başlangıç 
#değerinden başlayıp, her seferinde adım sayısı kadar arttırarak ,bitiş 
#değerine kadar olan sayıları bulunduran bir numpy dizisi dödürür.
