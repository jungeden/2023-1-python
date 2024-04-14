#리스트 초기화
primes = []
is_prime = True
for n in range(2,101):
    is_prime = True
    for num in range(2,n):
        if n % num == 0: 
            is_prime = False

    if is_prime:   #소수일 경우 primes라는 리스트에 추가한다.
        primes.append(n) #append() 메소드는 리스트에 n을 추가함.

print(primes)
        
