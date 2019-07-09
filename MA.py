# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/4'
"""

import pandas as pd
import numpy as np

class data_handle(object):
	
	def __init__(self, symbol):
		self.symbol = symbol
		self.data_df = pd.read_csv('F:/Stock_Data/stock_data/{}.csv'.format(self.symbol),
		                      encoding='gbk')
		self.data_df = self.data_df.sort_values(by='日期')
		self.bonus_df = pd.read_csv('F:/Stock_Data/bonus/{}.csv'.format(self.symbol),
		                       encoding='gbk')
		self.info_df = pd.read_csv('F:/Stock_Data/stock_info.csv',
		                      encoding='gbk')
		
	def reinstate(self, source, dest):
		self.data_df[dest] = self.data_df[source]
		
		# name = self.info_df['NAME'][self.info_df['SYMBOL'] == int(self.symbol)]
		# name = name[0]
		# self.data_df = self.data_df.drop(self.data_df[self.data_df['名称'] != name].index)
		for row in self.bonus_df.iterrows():
			bonus = row[1]
			offer = 0 if bonus['送股']=='--' else int(bonus['送股'])
			transfer = 0 if bonus['转增']=='--' else int(bonus['转增'])
			dividend = 0. if bonus['派息']=='--' else float(bonus['派息'])
			ex_dividend_date = bonus['除权除息日']
			bonus_list_date = bonus['红股上市日']
			if (ex_dividend_date != '--') & (bonus_list_date != '--'):
				self.data_df[dest] = np.where(self.data_df['日期'] < ex_dividend_date,
				                              self.data_df[dest] + dividend,
				                              self.data_df[dest])
				self.data_df[dest] = np.where(self.data_df['日期'] < ex_dividend_date,
				                              self.data_df[dest] * 10 / (10 + transfer + offer),
				                              self.data_df[dest])
			elif ex_dividend_date != '--':
				self.data_df[dest] = np.where(self.data_df['日期'] < ex_dividend_date,
				                              self.data_df[dest] + dividend,
				                              self.data_df[dest])
			elif bonus_list_date != '--':
				self.data_df[dest] = np.where(self.data_df['日期'] < ex_dividend_date,
				                              self.data_df[dest] * 10 / (10 + transfer + offer),
				                              self.data_df[dest])
		
	def save(self):
		self.data_df.to_csv('F:/Stock_Data/analysis/{}.csv'.format(self.symbol),
			               encoding='gbk',
			               index=False)

	def cal_MA(self, source):
		self.data_df['MA5'] = self.data_df[source].rolling(window=5).mean()
		self.data_df['MA20'] = self.data_df[source].rolling(window=20).mean()
		self.data_df['MA60'] = self.data_df[source].rolling(window=60).mean()
		self.data_df['MA120'] = self.data_df[source].rolling(window=120).mean()
		
	def MACD(self, source):
		self.data_df['EMA12'] = self.data_df[source].rolling(window=12).mean()
		self.data_df['EMA26'] = self.data_df[source].rolling(window=26).mean()
		self.data_df['DIF'] = self.data_df['EMA12'] - self.data_df['EMA26']
		self.data_df['MACD'] = self.data_df['DIF'].rolling(window=9).mean()
	
	def KDJ(self, source, n):
		self.data_df['RSV'] = (self.data_df[source] - self.data_df[source].rolling(window=n).min()) / (self.data_df[source].rolling(window=n).max() - self.data_df[source].rolling(window=n).min()) * 100.
		self.data_df['K'] = 50
		self.data_df['D'] = 50
		self.data_df['K'] = self.data_df['K'].shift(1) * 2 / 3 + self.data_df['RSV'] / 3
		self.data_df['D'] = self.data_df['D'].shift(1) * 2 / 3 + self.data_df['K'] / 3
		self.data_df['J'] = 3 * self.data_df['D'] - 2 * self.data_df['K']
		
		
def main():
	data = data_handle('000001')
	data.reinstate('收盘价', '新收盘')
	data.reinstate('开盘价', '新开盘')
	data.reinstate('最高价', '新最高')
	data.reinstate('最低价', '新最低')
	data.cal_MA('新收盘')
	data.MACD('新收盘')
	data.KDJ('新收盘', 9)
	data.save()
	
if __name__ == '__main__':
    main()