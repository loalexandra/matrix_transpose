from numpy import *
n, m = [int(i) for i in input().split()] #2 3
ep = []
for i in range(n):
        ep.append(input().split()) #список, в котором [['1', '2', '3'], ['4', '>
reshaped_arr = array(ep).reshape(n,m)
for i in reshaped_arr.transpose(): #преобразует в массив, делит на столбцы, пер>
        print(' '.join(i))
