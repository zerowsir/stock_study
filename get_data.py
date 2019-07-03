# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/2'
"""
import requests
import io
import json
import pandas as pd
from Stock_class import Stock_info, Stock, Index_info, Index, Bonus
import Config
from multiprocessing import Pool

def get_bonus_data(symbol):
	bonus = Bonus(symbol)
	bonus.get_data()

def get_bonus():
	stock_df = pd.read_csv(Config.STOCK_INFO_PATH + 'stocks_info.csv', encoding='gbk')
	pool = Pool(10)
	for row in stock_df.iterrows():
		symbol = '{:0>6}'.format(row[1]['SYMBOL'])
		pool.apply_async(func=get_bonus_data, args=(symbol,))
	pool.close()
	pool.join()
	print('股票分红信息全部处理完成！')

def get_index_data(row):
	code = '{:0>7}'.format(row['CODE'])
	sybmol = '{:0>6}'.format(row['SYMBOL'])
	index = Index(sybmol, code)
	index.get_data()

def get_index_history_data():
	index_info_df = pd.read_csv(Config.INDEX_INFO_PATH + 'index_info.csv', encoding='gbk')
	pool = Pool(10)
	for _, row in index_info_df.iterrows():
		pool.apply_async(func=get_index_data, args=(row,))
	pool.close()
	pool.join()
	print('全部数据获取成功！')

def get_all_index():
	url = Config.GET_ALL_INDEX_URL
	headers = Config.GET_ALL_INDEX_HEADERS
	params = Config.GET_ALL_INDEX_PARAMS
	
	response = requests.get(url, params=params, headers=headers)
	params['count'] =json.loads(io.StringIO(response.text).read())['total']
	response = requests.get(url, params=params, headers=headers)
	all_index_info_json = json.loads(io.StringIO(response.text).read())
	all_index_infos = all_index_info_json['list']
	
	columns = ['CODE', 'HIGH', 'LOW', 'NAME', 'OPEN', 'PERCENT', 'PRICE', 'SYMBOL', 'TURNOVER', 'UPDOWN', 'VOLUME', 'YESTCLOSE', 'no', 'zhenfu']
	
	all_index_info_df = pd.DataFrame(columns=columns)
	print('正在处理全部指数信息……')
	for i in range(len(all_index_infos)):
		
		all_index_info_df = all_index_info_df.append(Index_info(all_index_infos[i], i).to_dataframe(),
		                                             ignore_index=True, sort=True)
	print('正在保存全部指数信息……')
	all_index_info_df.to_csv(Config.INDEX_INFO_PATH + 'index_info.csv',
	                         encoding='gbk', index=False)
	print('全部指数信息处理完成！')
	
def get_stock_data(row):
	code = '{:0>7}'.format(row['CODE'])
	sybmol = '{:0>6}'.format(row['SYMBOL'])
	stock = Stock(sybmol, code)
	stock.get_data()

def get_stock_history_data():
	stock_info_df = pd.read_csv(Config.STOCK_INFO_PATH + 'stocks_info.csv', encoding='gbk')
	pool = Pool(10)
	for _, row in stock_info_df.iterrows():
		pool.apply_async(func=get_stock_data, args=(row,))
	pool.close()
	pool.join()
	print('全部数据获取成功！')
	
def get_all_stock_info():
	params = Config.GET_STOCK_INFO_PARAMS
	headers = Config.GET_STOCK_INFO_HEADERS
	url = Config.GET_STOCK_INFO_URL
	print('正在获取全部股票信息……')
	response = requests.get(url, params=params, headers=headers)
	
	all_stock_info_json = json.loads(io.StringIO(response.text).read())
	params['count'] = all_stock_info_json['total']
	
	response = requests.get(url, params=params, headers=headers)
	
	all_stock_info_json = json.loads(io.StringIO(response.text).read())
	all_stock_infos = all_stock_info_json['list']

	columns = ['CODE', 'FIVE_MINUTE', 'HIGH', 'HS', 'LB', 'LOW', 'MCAP', 'MFRATIO2', 'MFRATIO10', 'MFSUM', 'NAME',
	           'OPEN', 'PE', 'PERCENT', 'PRICE', 'SNAME', 'SYMBOL', 'TCAP', 'TURNOVER', 'UPDOWN', 'VOLUME', 'WB',
	           'YESTCLOSE', 'ZF']
	all_stock_info_df = pd.DataFrame(columns=columns)
	print('正在处理全部股票信息……')
	for i in range(len(all_stock_infos)):

		all_stock_info_df = all_stock_info_df.append(Stock_info(all_stock_infos[i], i).to_dataframe(),
		                                             ignore_index=True, sort=True)
	print('正在保存全部股票信息……')
	all_stock_info_df.to_csv(Config.STOCK_INFO_PATH + 'stocks_info.csv',
	                         encoding='gbk',index=False)
	print('全部股票信息处理完成！')

if __name__ == '__main__':
	get_all_stock_info()
	get_stock_history_data()
	get_all_index()
	get_index_history_data()
	get_bonus()