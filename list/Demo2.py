from my_package.number.util import *

import my_package.string.util as stringUtils

# 定义一个列表
aList = []

# 填充元素
for i in range(0,5):
    if i % 2 == 0:
        aList.append(i)
    aList.append(stringUtils.randomString(20))



# 打印一下
print(aList)

aList.insert(len(aList),"insert")



# 打印一下
print(aList)