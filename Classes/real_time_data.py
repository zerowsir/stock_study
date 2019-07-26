# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/24'
"""

import requests
import re
import pandas as pd
from lxml import etree

URL = 'http://api.money.126.net/data/feed/{},money.api'
HEADERS = {
	'Referer': 'http://quotes.money.163.com/0601326.html',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
	}

response = requests.get(url=URL.format('0601390'), headers=HEADERS)
data_str = response.content.decode('gbk')
reg = re.compile(r"\{[^{}]*\}")
data_str = reg.search(data_str).group(0)
data_dict = eval(data_str)

re_keys = list(data_dict.keys())
new_keys = ['查询代码', '涨跌幅', '最高', '卖三量', '卖二量', '卖五量', '卖四量', '现价', '今开', '买五价', '买四价', '买三价', '买二价', '买一价', '最低', '涨跌', '类型', '股票代码', '状态', '卖四价', '买三量', '买二量', '买一量', '更新时间', '买五量', '买四量', '昨收', '卖一量', '卖五价', '成交量', '卖一价', '股票名称', '卖三价', '卖二价', '箭头', '时刻', '成交额']
data_df = pd.DataFrame(columns=new_keys)
data = {}
for i in range(len(re_keys)):
	data[new_keys[i]] = data_dict[re_keys[i]]
data_df = data_df.append(data,ignore_index=True)
print(data_df)