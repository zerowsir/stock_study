# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/12'
"""

import pandas as pd
from multiprocessing import Pool


class convert_to_PyAlgoTrade(object):
	symbol = ''
	source_path = 'F:/Stock_Data/analysis/'
	destination_path = 'F:/Stock_Data/PyAlgoTrade/'
	drop_labels = ['股票代码', '名称', '前收盘', '涨跌额', '涨跌幅', '换手率', '成交金额', '总市值', '流通市值']
	columns = ['Date Time', 'Close', 'High', 'Low', 'Open', 'Volume', 'Adj Close']
	
	def __init__(self, symbol):
		self.symbol = symbol
	
	def convert(self):
		data_df = pd.read_csv(self.source_path + self.symbol + '.csv',
		                      encoding='gbk')
		
		for label in self.drop_labels:
			data_df = data_df.drop(label, axis=1)
		data_df.columns = self.columns
		
		data_df.to_csv(self.destination_path + self.symbol + '.csv',
		               encoding='gbk',
		               index=False)

def convert_PyAloTrade(symbol):
	print('正在转换{}的数据...'.format(symbol))
	convert = convert_to_PyAlgoTrade(symbol)
	convert.convert()
	print('{}的数据转换完成！'.format(symbol))

def main():
	info_df = pd.read_csv('F:/Stock_Data/stock_info.csv',
	                      encoding='gbk')
	symbols = info_df['SYMBOL'].values
	pool = Pool(10)
	for symbol in symbols:
		symbol = '{:0>6}'.format(symbol)
		pool.apply_async(func=convert_PyAloTrade, args=(symbol,))
	pool.close()
	pool.join()
	print('全部PyAlgoTrade数据转换完成...')

if __name__ == '__main__':
    main()