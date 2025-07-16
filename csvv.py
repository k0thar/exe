#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 18:46:33 2025

@author: h
"""

import csv

my_file=open('qq.csv',encoding='utf-8')
csv_data=csv.DictReader(my_file)
lines=list(csv_data)
all=0
new_data=dict()
for item in lines:
    l=list(item.values())
    new_data[l[0]]=int(l[1])*int(l[2])
    all=new_data[l[0]]+all
my_file.close()
 #make a new csv file and write the calculated data there
new=open('new.csv','w+',newline='')
"""
writer=csv.writer(new)
writer.writerow(new_data)
"""
new_data['all']=all
writer=csv.writer(new)
writer.writerow(new_data.items())
