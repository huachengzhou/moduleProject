

def divFunction(x,y):
    if y == 0:
        raise Exception("除数不能为0")
    return x / y


print(f" 3 % 0: {divFunction(3,0)}")