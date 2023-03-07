import random


# 随机整数
def randomInt():
    temp = int(random.random() * 1000)
    temp += int(random.uniform(0, 100))
    return temp


# 随机浮点数
def randomFloat():
    temp = 0
    temp += random.random() * 10
    temp *= random.random()
    return temp

print("导入了number模块")

