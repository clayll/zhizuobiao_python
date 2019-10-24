class Human():
    def __init__(self,name,age,tel):
        self.name = name
        self.age= age
        self.tel = tel

    def getName(self):
        print(self.name)

    def getAge(self):
        print(self.age)

    def getTel(self):
        print(self.tel)

# h1 = Human("tom","54","12345678")
# h1.getName()
# h1.getAge()
# h1.getTel()

import  random
# 随机生成10个数
randomList = lambda :  [random.randrange(1,10)  for i in range(10)]

def randomList1():
    return [random.randrange(1, 10) for i in range(10)]

l1 = randomList()
l2 = randomList1()


def add(x,y):
    return (x+y)

print(list(map(add,l1,l2)))
print(list(map(lambda x,y:x+y,l1,l2)))