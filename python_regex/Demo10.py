# coding=UTF-8
# 解决 SyntaxError: Non-UTF-8 code starting with '\xe7' in file
import pathlib
import re as regexUtils


str1 = """
李杜诗篇万口传，至今已觉不新鲜。
出自清代：赵翼的《论诗五首》

满眼生机转化钧，天工人巧日争新。
预支五百年新意，到了千年又觉陈。

李杜诗篇万口传，至今已觉不新鲜。
江山代有才人出，各领风骚数百年。

只眼须凭自主张，纷纷艺苑漫雌黄。
矮人看戏何曾见，都是随人说短长。

少时学语苦难圆，只道工夫半未全。
到老始知非力取，三分人事七分天。

诗解穷人我未空，想因诗尚不曾工。
熊鱼自笑贪心甚，既要工诗又怕穷。
"""

list1 = regexUtils.split("\\W",str1)

# print(list1)

for ss in list1:
    print(ss)


