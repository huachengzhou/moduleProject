from my_package.number.util import *

import my_package.string.util as stringUtils

# 定义一个列表
aList = []

# 填充元素
for i in range(0,20):
    if i % 2 == 0:
        aList.append(i)
    aList.append(stringUtils.randomString(20))

# 获取长度
print("len:",len(aList))

# 获取第一个
print("first element:",aList[0])

# 获取最后一个元素
print("last element:",aList[-1])

# 获取倒数第二个元素
print("last element:",aList[-2])


# 打印一下
print(aList)

# 删除第一个
del aList[0]

print(aList)



