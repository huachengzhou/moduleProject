import  re as reUtils


txt1 = "China is a great country"
result1 = reUtils.search("^China.*country$",txt1)

print(result1.group())
print(result1.span())
print(result1.end())
print(result1.start())
print(len(txt1))
