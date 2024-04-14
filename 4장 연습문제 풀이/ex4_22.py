#ex4_22

import datetime 
date = datetime.datetime.now()
y,m,d=str(date.year), str(date.month), str(date.day)

if len(y) == 1: #한 자리 일 경우 
    y = '0'+y
if len(m) == 1:
    m = '0'+m
if len(d) == 1:
    d = '0'+d


print('현재 시간은 {}년 {}월 {}일입니다.'.format(y,m,d))
print('지금 태어난 아이의 주민등록번호 앞자리는 : {}{}{}'.format(date.year%100,m,d))



