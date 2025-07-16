# -*- coding: utf-8 -*-

from datetime import datetime
##################Hamashoon type error mikhan
##################Hamashoon decorator mikhan

class Task:
    def __new__(cls,*args, **kwargs):
        print("Creating instance")
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
        print((date-present).days,'days remaining')
        return str((date-present).days)
    def update_proirity(self,pri):
        self.priority=pri
    def __str__(self):
        return f'title:{self.title} deadline:{self.deadline} {self.remaining_time()} remaining'

