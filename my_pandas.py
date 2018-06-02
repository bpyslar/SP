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

	df_1 = df[(df[col_list[2]] > float(5))]
	print("\n1st:\n")
	print(df_1[col_list[2]])

	df_1 = df[(df[col_list[4]] > float(235))]
	print("\n2nd:\n")
	print(df_1[col_list[4]])

	df_1 = df[( 0 <= df[col_list[5]]) & (df[col_list[5]] <= 205) & (df[col_list[7]] > df[col_list[8]])]
	print("\n3rd:\n")
	print(df_1)
	print(df_1.memory_usage().sum(), "bytes memory usage")

	length = len(df)
	col_length = len(col_list) #df.iloc[int or slice] - selecting by position
	random_list = random.sample(tuple(range(length//2)),length//9)
	df_1 = df.iloc[random_list,:] #df.loc[string or slice] - selecting by label
	print("Average value for the 1st Group: ", df_1[col_list[col_length-3]].mean())
	print("Average value for the 2nd Group: ", df_1[col_list[col_length-2]].mean())
	print("Average value for the 3rd Group: ", df_1[col_list[col_length-1]].mean())

	df_1 = df[(df["Time"] > time(18,0,0)) & (df[col_list[2]] > 6)]
	df_2 = df_1[(df_1[col_list[col_length-2]] > df_1[col_list[col_length-1]]) & (df_1[col_list[col_length-2]] > df_1[col_list[col_length-3]])]
	print("\n4th:\n",df_2)
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