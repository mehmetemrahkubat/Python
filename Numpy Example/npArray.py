# -*- coding: utf-8 -*-

import numpy as np

#a = np.arange(1,10)

a=np.array([1,3,5,10,17,27])
a=a.reshape(2,3)#a'nın değerini değiştir
#içine normal parantezler içerisinde 
#yazmama sebebimiz fonkisyona 6 parametre yolluyormuş gibi görmesin diye
#liste gibi atarsak parametre olarak algılamaz.
print(a)
print(a.dtype)
print("Dimension Count =" + str(a.ndim))

#numpyda liste elemanları aynı veri tipte olmalıdır.
#numpy hepsini aynı veri tipi algılar.

b= np.array([[1,3],[5,3],[8,9],[7,5]])
print(b)
print("Dimension Count =" + str(b.ndim))