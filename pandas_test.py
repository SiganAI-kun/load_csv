import pandas as pd

path = 'test.csv'
data = pd.read_csv(path)
# print(data)

data2 = pd.read_csv(path, header=0)
# print(data2)

data3 = pd.read_csv(path, header=None)
# print(data3)

data4 = pd.read_csv(path, header=None, names=('a', 'b', 'c', 'd'))
# print(data4)

data5 = pd.read_csv(path, header=0, index_col=0)
# print(data5)

data6 = pd.read_csv(path, usecols=[0, 2])
# print(data6)

data6_2 = pd.read_csv(path, usecols=[1])
print(data6_2)