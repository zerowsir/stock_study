# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/4'
"""

import pandas as pd
import numpy as np

def reinstate(symbol):
	data_df = pd.read_csv('F:/Stock_Data/stock_data/{}.csv'.format(symbol),
	                      encoding='gbk')
	data_df['复权价'] = data_df['收盘价']
	bonus_df = pd.read_csv('F:/Stock_Data/bonus/{}.csv'.format(symbol),
	                      encoding='gbk')
	info_df = pd.read_csv('F:/Stock_Data/stock_info.csv',
	                      encoding='gbk')
	name = info_df['NAME'][info_df['SYMBOL'] == int(symbol)]
	name = name[0]
	print(name)
	data_df = data_df.drop(data_df[data_df['名称'] != name].index)
	for row in bonus_df.iterrows():
		bonus = row[1]
		print(bonus)
		offer = 0 if bonus['送股']=='--' else int(bonus['送股'])
		transfer = 0 if bonus['转增']=='--' else int(bonus['转增'])
		dividend = 0. if bonus['派息']=='--' else float(bonus['派息'])
		ex_dividend_date = bonus['除权除息日']
		bonus_list_date = bonus['红股上市日']
		print(offer, transfer, dividend, ex_dividend_date, bonus_list_date)
		if (ex_dividend_date != '--') & (bonus_list_date != '--'):
			data_df['复权价'] = np.where(data_df['日期'] < ex_dividend_date, data_df['复权价'] + dividend, data_df['复权价'])
			data_df['复权价'] = np.where(data_df['日期'] < ex_dividend_date, data_df['复权价'] * 10 / (10 + transfer + offer),
			                          data_df['复权价'])
		elif ex_dividend_date != '--':
			data_df['复权价'] = np.where(data_df['日期'] < ex_dividend_date, data_df['复权价'] + dividend, data_df['复权价'])
		elif bonus_list_date != '--':
			data_df['复权价'] = np.where(data_df['日期'] < ex_dividend_date, data_df['复权价'] * 10 / (10 + transfer + offer), data_df['复权价'])
			
		data_df.to_csv('test.csv', encoding='gbk')
		

def cal_MA(symbol):
	data_df = pd.read_csv('F:/Stock_Data/stock_data/{}.csv'.format(symbol),
	                      encoding='gbk')
	data_df['MA5'] = data_df['收盘价'].rolling(window=5).mean()
	data_df['MA20'] = data_df['收盘价'].rolling(window=20).mean()
	data_df['MA60'] = data_df['收盘价'].rolling(window=60).mean()
	data_df['MA120'] = data_df['收盘价'].rolling(window=120).mean()
	print(data_df[['MA120', 'MA60', 'MA20', 'MA5']])
	
def main():
	# cal_MA('000001')
	reinstate('000001')
	
if __name__ == '__main__':
    main()