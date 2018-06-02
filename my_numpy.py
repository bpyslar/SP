#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import numpy as np
import fnmatch, shutil, os, sys
import re
from datetime import datetime, date, time
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#NumPy
def numpy_tasks(np_content):
	length = len(np_content)
	random_list = random.sample(tuple(range(length//2)),length//9)

	print("1st :\n")
	print(np_content[np_content[:,2] >= float(5)])

	print("2nd :\n")
	print(np_content[np_content[:,4] >= float(235)])

	print("3rd :\n")
	print(np_content[(np_content[:,5] <= 20 ) & (np_content[:,5] >= 19) & (np_content[:,7] >= np_content[:,8])])

	print("4th :\n")
	np_content_1 = np_content[random_list,:]
	print(np_content_1)
	mean_arr = np.array((np_content_1[:,6] + np_content_1[:,7] + np_content_1[:,8])/3.)
	print(mean_arr.reshape((len(np_content_1),-1)))

	np_content_1 = np_content[(np_content[:, 1] > time(18,0,0)) & ((np_content[:, 2] +  np_content[:,3]) > float(6)) & (np_content[:, 7] > np_content[:, 6]) &(np_content[:, 7] > np_content[:, 8])]
	print(np_content_1)

def numpy_content_maker(txt_content):
		txt_list = str_format(txt_content).split(";")
		i = 0
		while True:
			if re.search('[a-zA-Z]',txt_list[i]):
				txt_list.pop(i)
				continue
			break
		content = np.array(txt_list)
		length = len(content)
		np_content = content.reshape(int(length/9),9)
		print(np_content)
		return np_content

def str_format(str):
	char_to_order = list(map(ord,list(str)))
	i = 0
	while any(x in char_to_order for x in [10,12,13]):
		if any(char_to_order[i] == x for x in [10,12,13]):
			char_to_order[i] = 59
		i = i + 1
	return "".join(list(map(chr,char_to_order)))

def numpy_content_format(np_content):
	np_content = np_content.transpose()
	stack1 = np_content[0] 
	stack2 = np_content[1]
	stack3 = np_content[2:].astype(float)
	lst = [list(map(int,x.split("/"))) for x in stack1]
	stack1 = np.array([date(x[2],x[1],x[0]) for x in lst])
	lst = [list(map(int,x.split(":"))) for x in stack2]
	stack2 = np.array([time(x[0],x[1],x[2]) for x in lst])
	np_content = np.vstack((stack1,stack2,stack3))
	np_content = np_content.transpose()
	return np_content


def main():
	path = "/Users/bpislar/Лабки/Data Science/Lab_3/household_power_consumption.txt"
	txt_content = str()

	with open(path) as file:
 	   txt_content = file.read()
 	   lines = txt_content.split("\n")
	i = 0
	while i < len(lines):
		if lines[i].find("?") >= 0:
			lines.pop(i)
			continue
		i = i + 1
	txt_content = "\n".join(lines)
	np_content = numpy_content_format(numpy_content_maker(txt_content))
	numpy_tasks(np_content)

if __name__ == "__main__":
	main()