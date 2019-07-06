# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/4'
"""

import requests
from lxml import etree
import pandas as pd

class Bonus(object):
	URL = 'http://quotes.money.163.com/f10/fhpg_{}.html'
	HEADERS = {}
	file_path = ''
	def __init__(self, symbol):
		self.symbol = symbol
		self.URL = self.URL.format(symbol)
		print('正在获取{}数据……'.format(symbol))
		response = requests.get(url=self.URL,
		                        headers=self.HEADERS)
		self.html = etree.HTML(response.text)
		
	def get_data(self, content='bonus', num_div='4', num_col=8):
		if content == 'bonus':
			title = self.html.xpath('/html/body/div[2]/div[4]/table/thead/tr/th/text()')
			del title[2]
			title[2], title[3], title[4], title[5], title[6], title[7] =title[5], title[6], title[7], title[2], title[3], title[4]
			columns = title
		else:
			columns = self.html.xpath('/html/body/div[2]/div[{}]/table/thead/tr/th/text()'.format(num_div))
		
		tds = self.html.xpath('/html/body/div[2]/div[{}]/table/tr/td'.format(num_div))
		data_list = []
		for t in tds:
			data_list.append(t.text)
		if not ('暂无数据' in data_list):
			data = pd.DataFrame(columns=columns)
			for i in range(0, len(data_list), num_col):
				data_dict = {}
				for j in range(num_col):
					data_dict[columns[j]] = data_list[i + j]
				data_df = pd.DataFrame(data_dict, columns=columns, index=[i // num_col])
				data = data.append(data_df)
			data.to_csv(self.file_path + self.symbol + '.csv', encoding='gbk', index=False)
		else:
			print('暂无数据')
		print('{}数据处理完成'.format(self.symbol))
		
	def get_bonus(self):
		self.file_path = 'F:/Stock_Data/bonus/'
		self.get_data(content='bonus', num_div='4', num_col=8)

	def get_allot(self):
		self.file_path = 'F:/Stock_Data/allot/'
		self.get_data(content='allot', num_div='6', num_col=8)

	def get_issue(self):
		self.file_path = 'F:/Stock_Data/issue/'
		self.get_data(content='issue', num_div='8', num_col=8)

	def get_financing(self):
		self.file_path = 'F:/Stock_Data/financing/'
		self.get_data(content='finacing', num_div='10', num_col=6)
