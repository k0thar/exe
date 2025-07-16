#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 16:58:35 2025

@author: h
"""
from task import Task
import csv
##################Hamashoon type error mikhan
##################Hamashoon decorator mikhan


class ToDoList(Task):
    def __new__(cls,*args, **kwargs):
        print("Creating list")
        return object.__new__(cls)
    def __init__(self,name,tasks=list()):
        #name ro mishe ba file mesle untiteled(n) kard
        self.tasks=tasks
        self.name=name
    def add_task(self,nnew):
        self.tasks.append(nnew)
    def delete_task(self,wanted):
        self.tasks.remove(wanted)
    def show_undone(self):
        l=list()
        for t in self.tasks:
            if not t.finished:
                l.append(t)
                print(t)
            else:
                continue
        return l
    def show_all(self):
        for t in self.tasks:
            print(t)
    def show_done(self):
        l=list()
        for t in self.tasks:
            if t.finished:
                l.append(t)
                print(t)
        return l
    def __str__(self):
        gist=f'{self.name}: \n'
        for t in self.tasks:
            stir=str(t)
            if gist[-2]==':':
                gist=f'{gist}{stir}'
            gist=f'{gist}{stir}\n'
        return gist
    def save_in_csv(self):
        nam=input("please write the name of the saved file: ")
        #baraye save as o save adi ham fekr kon
        nam=nam+'.csv'
        open(nam, "a").close()        
        fil = nam
        open(fil, 'w').close()
        with open(fil, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f'name: {self.name}'])
            for task in self.tasks:
                writer.writerow([str(task)])
              
