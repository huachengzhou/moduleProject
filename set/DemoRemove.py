import datetime
import random


setX = {"0","a"}


for xx in range(1, 300, 5):
    setX.add(random.randrange(int(random.random() * xx), int(random.random() * xx+100)+100))

setX.add("v")

print(setX)

setX.remove("v")

print(setX)