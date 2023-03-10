import datetime

str1 = '2022-06-11 11:03'
str2 = '2022-06-11'

# 字符串 匹配格式必须一致 否则会报错
time1 = datetime.datetime.strptime(str2,"%Y-%m-%d")
time2 = datetime.datetime.strptime(str1,"%Y-%m-%d %H:%M")

print(time1)
print(time2)