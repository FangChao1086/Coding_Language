## Python爬虫

* [request库](#request库)
* [BeautifulSoup](#BeautifulSoup)
* [示例](#示例)

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
## BeautifulSoup
* 解析  
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/BeautifulSoup.jpg"></div>  

* 内容遍历：下行，上行，平行（平行发生在同一个父亲节点下的各节点间）
<div align=center><img src="https://github.com/FangChao1086/Coding_language/blob/master/依赖文件/标签树的遍历.jpg"></div>  

<span id="示例"></span>
## 示例 [详细](https://github.com/FangChao1086/coding_language/tree/master/python/爬虫/示例)
* 1.京东商品页面_简单获取页面
* 2.亚马逊商品页面_修改User-Agent
* 3.百度搜索关键词提交
* 4.网络图片的爬取与存储
* 5.ip地址归属地自动查询
