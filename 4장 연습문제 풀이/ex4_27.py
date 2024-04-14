#ex4_27

nums = float(input('1보다 작고 0보다 큰 소수를 입력하세요 :'))

def unit_fraction(frac):
    n=int(1/frac) #입력받은 소수
    a=1/n #근접한 분수
    b=1/(n+1)

    if (a-frac)**2 < (b-frac)**2: #뭐가 더 가까운지 비교 
        return n
    else:
        return n+1


print(f'가장 가까운 단위분수는 1/{unit_fraction(nums)}이며,\
이 값은 {1/unit_fraction(nums)}입니다.')
