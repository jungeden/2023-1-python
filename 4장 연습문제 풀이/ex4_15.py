#ex4_15

def my_sort(*nums): #오름차순 정렬 함수 
    a=list(nums)
    a.sort()
    return a

print('결과 : {}'.format(my_sort(45, 3, 4, 56, 5)))
print('결과 : {}'.format(my_sort(9, 8, 7, 6, 5, 4, 3)))
