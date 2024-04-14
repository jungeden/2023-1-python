#lab8_1
try:
    a = [10,20,30]
    a[3]
except Exception as e:
    print(f'error : {e}')

try:
    n = int('20%')
except Exception as e:
    print(f'error : {e}')

try:
    a = 100 + '200'
except Exception as e:
    print(f'error : {e}')
