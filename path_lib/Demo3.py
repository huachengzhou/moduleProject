import pathlib as pathLib

paths = ('file')

#读取所有文件夹下的文件
fileList = pathLib.Path.iterdir(pathLib.Path.cwd().joinpath(paths))

def ergodicFile(f):
    if f.is_dir():
        print(f"文件夹:{f.absolute()}")
        print(f"文件夹parent:{f.parent}")
        for ff in f.iterdir():
            ergodicFile(ff)
    else:
        print(f.name)
        print(f.absolute())

for f in fileList:
    ergodicFile(f)