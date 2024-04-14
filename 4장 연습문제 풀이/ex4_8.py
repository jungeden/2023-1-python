#ex4_8

a,b,c,d,e,f=map(int,input('여섯 개의 수를 입력하시오 :').split())
num=[a,b,c,d,e,f]

def mean6(num): #평균 
    return sum(num)/len(num)
def max6(num): #최대 
    return max(num)
def min6(num): #최소 
    return min(num)

print('평균값은 {}'.format(mean6(num)))
print('최댓값은 {}'.format(max6(num)))
print('최솟값은 {}'.format(min6(num)))
