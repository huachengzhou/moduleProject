import date_time__
import random

nowDate = date_time__.datetime.now()

setX = {"0"}

# 集合不能空 否则add会出问题的
setX.add("hh")

setX.add(random.random())
setX.add(random.randrange(int(random.random() * 100), int(random.random() * 100)+100))
setX.add(random.randrange(int(random.random() * 99), int(random.random() * 100)+100))
setX.add(random.randrange(int(random.random() * 98), int(random.random() * 100)+100))
setX.add(random.randrange(int(random.random() * 97), int(random.random() * 100)+100))
setX.add(random.randrange(int(random.random() * 96), int(random.random() * 100)+100))
setX.add(random.randrange(int(random.random() * 95), int(random.random() * 100)+100))

print(setX)
print(setX.pop())


print(setX)
