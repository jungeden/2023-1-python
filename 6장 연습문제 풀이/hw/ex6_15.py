#ex6_15
'''
슬라이싱을 이용해 하나씩 제거하는 코드 작성하기
'''

tuple = (4,5,2,3,8,1,9,0)
for i in range(len(tuple)):
    print(tuple[:len(tuple)-i])
