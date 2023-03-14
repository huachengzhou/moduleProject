import pathlib as pathLib
import random
import time
import hashlib

# 判断文件夹是否存在
if pathLib.Path(pathLib.Path.cwd().joinpath('file')).exists():
    pass
else:
    # 不存在则建立文件夹
    pathLib.Path.mkdir(pathLib.Path(pathLib.Path.cwd().joinpath('file')))

for dir in ['a', 'b']:
    if pathLib.Path(pathLib.Path.cwd().joinpath(*('file', dir))).exists():
        pass
    else:
        # 不存在则建立文件夹
        pathLib.Path.mkdir(pathLib.Path(pathLib.Path.cwd().joinpath(*('file', dir))))
    pass
    # 写文件

    fileName1 = str(random.randrange(100, 100000) + random.randrange(100, 100000) + random.randrange(100, 100000))

    paths = ('file', dir, fileName1 + '.txt')

    file1 = pathLib.Path.open(pathLib.Path.cwd().joinpath(*paths), mode="w", encoding="UTF-8")

    strList = []
    for x in range(1, 100, 2):
        strX = str(time.time() * time.time() * x)
        mn = hashlib.md5(strX.encode(encoding='utf-8'))
        strList.append(mn.hexdigest() + '\n')

    print(strList)
    file1.writelines(strList)
    file1.close()

print("所有写入完毕!")
