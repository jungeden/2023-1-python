#ex5_4
'''
리스트 순서 바꾸기 
'''
a = [2, 3, 4, 5, 6]
print('a =', a)

rev_a = []
n = a.pop()
for i in range(n+1): #n까지 
    if i < 5:
        rev_a.append(n - i)

print('rev_a =', rev_a)
