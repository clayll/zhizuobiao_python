import pandas as pd

a = pd.Series(['abc','def','abc def ghi'])
b = pd.Series([None,'zyx','vut'])

#字符大小转换
# print(a.str.lower())
# print(a.str.swapcase())

#字符填充/插入/扩展
# print(a.str.center(width=10,fillchar='?'))

#join在字符间插入字符

# print(a.map(lambda x:'?'.join(x)))




