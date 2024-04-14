n=int(input('수를 입력하세요 :'))
is_prime = True
for num in range(2,n):
    if n % num == 0: #약수 있으면
        is_prime = False #소수가 아님

print(n,'is prime :',is_prime)        
