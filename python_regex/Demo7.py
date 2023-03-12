# coding=UTF-8
# 解决 SyntaxError: Non-UTF-8 code starting with '\xe7' in file
import  re as regexUtils


str1 = "2月份，食品烟酒类价格同比上涨2.1%，影响CPI（居民消费价格指数）上涨约0.59个百分点。食品中，鲜果价格上涨8.5%，影响CPI上涨约0.18个百分点；蛋类价格上涨7.8%，影响CPI上涨约0.05个百分点；粮食价格上涨2.7%，影响CPI上涨约0.05个百分点；畜肉类价格上涨1.9%，影响CPI上涨约0.06个百分点，其中猪肉价格上涨3.9%，影响CPI上涨约0.05个百分点；水产品价格下降1.5%，影响CPI下降约0.03个百分点。"


matches = regexUtils.finditer("\\d+",str1)

for x in matches:
    print(x.group())





