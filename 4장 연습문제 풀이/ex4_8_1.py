#ex4_8_1
num=[a,b,c,d,e,f]
num=map(int,input('여섯 개의 수를 입력하시오 :').split())

def mean3(num):
    return sum(num)/len(num)
def max3(num):
    if a>b and a>c:
        if a>d and a>e:
            if a>f:
                return a
            else:
                return f
        else:
            if a>d: 
                
    if d>e:
        if d>f:
            return d
        elif :
            return c
    else:
        if b>c:
            return b
        else:
            return c

def min3(a,b,c):
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
print('평균값은 {}'.format(mean3(num)))
print('최댓값은 {}'.format(max3(num)))
print('최솟값은 {}'.format(min3(num)))

