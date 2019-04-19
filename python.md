# python
* [python3新特性](#python3新特性)
* [基础](#基础)
  * [输入](#输入)
* [re.match与re.search的区别](#re.match与re.search的区别)
* [extend与append的区别](#extend与append的区别)
* [浅拷贝与深拷贝](#浅拷贝与深拷贝)
* [迭代器和生成器](#迭代器和生成器)

<span id="python3新特性"></span>
## python3新特性
* pathlib模块
* 格式化字符串变量
* 统一编码支持中文字符
* Python 3.5 将支持 Async/Await 异步编程

<span id="基础"></span>
# 基础
<span id="输入"></span>
## 输入
![1.png](https://github.com/FangChao1086/Coding_language/blob/master/素材/1.PNG)  
```py
M, N = list(map(int, input().split(',')))

book = []
for i in range(M):
    line = list(map(int, input().split(',')))
    book.append(line)
```
---
![2.png](https://github.com/FangChao1086/Coding_language/blob/master/素材/2.PNG)
```py
# 输入处理
m = int(input())

tmp = []
for _ in range(m):
    line = [list(map(int, item.split(','))) for item in input().split(';')]
    tmp.extend(line)  # 
```
---
![3.png](https://github.com/FangChao1086/Coding_language/blob/master/素材/3.PNG)
```py
# 输入处理
n = int(input())
x, y = [], []
for i in range(n):
    _x, _y = list(map(int, input().split()))
    x.append(_x)
    y.append(_y)
```
---

<span id="re.match与re.search的区别"></span>
## re.match与re.search的区别
[参考链接：re.match与re.search的区别](http://www.runoob.com/python3/python3-reg-expressions.html)  
* re.match：从字符串的起始位置匹配，起始位置匹配不成功就返回None
* re.search：对整个字符串进行匹配

<span id="extend与append的区别"></span>
# extend与append的区别
[extend与append的区别](https://www.cnblogs.com/tzuxung/p/5706245.html)

<span id="浅拷贝与深拷贝"></span>
# 浅拷贝与深拷贝
[浅拷贝与深拷贝](https://www.cnblogs.com/xueli/p/4952063.html)

<span id="迭代器和生成器"></span>
## 迭代器和生成器
[参考链接：迭代器和生成器](http://www.runoob.com/python3/python3-iterator-generator.html)  
* 迭代器：一个可以记住遍历的位置的对象。
  * 基本方法：iter() 和 next()  
* 生成器：一个返回迭代器的函数，只能用于迭代操作
  1. 运行时，每次遇到**yield**时函数会暂停并保存当前所有的运行信息，返回 yield 的值
  2. 在下一次执行next()方法时从当前位置继续运行。

