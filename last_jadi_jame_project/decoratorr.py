#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 18:14:51 2025

@author: h
"""

def ddone(func):
    def wrapper():
        print('done')
        #Bebin mishe esm har function ro gereft o print kard
        func()
    return wrapper