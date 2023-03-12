import pathlib
import  re as reUtils

paths = ('file', 'Demo2.txt')

file1 = pathlib.Path.open(pathlib.Path.cwd().joinpath(*paths))

list1 = file1.readlines()

for x in list1:
    # print(x)
    pass


file1.close()


str1 = "_".join(list1)

# print(str1)
result1 = reUtils.search("t",str1)
print(result1.group())
print(result1.groups())
