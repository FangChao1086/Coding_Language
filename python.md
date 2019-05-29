# python

[参考链接：python知识点详细](https://github.com/taizilongxu/interview_python#20-%E9%97%AD%E5%8C%85)   

* [python3新特性](#python3新特性)
* [基础](#基础)
  * [输入](#输入)
* [np.mat()与np.array()的区别](#np.mat()与np.array()的区别)
* [\*args与\*\*kwargs的区别](#args与kwargs的区别)
* [re.match与re.search的区别](#re.match与re.search的区别)
* [extend与append的区别](#extend与append的区别)
* [浅拷贝与深拷贝](#浅拷贝与深拷贝)
* [迭代器和生成器](#迭代器和生成器)
* [打印1-100内的素数](#打印1-100内的素数)
* [最大公约数](#最大公约数)
* [最小公倍数](#最小公倍数)
* [自动补0](#自动补0)
* [生成可执行文件.exe](#生成可执行文件.exe)

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

<span id="np.mat()与np.array()的区别"><//span>
## np.mat()与np.array()的区别
[参考链接：np.mat()与np.array()的区别](https://www.jianshu.com/p/3a9c3a397932)
* np.mat()
  * 矩阵相乘：(\*) 或者 np.dot()
  * 点乘：np.multiply()
* np.array()
  * 矩阵相乘：np.dot()
  * 点乘：\* 或者 np.multiply()

<span id="args与kwargs的区别"></span>
## \*args与\*\*kwargs的区别 
[参考链接：\*args与\*\*kwargs的区别](https://www.cnblogs.com/yunguoxiaoqiao/p/7626992.html)
* \*args：将关键字参数打包成**tuple**给函数体使用  
* \*\*kwargs：将关键字参数打包成**dict**给函数体使用  

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

<span id="打印1-100内的素数"></span>
## 打印1-100内的素数
```python
# 打印素数
print(' '.join([str(item) for item in filter(lambda x: not [x % i for i in range(2, x) if x % i == 0], range(2, 101))]))
```

<span id="最大公约数"></span>
## 最大公约数
```python
# 获取两个数的最大公约数
def hcf(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


if __name__ == '__main__':
    num1 = int(input('输入第一个数字：'))
    num2 = int(input('输入第二个数字：'))

    print(num1, '和', num2, '的最大公约数为', hcf(num1, num2))
```

<span id="最小公倍数"></span>
## 最小公倍数
```python
# 获取两个数的最小公倍数
def lcm(x, y):
    if x < y:
        greater = y
    else:
        greater = x
    while (True):
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 112

    return lcm


if __name__ == '__main__':
    num1 = int(input('输入第一个数字：'))
    num2 = int(input('输入第二个数字：'))

    print(num1, '和', num2, '的最小公倍数为', lcm(num1, num2))
```

<span id="自动补0"></span>
## 自动补0
```python
# 字符串
n = '123'
s = n.zfill(5)

# int
n = 123
s = "%05d" % n

'''
'00123'
'''
```

<span id="生成可执行文件.exe"></span>
## 生成可执行文件.exe
* 依赖pyinstaller  
`pip install pyinstaller`
* **生成可执行文件命令**  
`pyinstaller -F xx.py`  
`-F`表示生成单个可执行文件  
* 结果
  * 在终端命令行路径中出现xx.spec文件（成功打包时，还会有dist文件夹）
  * **可执行文件.exe在dist文件夹中**
* 可能出现的问题  
`RecursionError: maximum recursion depth exceeded`
  * 解决步骤1，在xx.spec文件中添加如下代码,并保存  
  ```python
  import sys
  sys.setrecursionlimit(1000000)
  ```
  * 解决步骤2，在终端执行以下命令  
  `pyinstaller -F xx.spec`
  
 
