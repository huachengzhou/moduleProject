# coding=UTF-8
# 解决 SyntaxError: Non-UTF-8 code starting with '\xe7' in file
import pathlib
import re as regexUtils
import random

str1 = "China is a great country"
x = regexUtils.sub("\\s", str(random.randrange(1,1000)), str1)
y = regexUtils.sub("\\s", "<->", str1)

print(x)
print(y)