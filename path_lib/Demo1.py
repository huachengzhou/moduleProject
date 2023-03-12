import pathlib as pathLib

paths = ('file', 'f.txt')

file1 = pathLib.Path.open(pathLib.Path.cwd().joinpath(*paths), mode="r+", encoding="UTF-8")
list1 = file1.readlines()
for x in list1:
    print(x)
file1.close()
