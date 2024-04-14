#ex3_24

num = []

n=int(input('숫자를 입력하세요 :'))
for i in range(1,n+1): #1부터 입력받은 수 까지 
    num.append((1/i)**2)

print('결과는',sum(num),'입니다.') 

