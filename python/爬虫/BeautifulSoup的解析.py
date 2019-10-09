'''
author:fangchao
date:2019/10/9

content:Beautiful Soup4的解析
'''

import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())
"""
<html>
 <head>
  <title>
   This is a python demo page
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The demo python introduces several python courses.
   </b>
  </p>
  <p class="course">
   Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:
   <a class="py1" href="http://www.icourse163.org/course/BIT-268001" id="link1">
    Basic Python
   </a>
   and
   <a class="py2" href="http://www.icourse163.org/course/BIT-1001870001" id="link2">
    Advanced Python
   </a>
   .
  </p>
 </body>
</html>
"""

# 获取html中的所有的链接
for link in soup.find_all('a'):
    print(link.get('href'))
"""
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
"""
