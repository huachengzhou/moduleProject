from my_package.number.util import *
import time
import my_package.string.util as stringUtils

tuple1 = (
    stringUtils.randomString(20), stringUtils.randomString(20), stringUtils.randomString(20), randomInt(),
    randomFloat())

print(tuple1)

tupleX = (time.time(), time.time_ns())
print(tupleX)

tupleIndex = (2, 3, 'a', 'c')
print(f"倒数第一项:{tupleIndex[-1]}")
print(f"倒数第二项:{tupleIndex[-2]}")
print(f"第一项:{tupleIndex[0]}")


betweenTuple = ('a','k','4','7')
print(f"a属于元组:{'a' in betweenTuple}")
print(f"b不属于元组:{'a' in betweenTuple}")
print(f"元组长度:{len(betweenTuple)}")
