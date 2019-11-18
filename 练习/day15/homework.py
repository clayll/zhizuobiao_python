# 1.	正则表达式匹配中，（.）和（.?）匹配区别？  （2分）
# (.)表示匹配除了\n的一个字符，(.?)表示匹配除了\n的0个或者1个字符,如：
import re
p1 = re.compile(r"(.?)")
s = "1231231"
print(re.match(p1,s))
# 2. 正则匹配，匹配日期2018-03-20			（2分）
url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'
# 采用分组的方式，保证获取到url中dateRange这个参数避免其他参数也有日期的情况
p2 = re.compile(r"(dateRange=)([\d]+-[\d]+-[\d]+)")
rs = re.search(p2,url)
print(rs.group(2))


# 3. 举例说明zip（）函数用法···		(2分)
# 把两组迭代对象组合在一起，生成list，元素为元组
# 3.1
l1 = [i for i in range(10)]
l2=['A',"B","C","D","E","F",'G','H','I','J']
l3 = zip(l1,l2)
print(list(l3))
# 3.2 生成坐标点
import numpy as np
x = np.linspace(1,100,100)
y = np.linspace(50,5000,100)
rs = zip(x,y)
print(list(rs))


# 4. 生成0-100的随机数			（2分）
import random
# 4.1方法1 数字随机不重复
l1 = [i for i in range(0,101)]
random.shuffle(l1)
print(l1)
# 4.2 方法2 数字可能是重复的
l2 = [random.randint(0,100) for i in range(100)]
print(l2)


# 5. fun(*args,**kwargs)中的*args,**kwargs什么意思？（2分）
#  *arg 表示的是除了key=valeu形式的参数把他放到args中，类型为元组；**kwargs表示的任意个key=value形式键值对，kwargs类型为字典
def fun(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)
def test():
    pass

fun(1,3,4,5,(123,456),test,{"k":3,"x":3},k=2,z=3,w=5,f=test)