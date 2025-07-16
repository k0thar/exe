#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 10:36:33 2025

@author: h
"""

import json

import requests

api_url='http://api.open-notify.org/iss-now.json?callback=?'
response=requests.get(api_url)
json_data=response.json()
for per in json_data:
    print(per['name'])

print(response)