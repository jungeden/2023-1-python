#lab7_1

import datetime as dt
today = dt.datetime.today()
print(f'오늘의 날짜 : {today.year}년 {today.month}월 {today.day}일')\


if today.hour < 12 :
    print(f'현재 시간 : 오전 {today.hour}시 {today.minute}분 {today.second}초')

else :
    print(f'현재 시간 : 오후 {today.hour-12}시 {today.minute}분 {today.second}초')
