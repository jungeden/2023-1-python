#ex6_25
'''
딕셔너리를 활용해 검색할 수 있는 코드 구현하기
'''
print('사전 프로그램 시작... 종료는 q를 입력')
dictionary = {}
while True :
    cmd = input('$ ')
    if cmd == 'q':
        break
    elif cmd[0] == '<':
        cmd = cmd.replace('< ', '')
        f_word, b_word = cmd. split(':')
        dictionary[f_word] = b_word
    elif cmd[0] == '>':
        cmd = cmd.replace('> ', '')
        if cmd in dictionary.keys(): #있으면 
            print(dictionary[cmd])
        else: #없으면 
            print(f'{cmd}가 사전에 없습니다.')
    else:
        print('입력오류가 발생했습니다.')
print('사전 프로그램을 종료합니다.')
