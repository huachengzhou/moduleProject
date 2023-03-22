import  json as jsonUtils

import pathlib as pathLib


pagesFileDir = pathLib.Path(pathLib.Path.cwd().joinpath('pages.json'))

pagesFileJSONDir = pathLib.Path(pathLib.Path.cwd().joinpath('page_modules'))

print(pagesFileDir)
print(pagesFileJSONDir)


fileJSON = pathLib.Path.open(pagesFileDir, mode="r+", encoding="UTF-8")

listJSON = fileJSON.readlines()

fileJSON.close()

str1 = " ".join(listJSON)


pageJSON = jsonUtils.loads(str1)

# print(str1)

print(type(pageJSON))

print(pageJSON.get("tabBar"))

