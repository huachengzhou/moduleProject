import statistics
example_list = [1,2,3,4,5,6]

# 调和均值
# harmonic_mean(data) 用于计算数据的调和均值
print(statistics.mean(example_list))
print(statistics.harmonic_mean(example_list))
print(1/sum([1/1,1/2,1/3,1/4,1/5,1/6])*6)