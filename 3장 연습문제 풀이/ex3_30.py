#ex3_30

print('1)덧셈\t2)뺄셈\t3)곱셈\t4)나눗셈')
f=int(input('어떤 연산을 원하는지 번호를 입력하세요 :')) #f=연산 번호 
if f not in [1,2,3,4]:
    print('잘못 입력하였습니다.')
else:    
    n=int(input('원하는 숫자 두개를 입력하세요\n')) #n=원하는 숫자1
    m=int(input()) #m=원하는 숫자2
    if f == 1:
        print('{}+{}={}'.format(n,m,n+m))
    elif f == 2:
        print('{}-{}={}'.format(n,m,n-m))
    elif f == 3:
        print('{}*{}={}'.format(n,m,n*m))
    elif f == 4:
        print('{}/{}={}'.format(n,m,n/m))
  
   
