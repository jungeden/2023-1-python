T=int(input())
A=[]
for _ in range(T):
    a,b=input().split()
    b.replace(f'{b[int(a)-1]}','')
    print(b)
    A.append(b)
print(A)
