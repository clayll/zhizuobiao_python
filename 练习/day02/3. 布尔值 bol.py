#布尔值就两种：True，False
# 真：1 True； 假：0 False
#int str bool三者数据类型之间的转换
i1 = 100
print(bool(i1)) #True #非零即显示True

i2 = 0
print(bool(i2)) #False #零即False

t = True
print(int(t)) # True = 1

f = False
print(int(f)) # False = 0

print("True + False =",t + f)

#字符串转bool
s1 = "猪猪"
s2 = ''
print(bool(s1)) #True非空即True
print(bool(s2)) #空就是False




