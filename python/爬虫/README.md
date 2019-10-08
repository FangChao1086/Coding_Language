## Python爬虫

* [request库](#request库)

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
