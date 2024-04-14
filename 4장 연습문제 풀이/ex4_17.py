#ex4_17

def sum_range(n1,n2): #합 함수 
    n=n1
    for i in range(n1+1,n2+1):
        n = n + i
    return n
        
print('{}에서 {}까지의 정수의 합 : {}'.format(10,20,sum_range(10,20)))
print('{}에서 {}까지의 정수의 합 : {}'.format(40,100,sum_range(40,100)))

        
