import json as jsonUtils

import pathlib as pathLib
import os as osUtils


class FileLoader:
    def __init__(self):
        pass

    # 注解表示本方法是静态方法 不需要创建对象就可以调用 注意这个是高版本python语法
    @staticmethod
    def readFile(qss_file_name):
        """从文件中读取file的静态方法"""
        with open(qss_file_name, "r", encoding="UTF-8") as file:
            return file.read()


DIR_FILE_BASE = pathLib.Path(pathLib.Path.cwd().joinpath("page_modules"))
DIR_FILE_PAGE_JSON = pathLib.Path(pathLib.Path.cwd().joinpath('pages.json'))
DIR_FILE_PAGE_NEW_JSON = pathLib.Path(pathLib.Path.cwd().joinpath('pages.json'))

DIR_FIRST_PATH = "schedule/schedule"

fileList = pathLib.Path.iterdir(pathLib.Path(DIR_FILE_BASE))
listTotal = []

# 遍历列表
for filePath in fileList:
    str1X = str(filePath.name)
    if not str1X.endswith(".json"):
        continue
    strTemp = FileLoader.readFile(str(filePath))
    pageJSON = jsonUtils.loads(strTemp)
    listTemp = pageJSON.get("pages")
    for json in listTemp:
        json['path'] = pageJSON.get("root") + "/" + json['path']
    listTotal = listTotal + listTemp
    print("已经处理:", type(strTemp), filePath)
    pass

# 定义原始文件
fileJSONPath = pathLib.Path(pathLib.Path(DIR_FILE_PAGE_JSON))

# 排序
try:
    listTotal = sorted(listTotal, key=lambda entityJSON: entityJSON["path"].find(DIR_FIRST_PATH), reverse=True)
    print("已经排序")
except:
    print("没有定义首个路由")

# 生成 json对象
pageJSONParent = jsonUtils.loads(FileLoader.readFile(str(fileJSONPath)))
# 添加路由列表属性
pageJSONParent["pages"] = listTotal
# 将 json转化为字符串
jsonString = jsonUtils.dumps(pageJSONParent, ensure_ascii=False,indent=2)
print(str(pageJSONParent))

# 定义文件对象

with open(str(DIR_FILE_PAGE_NEW_JSON), "w") as fileWrite:
    # jsonUtils.dump(pageJSONParent, fp=fileWrite)
    jsonUtils.dump(pageJSONParent, fp=fileWrite,ensure_ascii=False)

fileWrite.close()

print("完成!")
osUtils.system("pause")