#ex4_19

def fibo(n): #피보나치 함수
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return fibo(n-1) + fibo(n-2)

n=int(input('fibo(n)의 n을 입력하세요 :'))
print('fibo({}) = {}'.format(n,fibo(n)))
