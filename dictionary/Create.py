

import  random

dicX = {}

for x in range(1,10):
    dicX[str(x)] = random.randrange(int("10") , int("10"+str(x)))

print(dicX)

dic20 = {'a':'zzz'}
print(dic20['a'])
print(dic20.get("a"))