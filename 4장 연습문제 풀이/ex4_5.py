#ex4_5

def inch2cm(inch): #인치를 센티미터로 변환 
    return inch*2.54

for i in range(1,6):
    print('{}인치 = {}센티미터'.format(i,inch2cm(i)))
