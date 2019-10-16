#演示循环
# while True:
#     print('A')
#     print('B')
#     print('C')
#     print('D')

#上面是一个死循环

#如何终止呢：
#1.改变条件:利用改变条件，终止循环。标志位的概念
# flag = True
# while flag:
#     print('A')
#     print('B')
#     print('C')
#     flag = False
#     print('D')


#例2: 显示打印从1-100
# count = 1
# flag = True
# while flag:
#     print(count)
#     count += 1
#     if count == 101:
#         flag = False

#2.break
#循环中，只要遇到break立马跳出循环：
# flag = True
# while flag:
#     print('A')
#     print('B')
#     print('C')
#     break
#     print('D')
# print(222)

#方法一:
# count = 1
# while True:
#     if count % 2 == 0:
#         print(count)
#     count += 1
#     if count == 101:
#         break

#方法二：
# count = 1
# while count < 101:
#     if count % 2 == 0:
#         print(count)
#     count += 1

#方法三:
# count = 2
# while count < 101:
#     print(count)
#     count += 2

#3.调用系统命令: quit()  exit()  不建议使用

#4.关键字:continue (终止本次循环)
#contiune终止本次循环，继续下一次循环

# flag = True
# print(111)
# while flag:
#     print('A')
#     print('B')
#     print('C')
#     continue
#     print('D')
# print(222)

# count = 0
# while count < 10:
#     count += 1
#     if count == 7:
#         continue
#     print(count)

# count = 0
# while count <= 100:
#     count += 1
#     if count > 5 and count < 95:
#         continue
#     print(count)


#5.while..else:
#while后面的else作用：当while循环正常执行，中间没有被break，就会执行else后面的语句
count = 0
while count <= 5:
    count += 1
    if count == 3:
        break
    print("循环",count)
else:
    print("循环正常执行完毕")
print("--out of while loop--")
