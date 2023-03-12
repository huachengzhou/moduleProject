import  re as regexUtils

print(regexUtils.match('www','www.runoob.com').span()) #在起始位置匹配
print(regexUtils.match('www','www.runoob.com').group())
print(regexUtils.match('com','www.runoob.com')) #不在起始位置匹配
