#ex7_5
'''
sin tan cos값 구하기
'''
import math
for i in range(0, 181, 10): #0부터 180까지 
    print(f'sin({i}) = {math.sin(math.radians(i)):.3f}, cos({i}) = {math.cos(math.radians(i)):.3f} , tan({i}) = {math.tan(math.radians(i)):.3f}')
    
