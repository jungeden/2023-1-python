#ex4_24
w=input('여러 단어로 이루어진 글을 입력하세요 :')

w = w.replace(',',' ') #공백으로 교체 
w = w.replace('.',' ')
w = w.replace(':',' ')
w = w.split()

a=[]
for j in w: #a에 추가한 뒤 정렬 
    a.append(j)
a.sort()

print(f'정렬 결과 :\n {a}')



