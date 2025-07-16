#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 16:33:52 2025

@author: h
"""
from task import Task
from decoratorr import *
##################Hamashoon type error mikhan

class ToDoList(Task):
    
    def __init__(self,name,tasks=list()):
        self.tasks=tasks
        self.name=name
        #name ro mishe ba file mesle untiteled(n) kard
    @ddone
    def add_tasks(self,nnew):
        self.tasks.append(nnew)
    @ddone
    def delete_tasks(self,wanted):
        self.tasks.remove(wanted)
    @ddone
    def show_undone(self):
        l=list()
        for t in self.tasks:
            if not t.finished:
                l.append(t)
        print(l)
        return l
    @ddone
    def show_all(self):
        for t in tasks:
            print(t)
    @ddone
    def show_done(self):
        l=list()
        for t in self.tasks:
            if t.finished:
                l.append(t)
        print(l)
        return l
    def save_in_csv(self):
        pass
    @ddone
    def __str__(self):
        gist='{self.name}: '
        for t in self.tasks:
            stir=str(t)
            if gist[-2]==':':
                gist='{gist}{stir}'
            gist='{gist}|{stir}'
        return gist
    @ddone
    def clear_empty_tasks(self):
        tmp=Task()
        for t in self.tasks:
            self.tasks.remove(tmp)