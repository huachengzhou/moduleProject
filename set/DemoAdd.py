import date_time__
import random

nowDate = date_time__.datetime.now()

set2 = {nowDate.year, nowDate.month, nowDate.day}

print(set2)
set2.add("kk")
print(set2)

set3 = {random.random() * 100, "vvv"}
set2.update(set3)

print(set2)
