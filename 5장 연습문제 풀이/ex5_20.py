#ex5_20
'''
반복되는 문자 압축
'''
def cp(src:str):
    print(f"src = '{src}'")

    result = ''
    i = 0
    while i < len(src): #갯수
        count = 0
        for j in range(i,len(src)):
            if src[i] != src[j]: #다르면 정지
                break
            count = count + 1
        result += f'{src[i]}{count}'
        i = i + count

    print(f"output = '{result}'")    
cp('aaaabbb')
cp('aaaabccccaaaaacccfg')
cp('')
cp('a')
