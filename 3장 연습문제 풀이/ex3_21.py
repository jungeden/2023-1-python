#ex3_21

n=int(input('숫자를 입력하세요 :'))
if n%2 == 0:
    print(n,'는 소수가 아닙니다')

else:
    for i in range(3,n,2):
        while n%i != 0: #n이 n-1숫자까지 모두 나누어 떨어지지 않으면 
            print(n,'는 소수입니다')
            break
        else:
            print(n,'는 소수가 아닙니다')
            break
    
