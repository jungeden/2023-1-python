#윤년 판별하기

y=int(input('연도를 입력하세요 :'))
is_leap_year=((y%4==0) and (y%100!=0) or (y%400==0))
print(y,'년은 윤년입니까?',is_leap_year)
