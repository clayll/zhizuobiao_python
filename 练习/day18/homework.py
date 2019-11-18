import pandas as pd

s = pd.Series((1,2,3),index=("a","b","c"))
s2 = pd.Series((4,5,6),index=("a","b","c"))
df = pd.DataFrame()
df['a'] = s
df['b'] = s2
df.insert(0,'z',(4,56,7))
print(df)
# df.drop('c',axis=1,inplace=True)
# print(df)
df.columns = ["A","B","C"]

df.rename(index = {"a":1,"b":2,"c":3},inplace=True)
print(df)