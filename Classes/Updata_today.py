# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/5'
"""
import pandas as pd
import datetime

class Update_today(object):
	symbol = ''
	file_path = 'F:/Stock_Data/stock_data/'
	
	
	def __init__(self, symbol):
		self.symbol = symbol
		
	def update(self, recode):
		self.data_df = pd.read_csv(self.file_path + symbol + '.csv',
		                           encoding='gbk')
		print(max(self.data_df['日期']))
		self.data_df = self.data_df.append(Recode(recode).recode,
		                                   ignore_index=True)
		self.data_df = self.data_df.sort_values(by='日期')
		
		# self.data_df.to_csv(self.file_path + symbol + '.csv', encoding='gbk', index=False)
		
		
class Recode(object):
	recode = {}
	def __init__(self, recode):
		self.recode['日期'] = datetime.date.strftime(datetime.date.today(), '%Y%m%d')
		self.recode['股票代码'] = recode['SYMBOL']
		self.recode['名称'] = recode['NAME']
		self.recode['最高价'] = recode['HIGH']
		self.recode['收盘价'] = recode['PRICE']
		self.recode['最低价'] = recode['LOW']
		self.recode['开盘价'] = recode['OPEN']
		self.recode['前收盘'] = recode['YESTCLOSE']
		self.recode['涨跌额'] = recode['UPDOWN']
		self.recode['涨跌幅'] = recode['PERCENT'] / 100
		self.recode['换手率'] = recode['HS'] * 100
		self.recode['成交量'] = recode['VOLUME']
		self.recode['成交金额'] = recode['TURNOVER']
		self.recode['总市值'] = recode['TCAP']
		self.recode['流通市值'] = recode['MCAP']
		
		
info_df = pd.read_csv('F:/Stock_Data/stock_info.csv',
                      encoding='gbk')
for row in info_df.iterrows():
	symbol = '{:0>6}'.format(row[1]['SYMBOL'])
	recode = row[1]
	stock = Update_today(symbol)
	stock.update(recode)
	break
