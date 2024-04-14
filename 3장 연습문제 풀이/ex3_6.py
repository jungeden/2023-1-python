#ex3_6

a,b,c=map(int,input('세 정수를 입력하시오 :').split()) #세 정수 

if a>b:
    if b>c:
        print(c,b,a)
    else:
        if a>c:
            print(b,c,a)
        else:
            print(b,a,c)
else:
    if a>c:
        print(c,a,b)
    else:
        if c>b:
            print(a,b,c)
        else:
            print(a,c,b)
 
