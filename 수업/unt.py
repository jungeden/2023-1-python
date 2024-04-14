N,M=map(int,input().split())
P=[]
Q=[]
r=[]
for _ in range(N):
    p=input()
    P.append(p)
for _ in range(M):
    q=input()
    Q.append(q)
    Q=' '.map(join(int,Q))
for i in Q:
    if type(i) != "<class 'int'>":
        print(i)
        for j in P:
            if i == j:
                r.append((P.index(j))+1)
    elif type(i) == "<class 'int'>":
        r.append(P[i-1])

print(r,Q)

  if n<6666:
        n=666
        a=0
        n=n+(1000*a)
        A.append(n)
        a+=1
    if 5666<=n<7000:
        n=6660
        a=0
        n=6660+(a)
        A.append(n)
        a+=1
    if 6669<=n<



            if (N%b)%a == 0:
        print(f'{(N//b)+(N%b//a)}')
    else:
print(f'{(N//b)+(N%b//a)}')



N=int(input())
a=3
b=5
A=[]
if N//b>0: 
    for i in range(1,N):
        if N%(b*i)%a == 0:
            print(f'{(N//(b*i))+(N%b//a)}')
            break
        elif N%a == 0:
            print(f'{N//a}')
            break
        else:
            print(-1)
            break
elif N%b == 0:
    print(f'{N//b}')

N=int(input())
a=3
b=5
A=[]
if N//b>0:
    for i in range(1,N):
        if N%(b*i)%a == 0:
            print(f'{(N//(b*i))+(N%b//a)}')
            break
        elif N%a == 0:
            print(f'{N//a}')
            break
        elif N%(a*i)%b == 0:
            print(f'{N//(a*i)+(N%a//b)}')
            break
        else:
            print(-1)
elif N%b == 0:
    print(f'{N//b}')  
