#ex4_9

num=list(map(int,input('정수 여러 개 입력하시오 :').split()))
a=[]
for i in num:
    a.append(i)
    
def mean_of_n(a): #평균 
    return sum(a)/len(a)
def max_of_n(a): #최대 
    return max(a)
def min_of_n(a): #최소 
    return min(a)

print('평균값은 {}'.format(mean_of_n(a)))
print('최댓값은 {}'.format(max_of_n(a)))
print('최솟값은 {}'.format(min_of_n(a)))
