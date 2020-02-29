#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk
import pymysql, os
import json
import time

all_data_kid = {}
all_data_activityid = {}

# 创建主界面
def create_win():
	win = tkinter.Tk()
	win.title('运营活动')
	win.geometry('800x500+300+300')
	return win

# 创建header
def create_header(win):
	columns = ['kid', 'activity_id', 'activity_type', 'open_count', 'status', 'begin_time', 'end_time']
	tree = ttk.Treeview(win, show="headings", height=20, columns=columns)
	tree.pack()

	item_2_name = {}
	item_2_name['kid'] = [80, '王国ID']
	item_2_name['activity_id'] = [100, '活动ID']
	item_2_name['activity_type'] = [100, '活动类型']
	item_2_name['open_count'] = [50, '开启次数']
	item_2_name['status'] = [60, '状态']
	item_2_name['begin_time'] = [180, '开始时间']
	item_2_name['end_time'] = [180, '结束时间']

	for item in columns:
		tree.column(item, width=item_2_name[item][0], anchor='center')
		tree.heading(item, text=item_2_name[item][1])
	
	return tree

# 从数据库获取数据
def get_data_from_sql(kid):
	host = "127.0.0.1"
	user = "root"
	password = "password"
	database = "koh_gamedata_crr"
	conn = pymysql.connect(host, user, password, database=database)
	cursor = conn.cursor()
	cursor.execute("select data from activitytime_ros where kid=" + str(kid))
	row = cursor.fetchone()

	ret_sql = None
	while row:
	    # print(type(row[0]))
	    ret_sql = json.loads(row[0])
	    row = cursor.fetchone()
	conn.close()

	return ret_sql

# 创建全部的数据
def create_all_data(kid, ret_sql):
	all_data_kid[kid] = {}
	for key, value in ret_sql.items():
		key = int(key)
		all_data_kid[kid][key] = {}
		all_data_kid[kid][key]['begintime'] = value['begintime']
		all_data_kid[kid][key]['endtime'] = value['endtime']
		all_data_kid[kid][key]['opencount'] = value['opencount']
		all_data_kid[kid][key]['activityID'] = key
		all_data_kid[kid][key]['kid'] = kid

		if key not in all_data_activityid:
			all_data_activityid[key] = {}

		if kid not in all_data_activityid[key]:
			all_data_activityid[key][kid] = {}

		all_data_activityid[key][kid]['begintime'] = value['begintime']
		all_data_activityid[key][kid]['endtime'] = value['endtime']
		all_data_activityid[key][kid]['opencount'] = value['opencount']
		all_data_activityid[key][kid]['activityID'] = key
		all_data_activityid[key][kid]['kid'] = kid

# 刷新界面
def refreshUI(data, tree):
	x = tree.get_children()
	for item in x:
		tree.delete(item)

	index = 0
	for key, value in data.items():
		begintime = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(value['begintime']))
		endtime = time.strftime("%Y--%m--%d %H:%M:%S", time.localtime(value['endtime']))
		if value['begintime'] > time.time():
			status = "未开启"
		elif value['endtime'] < time.time():
			status = "已结束"
		else:
			status = "开启中"

		tree.insert("", index, values=("王国"+str(value['kid']), value['activityID'], value['activityID'], value['opencount'], status, begintime, endtime))
		index = index + 1

# 按钮回调
def showinfo(entry1, tree):
	param = int(entry1.get())
	if param in all_data_kid:
		refreshUI(all_data_kid[param], tree)
	elif param in all_data_activityid:
		refreshUI(all_data_activityid[param], tree)

# 主函数
def main():
	# 获取数据
	for kid in range(1, 999):
		ret_sql = get_data_from_sql(kid)
		if ret_sql:
			create_all_data(kid, ret_sql)
		else:
			break

	# 创建界面
	win = create_win()
	tree = create_header(win)

	entry1 = tkinter.Entry(win)
	entry1.pack()  
	button = tkinter.Button(win, text="按钮", command=lambda: showinfo(entry1, tree))
	button.pack()

	win.mainloop()

if __name__ == "__main__":
	main()
