import datetime

# timedelta 就只有这几个参数  要是年和月换成天或者周就是 python3.6
# def __new__(cls, days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0)

date1 = datetime.datetime(2019, 10, 1)
print(date1)

# 增加天
# datetime.timedelta
date1 = date1 + datetime.timedelta(days=1)

print(date1)

# 增加小时
date1 = date1 + datetime.timedelta(hours=1)
print(date1)

# 增加分钟
date1 = date1 + datetime.timedelta(minutes=2)
print(date1)

# 减少分钟
date1 = date1 + datetime.timedelta(minutes=-1)
print(date1)

# 增加秒
date1 = date1 + datetime.timedelta(seconds=20)
print(date1)

# 增加毫秒
date1 = date1 + datetime.timedelta(milliseconds=10)
print(date1)

# 增加周
date1 = date1 + datetime.timedelta(weeks=1)
print(date1)

# 增加一年
# 闰年366天 , 平年365天 公历年份是整百数的，必须是400的倍数才是世界闰年（如2000是世纪闰年，1900不是世纪闰年
if (date1.year + 1) % 400 == 0:
    date1 = date1 + datetime.timedelta(days=366)
    print("闰年")
else:
    print("平年")
    date1 = date1 + datetime.timedelta(days=365)

print(date1)


# 计算给定月份的总天数
def computeMonthDay(monthMin, monthMax, year):
    tempDay = 0
    day2Month = 0
    if year % 400 == 0:
        day2Month = 29
    else:
        day2Month = 28
    day31List = [1, 3, 5, 7, 8, 10, 12]
    day30List = [4, 6, 9, 11]
    for x in range(monthMin + 1, monthMax + 1):
        print(f"x:{x}")
        if x == 2:
            tempDay += day2Month
        elif x in day31List:
            tempDay += 31
        elif x in day30List:
            tempDay += 30
    return tempDay


# 在当前日期任意增加几月 但是没有超过12
month1 = 12
if month1 + date1.month <= 12:
    date1 = date1 + datetime.timedelta(days=computeMonthDay(date1.month, date1.month + month1, date1.year))
else:
    month2 = 12 - month1
    date1 = date1 + datetime.timedelta(days=computeMonthDay(date1.month, date1.month + month2, date1.year))
    date1 = date1 + datetime.timedelta(days=computeMonthDay(0, month1 - month2, date1.year))

print(date1)

# 任意月份
# month2 输入的任意月份
month2 = 31
# month2X 实际添加的月份
month2X = 0
# 实际添加的年份
year1 = 0
if month2 >= 12:
    year1 = int(month2 / 12)
    month2X = month2 - year1 * 12
else:
    year1 = 0
    month2X = month2 - year1 * 12


print(f"year:{year1} ; month2X:{month2X}")

if year1 > 0:
    for x in range(0,year1):
        if (date1.year + 1) % 400 == 0:
            date1 = date1 + datetime.timedelta(days=366)
        else:
            date1 = date1 + datetime.timedelta(days=365)
else:
    if month2X + date1.month <= 12:
        date1 = date1 + datetime.timedelta(days=computeMonthDay(date1.month, date1.month + month2X, date1.year))
    else:
        month2 = 12 - month2X
        date1 = date1 + datetime.timedelta(days=computeMonthDay(date1.month, date1.month + month2, date1.year))
        date1 = date1 + datetime.timedelta(days=computeMonthDay(0, month2X - month2, date1.year))

# 结束

print(date1)