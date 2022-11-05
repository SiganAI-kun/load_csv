import pandas as pd

path = 'test.csv'
data = pd.read_csv(path)
# print(data)
#     A   B   C   D
# 0   0   1   2   3
# 1  10  11  12  13
# 2  20  21  22  23
# 3  30  31  32  33

data2 = pd.read_csv(path, header=0)
# print(data2)
#     A   B   C   D
# 0   0   1   2   3
# 1  10  11  12  13
# 2  20  21  22  23
# 3  30  31  32  33

data3 = pd.read_csv(path, header=None)
# print(data3)
#     0   1   2   3
# 0   A   B   C   D
# 1   0   1   2   3
# 2  10  11  12  13
# 3  20  21  22  23
# 4  30  31  32  33

data4 = pd.read_csv(path, header=None, names=('a', 'b', 'c', 'd'))
# print(data4)
#     a   b   c   d
# 0   A   B   C   D
# 1   0   1   2   3
# 2  10  11  12  13
# 3  20  21  22  23
# 4  30  31  32  33

data5 = pd.read_csv(path, header=0, index_col=0)
# print(data5)
#      B   C   D
# A    
# 0    1   2   3
# 10  11  12  13
# 20  21  22  23
# 30  31  32  33

data6 = pd.read_csv(path, usecols=[0, 2])
# print(data6)
#     A   C
# 0   0   2
# 1  10  12
# 2  20  22
# 3  30  32

data6_2 = pd.read_csv(path, usecols=[1])
print(data6_2)
#     B
# 0   1
# 1  11
# 2  21
# 3  31
