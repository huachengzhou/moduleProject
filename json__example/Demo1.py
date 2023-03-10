import json

# 一些 JSON:
x = '{ "name":"Bill", "age":63, "city":"Seatle"}'

# 解析 x:

y = json.loads(x)

print(f"json 类型 {type(y)}")
print(y)
