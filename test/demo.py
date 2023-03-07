import sys
import os
import pathlib

# 获取父路径
# pathlib.Path(os.getcwd()).parent
# 获取分隔符
# stepWindows = os.path.sep

# print(pathlib.Path.cwd().parent.joinpath("number"))


path_number = pathlib.Path.cwd().parent.joinpath("my_module")

# path_number = pathlib.Path.cwd().parent.joinpath(*("my_module","string"))



# sys.path.append(path_number)



str1 = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
sys.path.append(str1+"\\my_module")


# print(sys.version)
# print(sys.path)
print(path_number)
print(str1+"\\my_module")

import Demo

