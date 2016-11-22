from numpy import *
n, m = input().split() #2 3
ep = []
for i in range(int(n)):
        ep.append(input().split()) #список, в котором [['1', '2', '3'], ['4', '5', '6']]
for i in array(ep).reshape(int(n), int(m)).transpose(): #преобразует в массив, делит на столбцы, переворачивает
        print(' '.join(i), end='\n')