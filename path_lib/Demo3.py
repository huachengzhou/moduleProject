import pathlib as pathLib

paths = ('file')

#读取所有文件夹下的文件
fileList = pathLib.Path.iterdir(pathLib.Path.cwd().joinpath(paths))

for f in fileList:
    if f.is_file():
        print(f.read_text(encoding="utf-8"))
        print(f.name)