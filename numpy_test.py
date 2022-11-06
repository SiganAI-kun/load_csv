import numpy as np

path = 'test2.csv'

data = np.loadtxt(path, delimiter=',')
# print(data)
#[[ 0.  1.  2.  3.]
# [10. 11. 12. 13.]
# [20. 21. 22. 23.]
# [30. 31. 32. 33.]]

data2 = np.loadtxt(path)
# print(data2)
# ValueError: could not convert string '00,01,02,03' to float64 at row 0, column 1.