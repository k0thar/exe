#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 16:58:59 2025
@author: h
"""

import requests
import bs4
import regex

r=requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
t=r.text
s=bs4.BeautifulSoup(t,"html.parser")
#1
t=s.select('#firstHeading > span:nth-child(1)')
print(t[0].text)
#2
t=s.select('#mw-panel-toc-list')
for sub in t:
    print(sub.text)
#3
t=r.text
site=str(t)
l=regex.findall('\"h.+svg.png\"', site)
for add in l:
    print(add)
