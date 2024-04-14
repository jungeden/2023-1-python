a,b=map(int,input().split())
c=int(input())
m=a*60+b+c
a=m//60
b=m%60
if a<=23:
    print(a,b)
else:
    print(a-24,b)

