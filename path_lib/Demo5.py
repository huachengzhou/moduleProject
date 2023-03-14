import zipfile as zipUtils
import pathlib as pathLib
import random
import os as osUtils


# 解压文件路径
extracta_file_path = pathLib.Path(pathLib.Path.cwd().joinpath('extracta'))

# 压缩文件路径
sourceFileDir = pathLib.Path(pathLib.Path.cwd().joinpath(*('file_zip','69134srmdir_all.zip')))

# 判断文件夹是否存在
if extracta_file_path.exists():
    pass
else:
    # 不存在则建立文件夹
    pathLib.Path.mkdir(extracta_file_path)


zip_file = zipUtils.ZipFile(sourceFileDir)
# 解压

zip_extract = zip_file.extractall(extracta_file_path)
zip_file.close()