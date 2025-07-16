#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 14:02:45 2025

@author: h
"""
def deco(f):
    def wrapper(n):
        import time
        start = time.time()
        result=f(n)
        finish=time.time()
        return finish-start,result
    return wrapper

@deco
def list_n(n):
    l=[]
    for i in range(1,n+1):
        l.append(i)
    return l

print(list_n(5))