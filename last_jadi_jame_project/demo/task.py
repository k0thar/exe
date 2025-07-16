#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:10:28 2025

@author: h
"""
from datetime import datetime
import csv

class Task:
    def __new__(cls,*args, **kwargs):
        #print("Creating task")
        return object.__new__(cls)  
    def __init__(self,title="",mtn="",deadline='00000000',priority=-1,subtasks='',finished=False):
        self.mtn = mtn
        self.deadline = deadline
        self.priority = priority
        self.title = title
        self.subtasks = subtasks
        self.finished = finished
    def finish(self):
         return self.finished
    def remaining_time(self):
        date= datetime.strptime(self.deadline, '%Y%m%d').date()
        present=date.today()
        #print((date-present).days,'days remaining')
        return str((date-present).days)
    def update_proirity(self,pri):
        self.priority=pri
    def __str__(self):
        return f'title:{self.title} deadline:{self.deadline} {self.remaining_time()} remaining'

class ToDoList(Task):
    def __new__(cls,*args, **kwargs):
        print("Creating list")
        return object.__new__(cls)
    def __init__(self,name,tasks=list()):
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
        nam=nam+'.csv'
        open(nam, "a").close()        
        fil = nam
        open(fil, 'w').close()
        with open(fil, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f'name: {self.name}'])
            for task in self.tasks:
                writer.writerow([str(task)])
            #writer.writerows(self.__str__())

tt=Task('tt',deadline='19340212',priority=2)
tt1=Task('ttdfkl',deadline='19340512',priority=9)
tt6 = Task("Complete project", "MTN001", "20231215", 3, ["research", "coding"], False)
tt2 = Task("Write documentation", "MTN002", "20231130", 2, "", True)
tt3 = Task("Team meeting", "MTN003", "20231120", 1, ["prepare slides"], False)
tt4 = Task("Code review", "MTN004", "20231125", 2, ["frontend", "backend"], False)
tt5 = Task("Deploy to production", "MTN005", "20231201", 4, ["testing", "approval"], False)

vist=[tt,tt1]
todo=ToDoList('asb',vist)
todo.add_task(tt2)
todo.add_task(tt3)
todo.add_task(tt4)
todo.add_task(tt5)
todo.add_task(tt6)
todo.save_in_csv()
#print(len(todo.tasks))
print(todo)
#todo.show_all()
#print(len(todo.tasks))
#todo.delete_task(tt)
#print()
#print(tt)
