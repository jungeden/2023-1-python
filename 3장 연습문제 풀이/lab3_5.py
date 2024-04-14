#lab3_5
#1.
s=int(input('자동차의 속도를 입력하세요(단위 : km/h):'))
if s>=100:
    print('고속')
elif 60<=s<100:
    print('중속')
else:
    print('저속')

#2.
m=int(input('미세먼지 농도를 입력하세요(단위 : microgram/m^3):'))
if 0<=m<=15:
    print('좋음')
elif 16<=m<=35:
    print('보통')
elif 36<=m<=75:
    print('나쁨')
else:
    print('매우 나쁨')
