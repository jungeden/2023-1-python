#ex5_21
'''
5.20번 문제에서 압축한 문자열의 압축을 해제해 복원하기
'''
src = 'a2b3c6a2c3f1g1'
print("src = 'a2b3c6a2c3f1g1'")
for i in range(int(len(src) / 2)):
    print(src[i*2]*int(src[i*2+1]), end='') #복구
