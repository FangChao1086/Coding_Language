# python

[参考链接：python知识点详细](https://github.com/taizilongxu/interview_python#20-%E9%97%AD%E5%8C%85)   

* [python3新特性](#python3新特性)
* [基础](#基础)
  * [输入](#输入)
* [变量的作用域](#变量的作用域)
* [dict按value排序](#dict按value排序)
* [.format的用法](#.format的用法)
* [np.mat()与np.array()的区别](#np.mat()与np.array()的区别)
* [\*args与\*\*kwargs的区别](#args与kwargs的区别)
* [re.match与re.search的区别](#re.match与re.search的区别)
* [extend与append的区别](#extend与append的区别)
* [浅拷贝与深拷贝](#浅拷贝与深拷贝)
* [迭代器和生成器](#迭代器和生成器)
* [线程与进程](#线程与进程)
* [打印1-100内的素数](#打印1-100内的素数)
* [最大公约数](#最大公约数)
* [最小公倍数](#最小公倍数)
* [自动补0](#自动补0)
* [拍照功能](#拍照功能)
* [生成可执行文件.exe](#生成可执行文件.exe)
* [python彩蛋](#python彩蛋)

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

## 变量的作用域
* 全局变量
  * 在函数体外定义的变量
* 局部变量
  * 在函数体内部定义的变量
* **作用域**
  * **全局变量在所有作用域都可读**
  * **局部变量只能在本函数可读**
  * 优先读取函数本身有的局部变量，再去读全局变量
  * 函数体内要想对全局变量进行修改，需要在函数体内先用全局关键字global定义
  
```python
'''
author:fangchao
date:2019/6/10

content: 变量的作用域
'''
# 全局变量
balance = 1


def change():
    # 定义全局变量
    global balance
    balance = 100
    # 定义局部变量
    num = 20
    print("change() balance={0}".format(balance))


if __name__ == "__main__":
    change()
    print("修改后的 balance={0}".format(balance))

'''
change() balance=100
修改后的 balance=100

# 如果注释掉change()函数里的 global
change() balance=100
修改后的 balance=1
'''
```

<span id="dict按value排序"></span>
## dict按value排序
```python
# 按照value从大到小排序:
sorted(d.items(), key = lambda x:x[1], reverse = True)

# 按照value从小到大排序:
sorted(d.items(), key = lambda x:x[1], reverse =False)
```

<span id=".format的用法"></span>
## .format的用法
```python
d = 'a: {}, b: {}'.format(23, 34)
print(d)

'''
a: 23, b: 34
'''
```

<span id="np.mat()与np.array()的区别"></span>
## np.mat()与np.array()的区别
[参考链接：np.mat()与np.array()的区别](https://www.jianshu.com/p/3a9c3a397932)
* np.mat()
  * 矩阵相乘：\* 或者 np.dot()
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
[参考链接：浅拷贝与深拷贝](https://www.cnblogs.com/xueli/p/4952063.html)  
* copy浅拷贝：没有拷贝子对象，原始数据改变，子对象也会跟着改变
* deepcopy深拷贝：拷贝子对象，原始数据改变，子对象不会改变

<span id="迭代器和生成器"></span>
## 迭代器和生成器
[参考链接：迭代器和生成器](http://www.runoob.com/python3/python3-iterator-generator.html)  
* 迭代器：一个可以记住遍历的位置的对象。
  * 基本方法：iter() 和 next()  
* 生成器：一个返回迭代器的函数，只能用于迭代操作
  1. 运行时，每次遇到**yield**时函数会暂停并保存当前所有的运行信息，返回 yield 的值
  2. 在下一次执行next()方法时从当前位置继续运行。

## 线程与进程
### 线程
* **守护线程**
  * 运行前提：主线程必须存在，不存在时守护线程就会被销毁
* **多线程的锁机制**
  * 多进程之间对内存中的变量不会产生冲突
  * **多个线程对内存中的共享变量同时进行操作时会产生影响，产生死锁（线程安全问题，需要加锁解决，对数据进行锁定）**
    * 示例，两个线程：t1,t2；t1对全局变量a进行加100任务，t2对全局变量a进行减100任务；当线程t1、t2同时修改全局变量a时，循环次数够多时，a的值就会出现变化
    * ```python
      '''
      author:fangchao
      date:2019/6/10

      content:线程死锁
      '''
      import threading

      balance = 100


      def change(num, counter):
          global balance
          for i in range(counter):
              balance += num
              balance -= num
              if balance != 100:
                  # 如果输出这句话，说明线程不安全
                  print("balance=%d" % balance)
                  break


      if __name__ == "__main__":
          thr1 = threading.Thread(target=change, args=(100, 500000), name='t1')
          thr2 = threading.Thread(target=change, args=(100, 500000), name='t2')
          thr1.start()
          thr2.start()
          thr1.join()
          thr2.join()
          print("{0} 线程结束".format(threading.current_thread().getName()))

      '''
      balance=200
      MainThread 线程结束
      '''
      ```
* 死锁的解决方案：**互斥锁**
  * 在某个线程需要更改共享数据时，先将其资源锁定，直到该线程释放资源时，其他线程才能对其进行更改
  * 核心代码
    * ```python
      # 创建锁
      mutex = threading.Lock()
      # 锁定
      mutex.acquire()
      # 释放
      mutex.release()
      ```
  * 示例
    * ```python
      '''
      author:fangchao
      date:2019/6/10

      content:互斥锁
      '''
      import threading

      balance = 100
      lock = threading.Lock()  # 创建锁


      def change(num, counter):
          global balance
          for i in range(counter):
              # 先要获取锁
              lock.acquire()
              balance += num
              balance -= num

              # 释放锁
              lock.release()

              if balance != 100:
                  # 如果输出这句话，说明线程不安全
                  print("balance=%d" % balance)
                  break


      if __name__ == "__main__":
          thr1 = threading.Thread(target=change, args=(100, 500000), name='t1')
          thr2 = threading.Thread(target=change, args=(100, 500000), name='t2')
          thr1.start()
          thr2.start()
          thr1.join()
          thr2.join()
          print("{0} 线程结束".format(threading.current_thread().getName()))

      '''
      MainThread 线程结束
      '''
      ```
      
### 多线程与多进程的区别
* 一个程序至少有一个进程，一个进程至少有一个线程
* 进程在执行过程中拥有独立的内存单元，但多个线程共享内存
* 线程不能够独立的执行，需要依存在应用程序中

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

## 拍照功能
* 显示画面，按S拍照，按空格退出
```python
'''
author:fangchao
date:2019/6/11

content:拍照功能
'''
import cv2

# 0:笔记本摄像头  1：外置摄像头
cap = cv2.VideoCapture(0)
i = 0

while (True):
    ret, frame = cap.read()
    if ret:
        cv2.imshow('capture', frame)
    k = cv2.waitKey(1)  # 等待1ms
    if k == ord(' '):
        break
    if k == ord('s'):
        cv2.imwrite('capture_' + str(i) + '.jpg', frame)
        i = i + 1

cap.release()  # 关闭视频捕获器
cv2.destroyAllWindows()  # 关闭所有窗口
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
<details><summary>可能出现的问题</summary>
 
`RecursionError: maximum recursion depth exceeded`
  * 解决步骤1，在xx.spec文件中添加如下代码,并保存  
  ```python
  import sys
  sys.setrecursionlimit(1000000)
  ```
  * 解决步骤2，在终端执行以下命令  
  `pyinstaller -F xx.spec`
  </details>
  
<span id="python彩蛋"></span>
## python彩蛋
```python
'''
author:fangchao
date:2019/6/4

content:python彩蛋
'''

# 彩蛋一
import __hello__
'''
Hello world!
'''

# 彩蛋二
import this
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

# 彩蛋三
import antigravity
'''
$输出反重力图像$
'''
```
