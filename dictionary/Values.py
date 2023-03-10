import random


dicX = {}

for x in range(1,10):
    dicX[str(x)] = random.randrange(int("10") , int("10"+str(x)))

print(dicX)

print(dicX.values())


for x in dicX.values():
    print(x)


print(dicX.items())