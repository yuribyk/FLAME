#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 23:18:20 2019

@author: yuribyk
"""

a="madhuri dixit"
b="yoyo honey singh"

a=a.lower()
b=b.lower()

aa=list(a)
aaa="+".join(aa)

bb=list(b)
bbb="+".join(bb)

import vector_plus_minus_gamma

c = vector_plus_minus_gamma.sub(aaa,bbb)

print(c)
n=0
for i in c:
    if i[1]!=" ":
        if i[0]>0:
            n+=i[0]
        else:
            n-=i[0]
print("FLAME on number: ",n)

import NEW_flame

d=NEW_flame.new_flame(n)
print(d)