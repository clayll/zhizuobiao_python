dic = {1:"clay",2:"mike"}





# 1. (本题3分)现在有一个List[1,2,3,4,5,6,7,8,10]，手动输入一个数字，分别与List中的每一个成员进行身份运算，并输出结果。
# 2.(本题2分)
#    定义一个整形变量，并打印出其变量类型，再定义一个浮点型变量并打印其变量类型，将这个整形和浮点型相乘，预测并打印其变量类型。
# 3. (本题3分)Python里面如何拷贝一个对象？（赋值，浅拷贝，深拷贝的区别）
# 4. (本题2分)存在字符串“ab2b3n5n2n67mm4n2”,编程统计字符串中字母n出现的次数

#回家作业
# dic = {
#     'name':'汪峰',
#     'age':48,
#     'wife':[{'name':'国际章','age':38}],
#     'children':{'first_girl':'小苹果', 'sencond_girl':'小一','third_girl':'顶顶'}
# }
#1.获取汪峰的名字
#2.获取这个字典{'name':'国际章','age':38}
#3.获取汪峰妻子的名字
#4.获取汪峰的第三个孩子的名字

def test1():
    ls = [i+1 for i in range(10)]
    inputStr = input("手动输入一个数字:")
    try:
        inputStr = int(inputStr)
    except:
        print("您输入的不是数字，请重新输入")
        return

    for i in ls:
        print("身份运算结果：%s " % bool(i==inputStr))


def test2():
    n1 = 2;
    print("整形类型为：%s " % type(n1))
    n2 = 1.5
    print("浮点类型为：%s " % type(n2))
    n3 = n1 * n2
    print("整形和浮点型相乘类型为：%s" % type(n3))

def test3():
    s1 = "test"
    s2 = s1
    s1 = "test2"
    print(s1)


def test4():
    inputStr = input("请输入带n的字符串:")
    ls = list(inputStr)
    n = ls.count('n')
    print("您输入的字符串没有n" if n == 0  else "您输入的字符串中n包括%d个" % n)

def test5():
    dic = {
        'name':'汪峰',
        'age':48,
        'wife':[{'name':'国际章','age':38}],
        'children':{'first_girl':'小苹果', 'sencond_girl':'小一','third_girl':'顶顶'}
    }
    # 1.获取汪峰的名字
    print("获取汪峰的名字:%s" % dic['name'])
    # 2.获取这个字典{'name':'国际章','age':38}
    print("获取汪峰的名字:%s" % dic.setdefault('wife'))
    # 3.获取汪峰妻子的名字
    print("获取汪峰妻子的名字:%s" % dic.setdefault('wife')[0]['name'])
    # 4.获取汪峰的第三个孩子的名字
    print("汪峰的第三个孩子的名字:%s" % [dic.setdefault('children')[i] for i in  dic.setdefault('children').keys()][2])
def test():
    list1 = [2, 3, 8, 4, 9, 5, 6]
    list2 = [5, 6, 10, 17, 11, 2]

    ls = map(lambda x,y : x+y,[i+1 for i in range(10)],[i+2 for i in range(10)])
    print(list(ls))
test()

# test4()

# map(float,input())