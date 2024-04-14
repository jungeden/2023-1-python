#ex4_18

a = int(input('범위의 시작 정수 :'))
b = int(input('범위의 마지막 정수 :'))
c=b
while True:
    n=0
    for i in range(a,b+1): #a부터 b까지 
        if c%i == 0: #b로 나누어 떨어지면
           n=n+1
    if n == len(range(a,b+1)):
        print(f'{a}에서 {b}까지의 정수들의 최소공배수는 : {c}')
        break
    c=c+1    
