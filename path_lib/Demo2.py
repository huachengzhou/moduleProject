import pathlib as pathLib
import random
import time
import hashlib

fileName1 = str(random.randrange(100, 100000) + random.randrange(100, 100000) + random.randrange(100, 100000))

paths = ('file', fileName1 + '.txt')

file1 = pathLib.Path.open(pathLib.Path.cwd().joinpath(*paths), mode="w", encoding="UTF-8")

strList = []
for x in range(1, 100, 2):
    strX = str(time.time() * time.time() * x)
    mn = hashlib.md5(strX.encode(encoding='utf-8'))
    strList.append(mn.hexdigest() + '\n')

print(strList)
file1.writelines(strList)


