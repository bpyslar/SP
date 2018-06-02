#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import pandas as pd
import fnmatch, shutil, os, sys
import re
from datetime import datetime, date, time
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#Pandas
def pandas_tasks(df):
	col_list = df.columns

	print("\n1st:\n")
	df_1 = df[(df[col_list[2]] > float(5))]
	print(df_1[col_list[2]])

	print("\n2nd:\n")
	df_1 = df[(df[col_list[4]] > float(235))]
	print(df_1[col_list[4]])

	print("\n3rd:\n")
	df_1 = df[ (19 <= df[col_list[5]])&(df[col_list[5]] <= 20) & (df[col_list[7]] > df[col_list[8]])]
	print(df_1)
	print(df_1.memory_usage().sum(), "bytes memory usage")

	print("\n4th:\n")
	length = len(df)
	#df.loc[string or slice] - selecting by label
	random_list = random.sample(tuple(range(length//2)),length//9)
	#range - aryphmetic progression, list from x to y(!) with z step  
	df_1 = df.iloc[random_list,:] #df.iloc[int or slice] - selecting by position
	print(df_1)
	print("Average value for the 1st Group: ", df_1[col_list[6]].mean())
	print("Average value for the 2nd Group: ", df_1[col_list[7]].mean())
	print("Average value for the 3rd Group: ", df_1[col_list[8]].mean())

	print("\n5th:\n")
	df_1 = df[(df["Time"] > time(18,0,0)) & (df[col_list[2]] > 6)]
	df_2 = df_1[(df_1[col_list[7]] > df_1[col_list[8]]) & (df_1[col_list[7]] > df_1[col_list[6]])]
	print(df_2)
	print("First half:\n")
	firsthalf_list = list(tuple(range(len(df_2)//2)))
	df_2_firsthalf = df_2.iloc[firsthalf_list,:]
	print(df_2_firsthalf)
	print("Second half:\n")
	secondhalf_list = list(tuple(range(len(df_2)//2,len(df_2))))
	df_2_secondhalf = df_2.iloc[secondhalf_list,:]
	print(df_2_secondhalf)
	return col_list



def pandas_content_format(df):
	df.apply(pd.to_numeric,errors = 'ignore')
	type_date = type(date(12,12,12))

	if not type(df["Date"][0]) == type_date:
		lst = [list(map(int,x.split("/"))) for x in list(df["Date"])]
		df['Date'] = [date(x[2],x[1],x[0]) for x in lst]

	if not type(df["Time"][0]) == type(time(0,0,0)):
		lst = [list(map(int,x.split(":"))) for x in list(df["Time"])]
		df['Time'] = [time(x[0],x[1],x[2]) for x in lst]
	
	return df


def pandas_content_maker(txt_content):
	txt_content_ = StringIO(txt_content)
	df = pd.read_csv(txt_content_,sep = ';')
	txt_content_.close()
	df = pandas_content_format(df)
	return df


def main():
	path = "/Users/bpislar/Лабки/Data Science/Lab_3/household_power_consumption.txt"
	txt_content = str()

	with open(path) as file:
		txt_content = file.read()
	lines = txt_content.split("\n")

	i  = 0

	while i < len(lines):
		if lines[i].find("?") >= 0:
			lines.pop(i)
			continue
		i = i + 1

	txt_content = "\n".join(lines)
	pd_content = pandas_content_format(pandas_content_maker(txt_content))
	pandas_tasks(pd_content)

if __name__ == "__main__":
	main()