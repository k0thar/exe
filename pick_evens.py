#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 12:36:20 2025

@author: h
"""

def pick_evens(*args):
    lst=[1,1]
    for num in args:
        if num%2==0:
            lst.append(num)
    lst.pop(0)
    lst.pop(0)
    return lst

print(pick_evens(1,3,5))