import random
import math

fun1 = lambda a, b: print(a + b)

fun1(random.randrange(1, 100), random.randrange(1, 100))


def fun (x = 0,y = 0):
    return lambda :  math.pow(x,2)+math.pow(y,2)


value1 = fun(3,4)

print(value1())


print(math.pow(3,2)+math.pow(4,2))
print(math.pow(math.pow(3,2)+math.pow(4,2),0.5))
print(math.sqrt(math.pow(3,2)+math.pow(4,2)))