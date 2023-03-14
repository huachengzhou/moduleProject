import zipfile as zipUtils
import pathlib as pathLib
import random
import os as osUtils

# 压缩文件
zip_file_path = pathLib.Path(pathLib.Path.cwd().joinpath('file_zip'))

# 压缩文件路径
sourceFileDir = pathLib.Path(pathLib.Path.cwd().joinpath(('file')))

# 判断文件夹是否存在
if zip_file_path.exists():
    pass
else:
    # 不存在则建立文件夹
    pathLib.Path.mkdir(zip_file_path)

zip_file_path = pathLib.Path.joinpath(zip_file_path, str(random.randrange(1, 100000)) + "srmdir_all.zip")
print(zip_file_path)
print(sourceFileDir)
zipFile = zipUtils.ZipFile(zip_file_path, 'w', zipUtils.ZIP_DEFLATED)


def zipFileFun(sourceFileDir, zipFile):
    for dirpath, dirnames, filenames in osUtils.walk(sourceFileDir):
        # 这一句很重要，不replace的话，就从根目录开始复制
        fpath = dirpath.replace(str(sourceFileDir), '')
        # 这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
        fpath = fpath and fpath + osUtils.sep or ''
        for filename in filenames:
            zipFile.write(osUtils.path.join(dirpath, filename), fpath + filename)
            print('压缩成功', osUtils.path.join(dirpath, filename), fpath + filename)


zipFileFun(sourceFileDir, zipFile)

zipFile.close()

print("复杂压缩结束!")
