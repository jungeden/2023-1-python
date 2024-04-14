#7_1
'''
연애 일수 구하기
'''
#1
from datetime import *
t = date(2019, 2, 24) # 연애시작일
today = date.today() 
print(f'춘향이와 몽룡이의 연애 시작일: {t.year}년 {t.month}월 {t.day}일')
print(f'연애 시작일로부터 경과한 날짜:{(today - t).days}일')

print()

#2
import datetime as dt

print(f"춘향이와 몽룡이의 연애 시작일 : 2019년 2월 24일")

first_date = dt.date(2019,2,24)
after_100_days = first_date + dt.timedelta(days=100)
after_200_days = first_date + dt.timedelta(days=200)
after_500_days = first_date + dt.timedelta(days=500)
after_1000_days = first_date + dt.timedelta(days=1000)

print(f"100일 기념일 : {after_100_days.year}년 {after_100_days.month}월 {after_100_days.day}일")
print(f"200일 기념일 : {after_200_days.year}년 {after_200_days.month}월 {after_200_days.day}일")
print(f"500일 기념일 : {after_500_days.year}년 {after_500_days.month}월 {after_500_days.day}일")
print(f"1000일 기념일 : {after_1000_days.year}년 {after_1000_days.month}월 {after_1000_days.day}일")
