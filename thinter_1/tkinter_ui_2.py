#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk
win = tkinter.Tk()
win.title("my_tkinter_ui")
win.geometry("400x400+200+50")

# # 创建文本
# label = tkinter.Label(win, 
# text="this is a word",
# bg="pink", fg="red",
# font=("黑体", 20),
# width=20,
# height=10,
# wraplength=100,
# justify="left",
# anchor="ne"
# )

# label.pack()


# 创建按钮
# def func():
# 	print("aaaaaaaaaaaaaaaaaaaaaaa")
# button1 = tkinter.Button(win, text="按钮", command=func, width=10, height=10)
# button1.pack()

# 密文显示
# entry1 = tkinter.Entry(win, show="*") # show="*" 可以表示输入密码
# entry1.pack()

# 创建一个listbox，添加几个元素
# lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
# lb.pack()

# for item in ["good", "nice", "handsome", "aaa", "bbb", "ccc", "ddd"]:
#     # 按顺序添加
#     lb.insert(tkinter.END, item)


# 菜单条
# menubar = tkinter.Menu(win)
# win.config(menu=menubar)

# def func():
# 	print("**********")

# # 创建一个菜单选项
# menu1 = tkinter.Menu(menubar, tearoff=False)

# # 给菜单选项添加内容
# for item in ['python','c','java','c++', 'c#','php','B','退出']:
# 	if item == '退出':
# 		# 添加分割线
# 		menu1.add_separator()
# 		menu1.add_command(label=item, command=win.quit)
# 	else:
# 		menu1.add_command(label=item, command=func)

# # 向菜单条上添加菜单选项
# menubar.add_cascade(label='语言', menu=menu1)


# 表格
tree = ttk.Treeview(win)
tree.pack()

# 定义列
tree["columns"] = ("name", "age", "height", "weight")
# 设置列，列还不显示
# tree.column("name", width=100)
# tree.column("age", width=100)
# tree.column("height", width=100)
# tree.column("weight", width=100)

# 设置表头
tree.heading("name", text="姓名")
tree.heading("age", text="年龄")
tree.heading("height", text="身高")
tree.heading("weight", text="体重")

# 添加数据
tree.insert("", 0, values=("小郑","34","177cm","70kg"))
tree.insert("", 1, values=("小张","43","188cm","90kg"))


win.mainloop()