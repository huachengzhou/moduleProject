
try:
    x1 = 2 / 0
except:
    print("异常 除数为0")
finally:
    print("不管抛出异常与否都会执行")