import pathlib as pathLib
import os as osUtils

fileDir = pathLib.Path.cwd().joinpath(('DemoOther.py'))

print(f"返回电脑用户的目录: {fileDir.home()}")
print(f"返回文件当前所在目录: {fileDir.cwd()}")
print(f"返回文件: {fileDir.parts}")
print(f"返回根目录: {fileDir.anchor}")
print(f"返回根目录: {fileDir.root}")
print(f"返回父级目录: {fileDir.parent}")
print(f"返回所有上级目录的列表: {fileDir.parents}")
print(f"后缀: {fileDir.suffix}")
print(f"返回文件后缀列表: {fileDir.suffixes}")
print(f"获得文件属性: {fileDir.stat()}")
print(f"返回文件名+文件后缀: {fileDir.name}")
print(f"返回文件名: {fileDir.stem}")
print(f"获得文件路径: {str(fileDir)}")
print(f"获得文件路径base: {str(fileDir).replace(osUtils.sep + fileDir.name, '')}")
