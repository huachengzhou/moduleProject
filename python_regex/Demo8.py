# coding=UTF-8
# 解决 SyntaxError: Non-UTF-8 code starting with '\xe7' in file
import pathlib
import re as regexUtils


paths = ('file', 'Demo8.txt')

file1 = pathlib.Path.open(pathlib.Path.cwd().joinpath(*paths), encoding="UTF-8")

list1 = file1.readlines()

str1 = "".join(list1)


rule1 = "\\d+....."

compile1 = regexUtils.compile(rule1,regexUtils.X)

matches = compile1.finditer(str1)
# compile1.findall()
# compile1.match()
# compile1.search()
# compile1.split()
# compile1.sub()

for x in matches:
    print(x.group())
