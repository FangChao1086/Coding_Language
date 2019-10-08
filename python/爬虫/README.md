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
