#ex7_10
'''
사용자가 랜덤한 숫자 맞추는 프로그램 만들기
'''
import random

x = random.randint(1, 20)
n = 0
while True:
    num = int(input("1부터 20까지의 숫자를 입력하세요: "))
    n += 1
    if x>num: #크면 
        print(num, '보다 큽니다.')
    elif x<num: #작으면 
        print(num, '보다 작습니다.')
    else:
        print("정답입니다!")
        if n <= 3:
            print("{}번 만에 맞춘 당신은 천재!".format(n))
        elif n <= 6:
            print("{}번 만에 맞추셨네요. 잘했어요^^".format(n))
        else:
            print("{}번 만에 맞추다니 쩝쩝...".format(n))
