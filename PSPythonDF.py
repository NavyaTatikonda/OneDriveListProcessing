import fileinput
import pandas as pd

#empty df
#column_names = ["a", "b", "c"]
#df = pd.DataFrame(columns = column_names)
#print(df)

#for line in fileinput.input():
#    pass
df = pd.DataFrame(columns=["Day-Part", "Start Time", "End Time"])
#user created dataframe------using INPUT
for _ in range(2):

	dp = input("Enter Part of the Day ")
	st = input("enter")
	et = input("Enter ")
	df1 = pd.DataFrame(data=[[dp,st,et]],columns=["Day-Part", "Start Time", "End Time"])
	df = pd.concat([df,df1], axis=0)

df.index = range(len(df.index))
print(df)
