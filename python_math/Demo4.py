import statistics

# 计算分组连续数据的中位数

print(statistics.median_high([1, 4, 7]))

print(statistics.median_high([1, 4, 7, 10]))

"""
median_grouped(data, interval=1)函数
median_grouped(data, interval=1) 函数用于计算分组连续数据的中位数。其中 interval 表示数据之间的间隔，即组距。

此函数计算方法较复杂，可参考公式 中位数=中位数所在组下限+{[(样本总数/2-到中位数所在组下限的累加次数)/中位数所在组的次数]*中位数的组距} ,
如果数据是空的会报 StatisticsError
"""

print(statistics.median_grouped([1, 2, 2, 3, 4, 4, 4, 4, 4, 5]))


print(statistics.median_grouped([3, 4, 4, 5, 6], interval=1))

print(statistics.median_grouped([1, 3, 5, 5, 7], interval=2))