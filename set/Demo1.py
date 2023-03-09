import random
import time
import datetime

set1 = {random.random() * 100, time.time_ns(), datetime.datetime.year, datetime.datetime.month, datetime.datetime.day}


print(f"set1:{set1}")

for x in set1:
    print(x)


# print(set1[0])
# del set1[0]