import json as jsonUtils

import pathlib as pathLib



fileJSONParent = pathLib.Path.open(pathLib.Path(pathLib.Path.cwd().joinpath('pages.json')), mode="r+", encoding="UTF-8")
listJSONParent = fileJSONParent.readlines()
fileJSONParent.close()
pageJSONParent = jsonUtils.loads(" ".join(listJSONParent))

pagesFileJSONDir = pathLib.Path(pathLib.Path.cwd().joinpath(*("page_modules", "acc.json")))
fileJSON = pathLib.Path.open(pagesFileJSONDir, mode="r+", encoding="UTF-8")
listJSON = fileJSON.readlines()
fileJSON.close()

pageJSON = jsonUtils.loads(" ".join(listJSON))

list1 = pageJSON.get("pages")

for json in list1:
    json['path'] = pageJSON.get("root") + "/" + json['path']

pageJSONParent["pages"] = list1

jsonString = jsonUtils.dumps(pageJSONParent,ensure_ascii=False)


fileWrite = open(pathLib.Path(pathLib.Path.cwd().joinpath('pages2.json')), "w", encoding="UTF-8")
fileWrite.write(jsonString)
fileWrite.flush()

fileWrite.close()
