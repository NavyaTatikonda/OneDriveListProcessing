import pandas as pd
import sys

df = pd.DataFrame(columns=["A", "B", "C"])
#parts = int(input("Enter the number of day parts:"))
parts=3 #number of rows.
for _ in range(parts):
    dp1 = sys.argv[1]
    dp2 = sys.argv[2]
    dp3 = sys.argv[3]
    df1 = pd.DataFrame(data=[[dp1 ,dp2,dp3]],columns=["A", "B", "C"])
    df = pd.concat([df,df1], axis=0)

df.index = range(len(df.index))
#sys.stdout.write(df)
print(df)
