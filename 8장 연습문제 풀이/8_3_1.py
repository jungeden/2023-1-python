#8_3
'''
hello.txt 파일을 텍스트 편집기를 이용해 작성하기
'''
#(1)
f=open('hello.txt','r')
print('hello.txt 파일 :')
a=f.read()
print(a)
f.close()
