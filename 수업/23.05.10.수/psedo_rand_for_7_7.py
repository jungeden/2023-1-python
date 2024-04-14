#pseudo_rand_for

def pseudo_rand(x):
    new_x= (1103515245*x+12345)%(2**31)
    return new_x

x = 20402
for _ in range(5):
    x=pseudo_rand(x)
    print(x)
