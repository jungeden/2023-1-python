#lab 7_2
#1
import datetime as dt
today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.')

xmas = dt.datetime(2025,12,25)
time_gap = xmas - dt.datetime.now()

print(f'2025년 크리스마스까지는 {time_gap.days}일 {time_gap.seconds // 3600}시간 남았습니다.')


#2
import datetime as dt
today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.')

new = dt.datetime(2036,1,1)
time_gap = new - dt.datetime.now()

print(f'2036년 새해까지는 {time_gap.days}일 {time_gap.seconds // 3600}시간 남았습니다.')

#3
import datetime as dt
today = dt.date.today()
print(f'오늘은 {today.year}년 {today.month}월 {today.day}일입니다.')

bd = dt.datetime(2024,2,24)
time_gap = bd - dt.datetime.now()

print(f'2024년 생일까지는 {time_gap.days}일 {time_gap.seconds // 3600}시간 남았습니다.')

