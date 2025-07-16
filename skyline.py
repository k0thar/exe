#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 12:45:25 2025

@author: h
"""

def skyline(*args):
    heigh=-1
    for height in args:
        if height>heigh:
            heigh=height