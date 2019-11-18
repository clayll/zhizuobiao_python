#什么是PyQuery
#是一种类似于Jquery的解析网页工具。
#lxml
#一、初始化PyQuery对象
#1.初始化PyQuery对象
#方式一：通过网页信息初始化PyQuery对象
# from pyquery import PyQuery as pq
# s = '<html><title>PyQuery用法总结</title></html>'
# doc = pq(s)
# print(doc('title'))

#PyQuery还会将残缺的html文档补全。
# s = '<html><title>PyQuery用法总结</title>'
# doc = pq(s)
# print(doc('html'))

#方式二:URL网址初始化PyQuery对象
#将要解析的URL网址当作参数传递给PyQuery类
# from pyquery import PyQuery as pq
# url = 'http://www.baidu.com'
# doc = pq(url=url,encoding='utf-8')
# print(doc('title'))

#方式三:通过文件初始化PyQuery对象
# from pyquery import PyQuery as pq
# doc = pq(filename='baidu.html',encoding='utf-8')
# print(doc('title'))

#2.访问节点属性:
#使用attr()方法访问节点的属性
# from pyquery import PyQuery as pq
# li = pq('<li id="test1" class="test1"></li><li id="test2" class="test2"></li>')('li')
# print(li.attr("id"))
#代码中有两个不同的id节点。但是attr()方法只取第一个节点的id属性值，而不取第二个。
# li = pq('<li class="test1"></li><li id="test2" class="test2"></li>')('li')
# print(li.attr("id"))
#第一个li节点没有id属性，所以返回None

#***如果要取多个li节点的属性值，就要用到items()方法来实现
#items()方法返回的节点的生成器对象：generator object PyQuery.items
# from pyquery import PyQuery as pq
# li = pq('<li id="test1" class="test1"></li><li id="test2" class="test2"></li>')('li')
# print(li.items())
# for item in li.items():
#     print(item.attr("id"))
# <generator object PyQuery.items at 0x000001D17B996570>
# test1
# test2

#节点的增删改查
#1.动态添加节点属性
#PyQuery有很多方法动态添加节点属性：
#addClass()，动态添加class属性
# from pyquery import PyQuery as pq
# html = '<li id="test1" class="test1"></li>'
# li = pq(html)('li')
# li.addClass("zhuzhu")
# print(li)
#2.使用attr()方法还能动态添加其他属性:
# from pyquery import PyQuery as pq
# html = '<li id="test1" class="test1"></li>'
# li = pq(html)('li')
# li.attr('name','li name')
# print(li)
# li.attr("type","li")
# print(li)
# print(li.attr("type"))
#*执行第一个attr()方法时，有两个参数，分别是name和li name。 这是给li节点添加name属性和属性值。
#执行第二个attr()也是两个参数，分别type和li，这是给li节点添加type属性及type的属性值
#执行第三次attr()只有一个type参数，就是获取li节点type值
#***小结:attr()方法只有一个参数时，是获取节点的属性值
#若有两个参数时，是给节点添加属性及属性值。第一个参数为属性，第二个参数为属性值。

#removeClass()，动态移除节点class属性:
# from pyquery import PyQuery as pq
# html = '<li id="test1" class="test1"></li>'
# li = pq(html)('li')
# li.removeClass("test1")
# print(li)
#将 class节点属性值由test1变为""。


#动态添加/修改文本值
#PyQuery是支持动态给节点添加文本值:
#可使用html()和text()方法都可以动态地给节点添加或修改节点地文本值。
# from pyquery import PyQuery as pq
# html = '<li id="test1" class="test1"></li>'
# li = pq(html)('li')
# li.html("i love you")
# print(li)
# li.text("I love you too")
# print(li)

#获取节点地文本值
# from pyquery import PyQuery as pq
# html = '<li id="test_id">My name is Zhuzhu</li>'
# li = pq(html)('li')
# print(li.html())
# print(li.text())
#小结:html()和text()如果没有参数，则是获取属性的文本值；如果有参数，则是改变或者添加节点的属性值


#移除节点:
#remove()方法可以动态移除节点

# from pyquery import PyQuery as pq
# # html = '''
# # <ul>
# #     hello I am ul tag
# #     <li>
# #         hello I am li tag
# #     </li>
# # </ul>
# # '''
# #
# # ul = pq(html)('ul')
# # print(ul.text())
# # print('执行remove()移除节点')
# # ul.find('li').remove()
# # print(ul.text())
#上述代码的ul节点中有li节点，执行ul.text()方法会返回包括li节点的文本信息。
#若我们不要返回li节点信息，直接用remove()方法，删除掉ul节点中的li节点。

#查询节点
#PyQuery支持使用css的. #来查找节点。
#.代表class ;#代表id
# from pyquery import PyQuery as pq
# html = '''
# <div class="div_tag">
#     <ul id ="ul_tag">
#         hello I am ul tag
#             <li>hello I am li tag</li>
#             <li>hello I am li tag too</li>
#     </ul>
# </div>
# '''
# doc = pq(html)
# print(doc('.div_tag #ul_tag li'))


#find()方法查找节点
# from pyquery import PyQuery as pq
# html = '''
#     <div class="div_tag">
#         <ul id ="ul_tag">
#             hello I am ul tag
#                 <li>hello I am li tag
#                     <a>
#                           www.baidu.com
#                      </a>
#                    </li>
#                <li>hello I am li tag too</li>
#         </ul>
#     </div>
# '''
# doc = pq(html)
# print(doc('.div_tag #ul_tag').find("li"))
# print(doc('.div_tag #ul_tag li'))
#find("li")是把所有li节点及子节点全部都查找出来



#children()方法,是获取当前节点的所有子节点。

# from pyquery import PyQuery as pq
# html = '''
#     <div class="div_tag">
#         <ul id ="ul_tag">
#             hello I am ul tag
#                 <li>hello I am li tag
#                     <a>
#                           www.baidu.com
#                      </a>
#                    </li>
#                <li>hello I am li tag too</li>
#         </ul>
#     </div>
# '''
# doc = pq(html)
# print(doc('.div_tag').children().find("li"))

#使用parent()方法获取当前节点的父亲节点:
#parents()会返回节点的所有祖宗节点:html,body,div,ul

from pyquery import PyQuery as pq
html = '''
<div class="div_tag">
<ul id = "ul_tag">
hello I am ul tag
<li>hello I am li tag<a>www.bigdata17.com</li>
<li>hello I am li tag too</li>
</ul>
</div>
'''
doc = pq(html)
print(doc('.div_tag #ul_tag li:first').parents())


#siblings()方法返回当前节点的兄弟节点:

from pyquery import PyQuery as pq
html = '''
<div class="div_tag">
<ul id = "ul_tag">
hello I am ul tag
<li class='li_class1'>hello I am li tag<a>www.bigdata17.com</li>
<li class='li_class2'>hello I am li tag too</li>
<li class='li_class3'>hello I am li tag third</li> 
</ul>
</div>
'''
doc = pq(html)
# print(doc('.div_tag #ul_tag .li_class1').siblings())
#筛选要符合条件的节点
# print(doc('.div_tag #ul_tag .li_class1').siblings('.li_class2'))

