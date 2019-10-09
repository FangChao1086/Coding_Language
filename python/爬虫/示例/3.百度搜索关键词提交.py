'''
author:fangchao
date:2019/10/9

content:百度搜索关键词提交
'''

import requests

keyword = "Python"
try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")

"""
http://www.baidu.com/s?wd=Python
434608
"""
