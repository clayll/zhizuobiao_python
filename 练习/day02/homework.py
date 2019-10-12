'''
输入一个年份（例如2012），判断其是否为闰年，如果不是闰年则提示距离该年最近的闰年是哪一年。
'''
def test11():
    inputStr = input("请输入年份:")
    inputYear = int(inputStr)

    if inputYear % 4  != 0 :
        print("%s年不是闰年" % inputYear);
    elif inputYear % 100 == 0 and inputYear % 400 != 0:
        print("%s年不是闰年" % inputYear);
    else:
        print("%s年是闰年" % inputYear);

def test12():
    pass

'''
键盘输入一个字符，使用两种方法，判断该字符为大写还是小写，并将其大小写翻转输出。
'''
def test13():
    inputStr = input("请输入一个字符:")
    if len(inputStr) > 1:
        print("您输入的字符超过了一个，请重新输入。")
    if inputStr.islower():
        print("输入的小写字母，反转为：%s" % inputStr.upper())
    elif inputStr.isupper():
        print("输入的大写字母，反转为：%s" % inputStr.lower())
    else:
        print("输入的不是英文字母，请重新输入。" )

'''
按升序合并如下两个list, 并去除重复的元素
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
'''
def test21():
    import copy
    list1 = [2, 3, 8, 4, 9, 5, 6]
    list2 = [5, 6, 10, 17, 11, 2]
    list3 = copy.deepcopy(list1)
    list3.extend(list2)
    list4 = []
    for item in list3:
        if  item  not in list4:
            list4.append(item)

    list4.sort()
    print(list4)


test21()