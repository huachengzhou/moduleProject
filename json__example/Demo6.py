# -*- coding: UTF-8 -*-

import os as osUtils
import json as jsonUtils
import pathlib as pathLib


DIR_FILE_BASE = ""
DIR_FILE_PAGE_JSON = ""
DIR_FILE_PAGE_NEW_JSON = ""

def writeJSONFile(DIR_FILE_BASE, DIR_FILE_PAGE_JSON, DIR_FILE_PAGE_NEW_JSON,DIR_FIRST_PATH):
    print("......")
    print(DIR_FILE_BASE)
    print(DIR_FILE_PAGE_JSON)
    print(DIR_FILE_PAGE_NEW_JSON)
    print(DIR_FIRST_PATH)
    fileList = pathLib.Path.iterdir(pathLib.Path(DIR_FILE_BASE))
    listTotal = []

    # 遍历列表
    for filePath in fileList:
        fileJSON = pathLib.Path.open(filePath, mode="r+", encoding="UTF-8")
        strTemp = "  ".join(fileJSON.readlines())
        pageJSON = jsonUtils.loads(strTemp)
        listTemp = pageJSON.get("pages")
        for json in listTemp:
            json['path'] = pageJSON.get("root") + "/" + json['path']
        listTotal = listTotal + listTemp
        fileJSON.close()
        print("已经处理:", type(strTemp), filePath)
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

    pass




DIR_FIRST_PATH = "schedule/schedule"


def runFun():


    global DIR_FILE_BASE
    global DIR_FILE_PAGE_JSON
    global DIR_FILE_PAGE_NEW_JSON


    print("请输入json文件夹")
    DIR_FILE_BASE = input()
    print("请输入 uniapp pages.json 位置")
    DIR_FILE_PAGE_JSON = input()
    print("请输入 新的 uniapp pages.json 位置")
    DIR_FILE_PAGE_NEW_JSON = input()

    # print("请输入首个路由")
    # DIR_FIRST_PATH = input()

    print("json文件夹", DIR_FILE_BASE, sep=":")
    print("uniapp pages.json 位置", DIR_FILE_PAGE_JSON, sep=":")
    print("新的 uniapp pages.json 位置", DIR_FILE_PAGE_NEW_JSON, sep=":")


runFun()

print("运行请输入1")

user_input = input()
if user_input.isdigit() & int(user_input) == 1:
    print("开始执行!")
    writeJSONFile(DIR_FILE_BASE, DIR_FILE_PAGE_JSON, DIR_FILE_PAGE_NEW_JSON,DIR_FIRST_PATH)

osUtils.system("pause")
