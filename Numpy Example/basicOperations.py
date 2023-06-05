# -*- coding: utf-8 -*-

import numpy as np

a = np.array([20,30,40,50])
b= np.arange(4)

# a=np.array([20,30,40,50])
# b=np.array([0,1,2,3])

# c=a-b
# #birbirine karşılık gelen indeksler çıkartılıyor
# print(c)

# d = b**3
# print(d)

# e=10*np.sin(a)
# print(e)
# print(e<7)#e dizisinde 7 den küçük olanları yaz

# # print(a*b)#elementwise product

# print("matris çarpımı : ", a@b)#matris çarpımı
# print("2.matris çarpımı : ",a.dot(b))#matris çarpımının farklı şekli aynı şey aslında
# #
# f= np.ones((2,4))#bellekten yer ayırma
# print(f)
# g=np.zeros((2,4))
# h = 10*np.random.random((2,4))#rast gele sayı üret
# print(h)
#
i=np.sum(b)#listedeki elemanları toplama
print(b.sum())
#
#j=np.min(b)#bdeki min değeri ver
#k=np.max(h)#hdaki max değeri ver
#
#l=np.sqrt(b)#karaköklerini vericek

# numpy_array = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
# numpy_array = numpy_array.reshape(5,2)
# #Satır bazlı birleştirme
# print(np.concatenate([numpy_array, numpy_array], axis =0))
# #Output:
# #[[0 1] 
# # [2 3] 
# # [4 5] 
# # [6 7] 
# # [8 9] 
# # [0 1] 
# # [2 3] 
# # [4 5] 
# # [6 7] 
# # [8 9]]


#Sütun bazlı birleştirme
print(np.concatenate([numpy_array, numpy_array], axis =1))
#Output:
#[[0 1 0 1] 
# [2 3 2 3] 
# [4 5 4 5] 
# [6 7 6 7] 
# [8 9 8 9]]

#mean, median, varyans ve standart sapma hesaplamak
numpy_array2 = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
print(numpy_array2.mean())
#Output:4.5
print(np.median(numpy_array2))
#Output:4.5
print(numpy_array2.var())
#Output:8.25
print(numpy_array2.std())
#Output:2.8722813232690143

# #Matrisin transpozu
# numpy_array3 = np.array([0,1, 2, 3, 4, 5, 6, 7, 8, 9])
# numpy_array3 = numpy_array.reshape(5,2)
# print(numpy_array3)
# print(numpy_array3.T)