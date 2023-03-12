import pathlib
import re as regexUtils

print(pathlib.Path.cwd())

paths = ('file', 'Demo4.txt')

file1 = pathlib.Path.open(pathlib.Path.cwd().joinpath(*paths), encoding="UTF-8")

list1 = file1.readlines()

str1 = "".join(list1)

print(str1)

# re.match从字符串的起始位置匹配一个模式（从头开始匹配），如果不是起始位置匹配成功的话，match()返回none
# match()要想匹配成功，要匹配的字符串的开头就必须和正则表达式一样，否则匹配不会成功
matchObj = regexUtils.match('.*', str1)

print("______________________________________")

print(matchObj.group())
print(matchObj.groups())
