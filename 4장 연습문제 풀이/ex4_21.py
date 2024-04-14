#ex4_21

nums=input('주민등록 번호 첫 6숫자 형식 입력 :')

y=int(nums[0:2])
m=int(nums[2:4])
d=int(nums[4:6])

def id_(nums): #생년월일 출력 함수
    if y < 50:
        if y < 10:
            print('200{}년 {}월 {}일'.format(y,m,d))
        else:
            print('20{}년 {}월 {}일'.format(y,m,d))
    else:
        print('19{}년 {}월 {}일'.format(y,m,d))

id_(nums)        
