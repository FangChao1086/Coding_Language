# python
* [基础](#基础)
  * [输入](#输入)
* [extend与append的区别](#extend与append的区别)
* [浅拷贝与深拷贝](#浅拷贝与深拷贝)

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

<span id="extend与append的区别"></span>
# extend与append的区别
[extend与append的区别](https://www.cnblogs.com/tzuxung/p/5706245.html)

<span id="浅拷贝与深拷贝"></span>
# 浅拷贝与深拷贝
[浅拷贝与深拷贝](https://www.cnblogs.com/xueli/p/4952063.html)
