#ex4_4

def mile2km(m): #마일을 킬로미터로 변환 
    return m*1.61

for i in range(1,6):
    print('{}마일 = {} 킬로미터'.format(i,mile2km(i)))
    
