'''
author:fangchao
date:2019/10/9

content:ip地址归属地自动查询
'''

import requests

url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '211.162.81.67')
    r.raise_for_status()  # 判断是否页面可获取
    r.encoding = r.apparent_encoding  # 将页面中的数据解析成可读的编码
    print(r.text[-500:])
except:
    print("爬取失败")

"""
mit" value="查询" class="form-btn" />
					</form>
				</div>
				<div class="query-hd">ip138.com IP查询(搜索IP地址的地理位置)</div>
				<h1 class="query">您查询的IP：211.162.81.67</h1><p class="result">本站主数据：江苏省南京市  长城宽带</p><p class="result">参考数据一：广东省惠州市 长城宽带</p>

			</div>
		</div>

		<div class="footer">
			<a href="http://www.miitbeian.gov.cn/" rel="nofollow" target="_blank">沪ICP备10013467号-1</a>
		</div>
	</div>

	<script type="text/javascript" src="/script/common.js"></script></body>
</html>
"""
