import pandas as pd

# file = open('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/Data.csv', 'r')
# print(file.readlines())

df = pd.read_csv('/Volumes/Data/Sunbeam/2019/Feb/DBDA/stats_R/dataset/Data.csv')
# print(df)
# print(df.head())
# print(df.tail())
# print(df.describe())

# print(df.Salary)
# print(df.Purchased)
# print(df['Person Age'])
# print(df[['Salary', 'Country']])
# print(df['Country'])

# columns = ['Salary', 'Person Age', 'Country']
# print(df[columns])


# print(df.Salary)
# print(df[['Salary', 'Person Age', 'Country']][df.Salary > 61000])
# print(df.Salary[[0, 1]])
# print(df[['Salary', 'Person Age']][df.Salary > 58000])
# print(df[['Salary', 'Person Age']][0:2])
# print(df[['Salary', 'Person Age']])

