#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 16:37:12 2025


شرح مسئله:
یک باغ‌وحش قصد دارد یک سیستم مدیریت حیوانات ایجاد کند. شما باید با استفاده از برنامه‌نویسی شی‌گرا (OOP) در پایتون، این سیستم را طراحی کنید.

 
۱. مقدمه بر شی‌گرایی (OOP Introduction)
وظیفه شما:
یک کلاس به نام Animal تعریف کنید که ویژگی‌های زیر را داشته باشد:

    name (نام حیوان)
    species (گونه حیوان)
    age (سن حیوان)
    sound (صدای حیوان)

سپس یک نمونه از این کلاس برای یک "شیر" ایجاد کرده و مشخصات آن را چاپ کنید.

 
۲. ویژگی‌ها و کلاس‌ها (Attributes and Class Keyword)
وظیفه شما:
متد make_sound() را به کلاس Animal اضافه کنید که صدای حیوان را چاپ کند.

 
۳. ویژگی‌های کلاس و متدها (Class Object Attributes and Methods)
وظیفه شما:
یک ویژگی کلاس (zoo_name) اضافه کنید که نام باغ‌وحش را مشخص کند. همچنین، یک متد info() تعریف کنید که مشخصات حیوان را چاپ کند.

 
۴. ارث‌بری و چندریختی (Inheritance and Polymorphism)
وظیفه شما:
یک کلاس جدید به نام Bird از Animal بسازید که یک ویژگی جدید wing_span (اندازه بال) داشته باشد.
همچنین متد make_sound() را بازنویسی کنید تا صدای پرندگان متفاوت باشد.

 
۵. متدهای جادویی (Magic/Dunder Methods)
وظیفه شما:
متد __str__ را در کلاس Animal پیاده‌سازی کنید تا وقتی شیء را چاپ می‌کنید، مشخصات حیوان نمایش داده شود.
conda update anaconda
conda install spyder=6.0.7
@author: h
"""


class Animal():
    def __init__(self,name,species,age,sound,zoo_name):
        self.name=name
        self.species=species
        self.age=age
        self.sound=sound
        self.zoo_name=zoo_name
    def __str__(self):
        return f'name:{self.name} species:{self.species}  age:{self.age}  sound:{self.sound} zoo_name:{self.zoo_name}'
    def make_sound(self):
        print (self.sound)
    def info(self):
        print(f'name:{self.name} species:{self.species}  age:{self.age}  sound:{self.sound}')
        
a=Animal("name", "species", "age", "sound","zoo_name")
print(a.age)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        