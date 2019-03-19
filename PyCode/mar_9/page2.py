import numpy as np
import pandas as pd

df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/Data.csv')
print(df)
# print(df.iloc[1, 1])
# print(df.iloc[1, 0:2])
# print(df.iloc[0:2, 0:3])
# print(df.iloc[:, 0:3])
# print(df.iloc[:, :])
# print(df.iloc[:, 0].values)
# print(df.iloc[:, :].values)
print(df.iloc[:, 3].values)
