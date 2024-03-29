
def test1():

    n = 5

    for i in range(n,0,-1):
        rs = 1
        for j in range(i,0,-1):
            rs=rs*j

        print("{0}的阶乘为：{1}".format(i,rs))




test1()



import prettytable as pt
class Employees:

    class Employee:
        def __init__(self, name, workHour, totalSalary):
            self.name = name
            self.workHour = workHour
            self.totalSalary = totalSalary

    def __init__(self):
        self.__employeeList = []

    def add_employee(self):
        while True:
            name = input("请输入员工姓名：")
            workHour = input("请输入员工工作小时：")
            salary = input("请输入时薪：")
            if workHour.isdigit() == False or  salary.isdigit() == False:
                print("请工作小时和时薪输入数字，现在请您重新输入")
                continue

            e = self.Employee(name,workHour,float(workHour)*float(workHour))
            self.__employeeList.append(e)
            rs = self.__isGoOn()
            if rs == 'Y':
                continue
            else:
                print("输入完毕！")
                self.__printRs()
                break


    def __isGoOn(self):
        while True:
            goon = input("是否继续添加 Y/N")
            if goon.isalpha()==True and goon.upper()== 'Y':
                return "Y"
            elif goon.isalpha() == True and goon.upper() == "N":
                return "N"
            else:
                print("输入有误，请重新输入")

    def __printRs(self):
        print('\t\t人员工资情况\t')
        tb = pt.PrettyTable()
        tb.field_names = ["雇员姓名", "工时", "薪水"]
        for i in self.__employeeList:
            tb.add_row([i.name,i.workHour,i.totalSalary])

        print(tb)

#
# es = Employees()
# es.add_employee()
import numpy as np
import matplotlib.pyplot as plt

def test3():


    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure("电影票房榜",figsize=(16,7))
    plt.title("电影票房榜",size=30)
    x_ = np.arange(0,20)
    x_lable = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊"]
    y_= [56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]
    plt.ylabel("电影名称")
    plt.xlabel("票房")
    plt.yticks(x_,labels=x_lable)
    for x,y in zip(y_,x_):
        plt.text(x,y,str(x)+"亿",va="center",color='g')
    # plt.barh([3,5],[12,20])
    plt.barh(x_,y_,color='yellow')
    plt.show()



delta = 0.25
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2

print(x.shape)
# print(y)
# print(Z)


plt.plot(X, Y,'.')
plt.show()

