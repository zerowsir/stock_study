# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/8/3'
"""

import pandas as pd
import requests
from lxml import etree

info_df = pd.read_csv('F:/Stock_Data/stock_info.csv', encoding='gbk')
for row in info_df.iterrows():
	symbol = row[1]['SYMBOL']
	url = 'http://quotes.money.163.com/trade/lsjysj_{}.html'.format('{:0>6}'.format(symbol))
	response = requests.get(url=url)
	html = response.content.decode('utf8')
	data = etree.HTML(html)
	columns = data.xpath('/html/body/div[2]/div[4]/table/thead/tr/th/text()')
	trs = data.xpath('/html/body/div[2]/div[4]/table/tr')
	data_df = pd.DataFrame(columns=columns)
	for tr in trs:
		row = tr.xpath('./td/text()')
		data = {}
		for i in range(len(columns)):
			data[columns[i]] = row[i]
		data_df = data_df.append(data, ignore_index=True)
		data_df = data_df.sort_values(by='日期')
	
	data_df_saved = pd.read_csv('F:/Stock_Data/stock_data/{}.csv'.format('{:0>6}'.format(symbol)),
	                            encoding='gbk')
	print(data_df)
	print(data_df_saved)
	break
	
	
	