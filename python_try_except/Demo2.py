try:
    print(x)
except NameError:
    print("参数 x 没有定义")
except:
    print("Something else went wrong")
