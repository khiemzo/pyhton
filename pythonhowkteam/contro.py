 -*- coding: utf-8 -*-
chuoi = "xin chào các bạn"
con_tro = None

for i in range(len(chuoi)//2):
    con_tro = chuoi[i]
    chuoi[i] = chuoi[len(chuoi)-i-1]
    chuoi[len(chuoi)-i-1] = con_tro


print("Chuỗi đảo ngược là:", chuoi)
