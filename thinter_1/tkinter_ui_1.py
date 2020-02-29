#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from tkinter import * 
root = Tk()
li     = ['C', 'python', 'php', 'html', 'SQL', 'java']
listb  = Listbox(root)
for item in li:
    listb.insert(0, item)
 
listb.pack()
root.mainloop()
