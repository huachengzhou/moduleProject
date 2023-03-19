var1 = {"a": 1, "b": 2, "c": 3}
var2 = tuple(var1)
print(type(var2))  # <class 'tuple'>
# 将字典中的键（key）转为元组，不包括值（value）
print(repr(var2))  # ('a', 'b', 'c')