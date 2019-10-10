## Python爬虫

* [request库](#request库)
* [BeautifulSoup](#BeautifulSoup)
* [正则表达式](#正则表达式)
* [Scrapy](#Scrapy)
* [示例](#示例)
* [视频教程](https://www.bilibili.com/video/av9784617?from=search&seid=9025437944886247756)

<span id="request库"></span>
## request库  [官网地址](http://cn.python-requests.org/zh_CN/latest/)
* get方法
```py
import requests
r = request.get("http://www.baidu.com")
print(r.status_code)

"""
200
"""
```
* patch
  * 提交局部修改请求
  
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/Response对象.JPG"></div>

<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/Requests库的异常.JPG"></div>

<span id="BeautifulSoup"></span>
## BeautifulSoup  [官网地址](https://beautifulsoup.readthedocs.io/zh_CN/latest/)  
* [解析代码](https://github.com/FangChao1086/coding_language/tree/master/python/爬虫/BeautifulSoup的解析.py)
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/BeautifulSoup.jpg"></div>  

* 内容遍历：下行，上行，平行（平行发生在同一个父亲节点下的各节点间）
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/标签树的遍历.jpg"></div>  

<span id="正则表达式"></span>
## 正则表达式
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/正则表达式.png"></div>  

### 特殊
```
^[A-Za-z]+$          由26个字母组成的字符串
^[A-Za-z0-9]+$       由26个字母和数字组成的字符串
^-?\d+$              整数形式的字符串
^[0-9]*[1-9][0-9]*$  正整数形式的字符串
[1-9]\d{5}           中国境内邮政编码，6位
[\u4e00-\u9fa5]      匹配中文字符

ip地址匹配：
(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5]).){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])
```

<span id="Scrapy"></span>
## Scrapy
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/scrapy爬虫框架.jpg"></div>

<span id="示例"></span>
## 示例 [详细代码](https://github.com/FangChao1086/coding_language/tree/master/python/爬虫/示例)
* 1.京东商品页面_简单获取页面
* 2.亚马逊商品页面_修改User-Agent
* 3.百度搜索关键词提交
* 4.网络图片的爬取与存储
* 5.ip地址归属地自动查询
* [中国大学排名定向爬虫](https://github.com/FangChao1086/coding_language/tree/master/python/爬虫/示例/中国大学排名定向爬虫.py)
* [淘宝商品翻页爬取](https://github.com/FangChao1086/coding_language/tree/master/python/爬虫/示例/淘宝商品翻页爬取.py)
