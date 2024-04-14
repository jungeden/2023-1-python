#ex4_6

def cel2fah(cel): #섭씨를 화씨로 변환 
    return (9/5)*cel+32

for i in range(10,51,10):
    print('섭씨 {}도 = 화씨 {}도'.format(i,cel2fah(i)))
