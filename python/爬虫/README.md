## Python爬虫

* [request库](#request库)
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

<span id="示例"></span>
## 示例
### 1.京东商品页面的爬取
```py
import requests

url = "https://item.jd.com/100003294619.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")

"""
<!DOCTYPE HTML>
<html lang="zh-CN">
<head>
    <!--yushou-->
    <meta http-equiv="Content-Type" content="text/html; charset=gbk" />
    <title>【海尔JSQ31-16WJS2(12T)】海尔（Haier）16升零冷水燃气热水器天然气 水气双调恒温智能浴缸注水 8年质保 JSQ31-16WJS2(12T)【行情 报价 价格 评测】-京东</title>
    <meta name="keywords" content="HaierJSQ31-16WJS2(12T),海尔JSQ31-16WJS2(12T),海尔JSQ31-16WJS2(12T)报价,HaierJSQ31-16WJS2(12T)报价"/>
    <meta name="description" content="【海尔JSQ31-16WJS2(12T)】京东JD.COM提供海尔JSQ31-16WJS2(12T)正品行货，并包括HaierJSQ31-16WJS2(12T)网购指南，以及海尔JSQ31-16WJS2(12T)图片、JSQ31-16WJS2(12T)参数、JSQ31-16WJS2(12T)评论、JSQ31-16WJS2(12T)心得、JSQ31-16WJS2(12T)技巧等信息，网购海尔JSQ31-16WJS2(12T)上京东,放心又轻松" />
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="mobile-agent" content="format=xhtml; url=//item.m.jd.com/product/100003294619.html">
    <meta http-equiv="mobile-agent" content="format=html5; url=//item.m.jd.com/product/100003294619.html">
    <meta http-equiv="X-UA-Compatible" content="IE=Edge">
    <link rel="canonical" hr
"""
```
