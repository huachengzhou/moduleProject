str1 = 'aaa'
str2 = 'bbb'
tuple1 = (10, 20)
tuple2 = ('ccc', 'ddd')
list1 = [10, 20]
list2 = ['iii', 'jjj']
dict1 = {'name': 'YYQX'}
dict2 = {'age': 20}
print(str1 + str2)
print(tuple2 + tuple1)
print(list1 + list2)
print(str1 * 3)
print(tuple2 * 3)
print(list2 * 3)
print('a' in str1)
print('a' not in str1)
print('name' in dict1)
print('age' in dict2)

# 结果
"""
D:\CS\python_venv\my_venv\Scripts\python.exe D:\pythonProjects\moduleProject\container\Demo24.py 
aaabbb
('ccc', 'ddd', 10, 20)
[10, 20, 'iii', 'jjj']
aaaaaaaaa
('ccc', 'ddd', 'ccc', 'ddd', 'ccc', 'ddd')
['iii', 'jjj', 'iii', 'jjj', 'iii', 'jjj']
True
False
True
True

Process finished with exit code 0

"""