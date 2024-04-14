#ex4_7

a,b,c=map(int,input('세 수를 입력하시오 :').split())

def mean3(a,b,c): #평균 
    return (a+b+c)/3
def max3(a,b,c): #최대 
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c

def min3(a,b,c): #최소 
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c
print('{},{},{}의 평균값은 {}'.format(a,b,c,mean3(a,b,c)))
print('{},{},{}의 최댓값은 {}'.format(a,b,c,max3(a,b,c)))
print('{},{},{}의 최솟값은 {}'.format(a,b,c,min3(a,b,c)))
            
    
