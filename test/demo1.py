import sys
import os
import pathlib

# 获取父路径
# pathlib.Path(os.getcwd()).parent
# 获取分隔符
# stepWindows = os.path.sep

# print(pathlib.Path.cwd().parent.joinpath("number"))
# path_number = pathlib.Path.cwd().parent.joinpath("module")

path_number = pathlib.Path.cwd().parent.joinpath(*("module","string"))
# path_number2 = pathlib.PureWindowsPath.joinpath()



sys.path.append(path_number)
print(sys.version)
# print(sys.path)
print(pathlib.PureWindowsPath.parent)

print(path_number)

