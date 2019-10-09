'''
author:fangchao
date:2019/10/9

content:亚马逊商品页面爬取_修改User-Agent
'''

import requests

url = "https://www.amazon.cn/dp/B000NI2RF0?ref_=Oct_RecCard_dsk_asin1&pf_rd_r=CXTBQCSNVF2QRHAQ6YKV&pf_rd_p=d7526bc5-3640-48d5-8d6b-448fefacc51e&pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-4"
r = requests.get(url)
print(r.status_code)  # 直接 503访问错误，网站限制了爬虫的头部User_Agent
print(r.request.headers)
"""
{'User-Agent': 'python-requests/2.18.4', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
"""

# 修改User-Agent后爬取
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    # r = requests.get(url)  # 直接爬取,爬取失败;503错误
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")
