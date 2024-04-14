#ex6_17
'''
인구 구성 튜플을 슬라이싱을 이용해 표현하기
'''
population_A = (100,150,230,120,180,100,140,95,81,21,4)
population_B = (300,420,530,420,400,300,40,5,1,1,1)

#1
print(f'마을 A와 B에 보낼 투표용지의 개수는 각각 {sum(population_A[2:])}장과 {sum(population_B[2:])}장입니다.') #20세이상 인구 총 합

#2
print(f'마을 A와 B의 고령화 정도는 각각 {sum(population_A[7:])/sum(population_A):.3f}와 {sum(population_B[7:])/sum(population_B):.3f}입니다.') #나누기

 
