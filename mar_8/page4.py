import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(s1)
# print(s1[1])
# print(s1[4])

# print(s1[[1, 4]])

# indexValues = [1, 2, 3]
# print(s1[indexValues])

print(s1[0:2])
print(s1[1:4])
print(s1[5:])
print(s1[:5])
print(s1[:])
print(s1)

# print(s1[-1])
