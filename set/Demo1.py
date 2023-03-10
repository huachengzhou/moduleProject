import random
import time
import date_time__

set1 = {random.random() * 100, time.time_ns(), date_time__.datetime.year, date_time__.datetime.month, date_time__.datetime.day}


print(f"set1:{set1}")

for x in set1:
    print(x)


# print(set1[0])
# del set1[0]