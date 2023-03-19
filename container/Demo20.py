var1 = {"name": "tom", "age": 20}
var2 = set(var1)
print(type(var2))  # <class 'set'>
# 将字典中的键（key）转为集合，不包括值（value）
print(repr(var2))  # {'name', 'age'}
