# -*- coding: utf-8 -*-

import numpy as np

a = np.floor(10*np.random.random((3,4)))#küsüratlı sayıları zemine indir
print(a)
print(a.shape)#satır sütün yapısını ver.

print(a.ravel())#verileri dümdüz yazıyor.
a=a.ravel()
print(a)
print(a.shape)#12 elemandan oluşan düz bir liste.

print(a.reshape(2,6))#satır sütünlarını değiştiriyoruz.
a=a.reshape(2,6)
print(a.T)#transpozu.

print(a.reshape(3,-1))
#Yeniden boyutlandırma işleminde bir boyut -1 olarak verilirse, 
#diğer boyutlar otomatik olarak hesaplanır.
