# 1. 现有如下代码：
class Student:
	def __init__(self,name,age,score):
		self.name,self.age,self.score = name,age,score
	# def __repr__(self):
	# 	return "Hello world"
	def infos(self):
		m = "Hello China"
		return m
	# def __str__(self):
	# 	return self.infos()
#
s1 = Student("Bob",30,88)
print(s1)
# （1）请问执行结果是什么？
#     Hello China
# # （2）请简单写出程序执行的过程及原因 (3分)
#     1.首先执行__init__方法进行赋值。2.print方法本来应该打印默认该对象的对性内存地址，发现同时实现了__repr__与__str__，当两者同时
# 实现时，__str__替代__repr__调用
#
#
# 2.写一个简单的线程计时器，每隔一秒在屏幕打印当前时间，时间格式为HH:MM:SS
# (5分)
import threading
import time
def showTime():
    while True:
        print(time.strftime("%HH:%MM:%SS", time.localtime()))
        time.sleep(1)

t = threading.Thread(target=showTime)
t.start()





# 3.画一个两行两列的子图。每张子图上标明序号数字。（2分）
import matplotlib.pyplot as plt

plt.figure("两行两列的子图",figsize=(8,6),facecolor='lightgray',edgecolor='b',linewidth=4)

for i in range(1,5):
    plt.subplot(2, 2, i,)
    axes = plt.gca()
    plt.xticks(())
    plt.yticks(())
    plt.text(0.5,0.5,i,color='r',size=36,ha='center',va='center')

plt.show()

