var1 = {"aa": 1, "bb": 2, "cc": 3}
var2 = list(var1)
# 将字典中的键（key）转为列表，不包括值（value）
print(var2)  # ['aa', 'bb', 'cc']
print(type(var2))  # <class 'list'>
