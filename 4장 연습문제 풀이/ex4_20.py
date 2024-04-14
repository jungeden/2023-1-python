#ex4_20

def fibo(n): #피보나치 함수 
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return fibo(n-1) + fibo(n-2)

for n in range(0,16): #15까지 출력 
        print('fibo({:3d}) = {:8d}'.format(n,fibo(n)))
