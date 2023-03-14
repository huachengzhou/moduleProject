import zipfile as zipUtils
import pathlib as pathLib
import random

# 判断文件夹是否存在
if pathLib.Path(pathLib.Path.cwd().joinpath('file_zip')).exists():
    pass
else:
    #不存在则建立文件夹
    pathLib.Path.mkdir(pathLib.Path(pathLib.Path.cwd().joinpath('file_zip')))

# 压缩文件路径
zip_file_path = pathLib.Path.cwd().joinpath(("file_zip"), str(random.randrange(1, 100000)) + "srmdir_all.zip")

print(zip_file_path)
zipFile = zipUtils.ZipFile(zip_file_path, 'w', zipUtils.ZIP_DEFLATED)

fileList = pathLib.Path.iterdir(pathLib.Path.cwd().joinpath(('file')))

for f in fileList:
    if f.is_file():
      pass
    # 目标地址path  源地址path
    zipFile.write(f.absolute(), f.name)
    pass

zipFile.close()


