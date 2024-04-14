#lab3_3
#1.
g_s=int(input('게임 점수를 입력하시오 :'))
print('game_score =',g_s)
if g_s>=1000:
    print('고수입니다.')

else:
    print('입문자입니다.')

#2.
num_a=int(input('한 정수를 입력하시오 :'))
num_b=int(input('다른 정수를 입력하시오 :'))
if num_a != num_b:
    print('두 값이 일치하지 않습니다.')
    
else:
    print('두 값이 일치합니다.')

#3.
#(1)
q=int(input('당신은 성인인가요(성인이면 1, 미성년이면 0):'))
if q==0:
    print('당신은 미성년자입니다.')
#(2)
if q==1:
    q_2=int(input('결혼을 하셨나요(기혼이면 1, 미혼이면 0):'))
    if q_2==1:
        print('당신은 결혼한 성인입니다.')
    if q_2==0:
        print('당신은 결혼하지 않은 성인입니다.')
