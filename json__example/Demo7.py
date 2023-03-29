import json as jsonUtils

import pathlib as pathLib



DIR_FILE_BASE =  pathLib.Path(pathLib.Path.cwd().joinpath("page_modules"))
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
    fileJSON = pathLib.Path.open(filePath, mode="r+", encoding="UTF-8")
    strTemp = "  ".join(fileJSON.readlines())
    pageJSON = jsonUtils.loads(strTemp)
    listTemp = pageJSON.get("pages")
    for json in listTemp:
        json['path'] = pageJSON.get("root") + "/" + json['path']
    listTotal = listTotal + listTemp
    fileJSON.close()
    # print("已经处理:", type(strTemp), filePath)
    pass

# 定义原始文件
fileJSONParent = pathLib.Path.open(pathLib.Path(pathLib.Path(DIR_FILE_PAGE_JSON)), mode="r+", encoding="UTF-8")
# 读取json串字符
listJSONParent = fileJSONParent.readlines()
fileJSONParent.close()

# 排序
try:
    listTotal = sorted(listTotal, key=lambda entityJSON: entityJSON["path"].find(DIR_FIRST_PATH), reverse=True)
    print("已经排序")
except:
    print("没有定义首个路由")

# 生成 json对象
pageJSONParent = jsonUtils.loads(" ".join(listJSONParent))
# 添加路由列表属性
pageJSONParent["pages"] = listTotal
# 将 json转化为字符串
jsonString = jsonUtils.dumps(pageJSONParent, ensure_ascii=False)

# 定义文件对象
fileWrite = open(pathLib.Path(DIR_FILE_PAGE_NEW_JSON), "w", encoding="UTF-8")
# 写入json字符串到文件中
fileWrite.write(jsonString)
fileWrite.flush()

fileWrite.close()

print("完成!")
