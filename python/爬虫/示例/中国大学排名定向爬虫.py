'''
author:fangchao
date:2019/10/9

content:中国大学排名定向爬虫
'''

import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(u_list, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            u_list.append([tds[0].string, tds[1].string, tds[2].string])


# # 原始打印出现中文不对齐问题
# def printUnivList(u_list, num):
#     print("{:^10}\t{:^10}\t{:^10}".format("排名", "学校名称", "总分"))
#     for i in range(num):
#         u = u_list[i]
#         print("{:^10}\t{:^10}\t{:^10}".format(u[0], u[1], u[2]))

# 打印格式优化
def printUnivList(u_list, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = u_list[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    u_info = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(u_info, html)
    printUnivList(u_info, 20)  # 20 univs


if __name__ == '__main__':
    main()

"""
优化前:
    排名    	   学校名称   	    总分    
    1     	   清华大学   	    北京    
    2     	   北京大学   	    北京    
    3     	   浙江大学   	    浙江    
    4     	  上海交通大学  	    上海    
    5     	   复旦大学   	    上海    
    6     	 中国科学技术大学 	    安徽    
    7     	  华中科技大学  	    湖北    
    7     	   南京大学   	    江苏    
    9     	   中山大学   	    广东    
    10    	 哈尔滨工业大学  	   黑龙江    
    11    	 北京航空航天大学 	    北京    
    12    	   武汉大学   	    湖北    
    13    	   同济大学   	    上海    
    14    	  西安交通大学  	    陕西    
    15    	   四川大学   	    四川    
    16    	  北京理工大学  	    北京    
    17    	   东南大学   	    江苏    
    18    	   南开大学   	    天津    
    19    	   天津大学   	    天津    
    20    	  华南理工大学  	    广东 
    

优化后:    
    排名    	　　　学校名称　　　	    总分    
    1     	　　　清华大学　　　	    北京    
    2     	　　　北京大学　　　	    北京    
    3     	　　　浙江大学　　　	    浙江    
    4     	　　上海交通大学　　	    上海    
    5     	　　　复旦大学　　　	    上海    
    6     	　中国科学技术大学　	    安徽    
    7     	　　华中科技大学　　	    湖北    
    7     	　　　南京大学　　　	    江苏    
    9     	　　　中山大学　　　	    广东    
    10    	　哈尔滨工业大学　　	   黑龙江    
    11    	　北京航空航天大学　	    北京    
    12    	　　　武汉大学　　　	    湖北    
    13    	　　　同济大学　　　	    上海    
    14    	　　西安交通大学　　	    陕西    
    15    	　　　四川大学　　　	    四川    
    16    	　　北京理工大学　　	    北京    
    17    	　　　东南大学　　　	    江苏    
    18    	　　　南开大学　　　	    天津    
    19    	　　　天津大学　　　	    天津    
    20    	　　华南理工大学　　	    广东 
"""
