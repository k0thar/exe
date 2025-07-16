#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 16:14:14 2025

@author: h
"""

class Task:
    def __new__(cls):
        print('new task created')
    def __init__(self,title="",mtn="",deadline='00000000',priority=-1,subtasks=None,done=False):
        self.mtn=mtn
        self.deadline=deadline
        self.priority=priority
    def done(self):
         return self.done
    def remaining_time(self):
        pass
    def __str__(self):
        return f'title:{self.title} deadline:{self.deadline} {self.remaining_time()} remaining'
        