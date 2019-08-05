#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 12:40:15 2019

@author: yuribyk
"""

def new_flame(n):
    a="FLAME"
    m=len(a)+1
    static=m-1
    for i in range(static,1,-1):
        b = a*m
        index= (n%i)*m
        q=m-2
        select = b[ index : index + q ]
        print(select)
        a = select
        m-=1
    return select
        
        
        
        
for i in range(30):
    print("flame ",i,new_flame(i))