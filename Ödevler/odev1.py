# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 11:00:29 2025

@author: tvn
"""
# %%
#  Print  fonksiyonu
print("hasan")
# ayırma operatörü koyma 
print("hasan ","Tüven","A","b","C",sep='*')
#%%
# veri tipleri
a=1
b=2.3
print(type(a))
print(type(b))
c="merhaba"
d="r"
print(type(c))
print(type(d))
#%%
# veri yapıları
# list mutable yapıdaki veriler
liste1=[3,2,"hasan",'*']
print(liste1[3])
liste2=[3,4,2,7]
liste2.sort()
print(liste2)
#%%
x="hasan"
x.capitalize()
#%%
def topla(deg1,deg2):
    c=deg1+deg2
    return c
print(topla(5,6))
#%%
class Oto():
    renk="beyaz"
    model="astra"
    marka="opel"
    def rrr(self):
        print("motor çalıştı")
        
al = Oto()
print(al)
print(al.marka)
print(al.model)
print(al.renk)
al.rrr()
#%%
ad=lambda x:2**x+x
ad(3)




