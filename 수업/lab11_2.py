#lab11_2
import numpy as np
import numpy.random as npr
ndarray=[23,45,67,7,2,30,34,82]
#1
a=np.array([23,45,67,7,2,30,34,82])
print(f'a=array({a})')
print(f'최댓값 : {max(ndarray)}\n최솟값 : {min(ndarray)}\n평균 : {sum(ndarray)/len(ndarray)}')
print()
#2
b=[npr.randint(0,99) for i in range(10)]
print(f'b={b}')
print(f'최댓값 : {max(b)}\n최솟값 : {min(b)}\n평균 : {sum(b)/len(b)}')
print()
#3
c=ndarray+b
print(c)
