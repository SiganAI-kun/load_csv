import csv

path = 'test.csv'
with open(path) as f:
    data = f.read()

# print(data)
# print(type(data))
#A,B,C,D
#00,01,02,03
#10,11,12,13
#20,21,22,23
#30,31,32,33

data2 = []
with open(path) as f:
    rows = csv.reader(f)
    # print(rows)
    #<_csv.reader object at 0x0000017463001B40>
    for row in rows:
        data2.append(row)

# print(data2)
#[['A', 'B', 'C', 'D'], ['00', '01', '02', '03'], ['10', '11', '12', '13'], ['20', '21', '22', '23'], ['30', '31', '32', '33']]

path2 = 'test2.csv'

data3 = []
with open(path2) as f:
    rows = csv.reader(f)
    for row in rows:
        data3.append([])
        for i in range(len(row)):
            data3[-1].append(int(row[i]))

# print(data3)
#[[0, 1, 2, 3], [10, 11, 12, 13], [20, 21, 22, 23], [30, 31, 32, 33]]