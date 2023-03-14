import zipfile
import pathlib as pathLib
import random
import os


# 判断文件夹是否存在
if pathLib.Path(pathLib.Path.cwd().joinpath('file_zip')).exists():
    pass
else:
    # 不存在则建立文件夹
    pathLib.Path.mkdir(pathLib.Path(pathLib.Path.cwd().joinpath('file_zip')))

# 压缩文件路径
zip_file_path = pathLib.Path.cwd().joinpath(("file_zip"), str(random.randrange(1, 100000)) + "srmdir_all.zip")

directory = pathLib.Path.cwd().joinpath(('file'))


z = zipfile.ZipFile(zip_file_path,'w',zipfile.ZIP_DEFLATED) #参数一：文件夹名
for dirpath, dirnames, filenames in os.walk(directory):
    #这一句很重要，不replace的话，就从根目录开始复制
    fpath = dirpath.replace(str(directory),'')
    fpath = fpath and fpath + os.sep or ''#这句话理解我也点郁闷，实现当前文件夹以及包含的所有文件的压缩
    for filename in filenames:
        z.write(os.path.join(dirpath, filename),fpath+filename)
        print ('压缩成功',os.path.join(dirpath, filename),fpath+filename)
z.close()