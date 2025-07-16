#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 16:14:14 2025

@author: h
"""
from datetime import datetime
from decoratorr import *

class Task:
    def __new__(cls,*args, **kwargs):
        """
        TypeError: Task.__new__() takes 1 positional argument but 4 were given
        Update __new__ to handle *args, **kwargs (even if it doesn’t use them):
        

        Parameters
        ----------
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        """
        print("Creating instance")
        return object.__new__(cls)  
    """
    If there is no explicit superclass (i.e., the class does not inherit from another class), Python implicitly inherits from the **base class `object`**.  

### What Happens in `super(A, cls).__new__(cls)` When No Superclass is Defined?
Even if you don't specify a superclass, `A` still inherits from `object` (the root class in Python). So:
```python
class A:  # implicitly inherits from `object`
    def __new__(cls):
        print("Creating instance")
        return super(A, cls).__new__(cls)  # Calls `object.__new__(cls)`
```
- `super(A, cls)` resolves to `object` (since `A`'s parent is `object`).
- `.__new__(cls)` invokes `object.__new__()`, which is the default method for creating a new instance.

### What If You Don’t Use `super()` or `object.__new__`?
If you override `__new__` but **don’t return an instance**, Python will not create the object, and `__init__` **won’t run**:
```python

class A:
    def __new__(cls):
        print("Creating instance (but not really)")
        # No return → implicitly returns None
    
    def __init__(self):
        print("This will never run")

a = A()  # Output: "Creating instance (but not really)"
print(a)  # Output: None (no instance was created)
```
⚠️ **This is usually a bug!** If `__new__` doesn’t return an instance, Python treats it as if the constructor failed.

### How to Fix It?
1. **Explicitly call `object.__new__`** (if you don’t want to use `super()`):
   ```python
   class A:
       def __new__(cls):
           print("Creating instance")
           return object.__new__(cls)  # Directly calls object.__new__
   ```
2. **Use `super()` (recommended)**:
   ```python
   class A:
       def __new__(cls):
           print("Creating instance")
           return super().__new__(cls)  # Python 3: cleaner syntax
   ```

### Key Takeaways:
- Even if you don’t specify a superclass, Python uses `object` as the default.
- `super(A, cls).__new__(cls)` → calls `object.__new__(cls)`.
- If `__new__` doesn’t return an instance, `__init__` is skipped, and `A()` evaluates to `None`.
- Best practice: **Always return an instance in `__new__`** (unless you intentionally want to prevent instantiation).
    
       #this makes 
       """
    #    print('new task created')
    def __init__(self,title="",mtn="",deadline='00000000',priority=-1,subtasks=None,finished=False):
        self.mtn=mtn
        self.deadline=deadline
        self.priority=priority
    @ddone
    def finish(self):
         return self.finished
    @ddone
    def remaining_time(self):
        date= datetime.strptime(self.deadline, '%Y%m%d').date()
        present=date.today()
        print((date-present).days)
        return str((date-present).days)
    @ddone
    def update_proirity(self,pri):
        self.priority=pri
    @ddone
    def __str__(self):
        return f'title:{self.title} deadline:{self.deadline} {self.remaining_time()} remaining'
        