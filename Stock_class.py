# coding=utf-8
"""
　　__title__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/2'
"""

import requests
import pandas as pd
import Config
import datetime
from lxml import etree

class Bonus:
	def __init__(self, symbol):
		self.symbol = symbol
	
	def get_data(self):
		url = Config.GET_BONUS_URL.format(self.symbol)
		response = requests.get(url)
		text = etree.HTML(response.text)
		title = text.xpath('/html/body/div[2]/div[4]/table/thead/tr[1]/th/text()')
		sub_title = text.xpath('//body/div/div/table/thead/tr[2]/th/text()')
		columns = title[:2] + sub_title + title[3:]
		
		print('正在处理{}的分红信息……'.format(self.symbol))
		data_list = text.xpath('/html/body/div[2]/div[4]/table[1]/tr/td/text()')
		data = pd.DataFrame(columns=columns)
		if not ('暂无数据' in data_list):
			for i in range(0, len(data_list), 8):
				data_dict = {}
				for j in range(8):
					data_dict[columns[j]] = data_list[i + j]
				data_df = pd.DataFrame(data_dict, columns=columns, index=[i // 8])
				data = data.append(data_df)
			data.to_csv(Config.BONUS_PATH + self.symbol + '.csv', encoding='gbk', index=False)
		
		print('正在处理{}的配股信息……'.format(self.symbol))
		columns = text.xpath('/html/body/div[2]/div[6]/table/thead/tr/th/text()')
		tds = text.xpath('/html/body/div[2]/div[6]/table/tr/td')
		data_list = []
		for t in tds:
			data_list.append(t.text)
		if not ('暂无数据' in data_list):
			data = pd.DataFrame(columns=columns)
			for i in range(0, len(data_list), 8):
				data_dict = {}
				for j in range(8):
					data_dict[columns[j]] = data_list[i + j]
				data_df = pd.DataFrame(data_dict, columns=columns, index=[i // 8])
				data = data.append(data_df)
			data.to_csv(Config.ALLOT_SHARES_PATH + self.symbol + '.csv', encoding='gbk', index=False)
		
		print('正在处理{}的增发信息……'.format(self.symbol))
		columns = text.xpath('/html/body/div[2]/div[8]/table/thead/tr/th/text()')
		tds = text.xpath('/html/body/div[2]/div[8]/table/tr/td')
		data_list = []
		for t in tds:
			data_list.append(t.text)
		if 	not('暂无数据' in data_list):
			data = pd.DataFrame(columns=columns)
			for i in range(0, len(data_list), 8):
				data_dict = {}
				for j in range(8):
					data_dict[columns[j]] = data_list[i + j]
				data_df = pd.DataFrame(data_dict, columns=columns, index=[i // 8])
				data = data.append(data_df)
			data.to_csv(Config.ISSUE_PATH + self.symbol + '.csv', encoding='gbk', index=False)
		
		print('正在处理{}的融资信息……'.format(self.symbol))
		columns = text.xpath('/html/body/div[2]/div[10]/table/thead/tr/th/text()')
		tds = text.xpath('/html/body/div[2]/div[10]/table/tr/td')
		data_list = []
		for t in tds:
			data_list.append(t.text)
		if not ('暂无数据' in data_list):
			data = pd.DataFrame(columns=columns)
			for i in range(0, len(data_list), 6):
				data_dict = {}
				for j in range(6):
					data_dict[columns[j]] = data_list[i + j]
				data_df = pd.DataFrame(data_dict, columns=columns, index=[i // 6])
				data = data.append(data_df)
			data.to_csv(Config.FINANCING_PATH + self.symbol + '.csv', encoding='gbk', index=False)
		
class Index:
	params = Config.GET_INDEX_PARAMS
	params['end'] = datetime.datetime.strftime(datetime.date.today(), '%Y%m%d')
	headers = Config.GET_INDEX_HEADERS
	url = Config.GET_INDEX_URL
	
	def __init__(self, symbol, code):
		self.symbol = symbol
		self.code = code
	
	def get_data(self, ):
		self.params['code'] = self.code
		print('正从网络获取{}数据……'.format(self.symbol))
		response = requests.get(self.url, params=self.params, headers=self.headers)
		with open(Config.INDEX_PATH + self.symbol + '.csv', 'w', newline='') as f:
			f.write(response.content.decode('gbk'))
		print('正在处理{}数据……'.format(self.symbol))
		data_df = pd.read_csv(Config.INDEX_PATH + self.symbol + '.csv', encoding='gbk')
		data_df = data_df.sort_values(by='日期', ascending=True)
		print('正在保存{}数据……'.format(self.symbol))
		data_df.to_csv(Config.INDEX_PATH + self.symbol + '.csv',
		               index=False, encoding='gbk')
		print('{}数据保存完成！！'.format(self.symbol))


class Index_info:
	def __init__(self, index_info, index=0):
		self.code = index_info['CODE']
		self.high = index_info['HIGH']
		self.low = index_info['LOW']
		self.name = index_info['NAME']
		self.open = index_info['OPEN']
		self.percent = index_info['PERCENT']
		self.price = index_info['PRICE']
		self.symbol = index_info['SYMBOL']
		self.turnover = index_info['TURNOVER']
		self.updown = index_info['UPDOWN']
		self.volume = index_info['VOLUME']
		self.yestclose = index_info['YESTCLOSE']
		self.zhenfu = index_info['zhenfu']
		self.index = index
	
	def to_dataframe(self):
		index_dict = {}
		index_dict['CODE'] = self.code
		index_dict['HIGH'] = self.high
		index_dict['LOW'] = self.low
		index_dict['NAME'] = self.name
		index_dict['OPEN'] = self.open
		index_dict['PERCENT'] = self.percent
		index_dict['PRICE'] = self.price
		index_dict['SYMBOL'] = self.symbol
		index_dict['TURNOVER'] = self.turnover
		index_dict['UPDOWN'] = self.updown
		index_dict['VOLUME'] = self.volume
		index_dict['YESTCLOSE'] = self.yestclose
		index_dict['zhenfu'] = self.zhenfu
		index_df = pd.DataFrame(index_dict, index=[self.index])
		return index_df


class Stock:
	params = Config.GET_HISTORY_DATA_PARAMS
	params['end'] = datetime.datetime.strftime(datetime.date.today(), '%Y%m%d')
	headers = Config.GET_HISTORY_DATA_HEADERS
	url = Config.GET_HISTORY_DATA_URL
	
	def __init__(self, symbol, code):
		self.symbol = symbol
		self.code = code
	
	def get_data(self, ):
		self.params['code'] = self.code
		print('正从网络获取{}数据……'.format(self.symbol))
		response = requests.get(self.url, params=self.params, headers=self.headers)
		with open(Config.STOCK_DATA_PATH + self.symbol + '.csv', 'w', newline='') as f:
			f.write(response.content.decode('gbk'))
		print('正在处理{}数据……'.format(self.symbol))
		data_df = pd.read_csv(Config.STOCK_DATA_PATH + self.symbol + '.csv', encoding='gbk')
		data_df = data_df.sort_values(by='日期', ascending=True)
		print('正在保存{}数据……'.format(self.symbol))
		data_df.to_csv(Config.STOCK_DATA_PATH + self.symbol + '.csv',
		               index=False, encoding='gbk')
		print('{}数据保存完成！！'.format(self.symbol))
		
		
class Mfratio:
	def __init__(self, mfratio):
		self.mfratio2 = mfratio['MFRATIO2']
		self.mfratio10 = mfratio['MFRATIO10']


class Stock_info:
	def __init__(self, stock_info, index=0):
		self.code = stock_info['CODE']
		self.five_minute = stock_info['FIVE_MINUTE']
		self.high = stock_info['HIGH']
		self.hs = stock_info['HS']
		self.lb = stock_info['LB']
		self.low = stock_info['LOW']
		self.mcap = stock_info['MCAP']
		self.mfratio = Mfratio(stock_info['MFRATIO'])
		self.mfsum = stock_info['MFSUM']
		self.name = stock_info['NAME']
		self.open = stock_info['OPEN']
		self.pe = stock_info['PE']
		self.percent = stock_info['PERCENT']
		self.price = stock_info['PRICE']
		self.sname = stock_info['SNAME']
		self.symbol = stock_info['SYMBOL']
		self.tcap = stock_info['TCAP']
		self.turnover = stock_info['TURNOVER']
		self.updown = stock_info['UPDOWN']
		self.volume = stock_info['VOLUME']
		self.wb = stock_info['WB']
		self.yestclose = stock_info['YESTCLOSE']
		self.zf = stock_info['ZF']
		self.index = index
	
	def to_dataframe(self):
		stock_dict = {}
		stock_dict['CODE'] = self.code
		stock_dict['FIVE_MINUTE'] = self.five_minute
		stock_dict['HIGH'] = self.high
		stock_dict['HS'] = self.hs
		stock_dict['LB'] = self.lb
		stock_dict['LOW'] = self.low
		stock_dict['MCAP'] = self.mcap
		stock_dict['MFRATIO2'] = self.mfratio.mfratio2
		stock_dict['MFRATIO10'] = self.mfratio.mfratio10
		stock_dict['MFSUM'] = self.mfsum
		stock_dict['NAME'] = self.name
		stock_dict['OPEN'] = self.open
		stock_dict['PE'] = self.pe
		stock_dict['PERCENT'] = self.percent
		stock_dict['PRICE'] = self.price
		stock_dict['SNAME'] = self.sname
		stock_dict['SYMBOL'] = self.symbol
		stock_dict['TCAP'] = self.tcap
		stock_dict['TURNOVER'] = self.turnover
		stock_dict['UPDOWN'] = self.updown
		stock_dict['VOLUME'] = self.volume
		stock_dict['WB'] = self.wb
		stock_dict['YESTCLOSE'] = self.yestclose
		stock_dict['ZF'] = self.zf
		stock_df = pd.DataFrame(stock_dict, index=[self.index])
		return stock_df
	