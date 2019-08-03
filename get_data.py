# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/4'
"""

from Classes.Info import Stock_info, Index_info
from Classes.Data import Stock_data, Index_data
from Classes.Bonus import Bonus
from multiprocessing import Pool
import threading

def get_bonus_data(symbol):
	bonus = Bonus(symbol)
	bonus.get_bonus()
	bonus.get_allot()
	bonus.get_issue()
	bonus.get_financing()

def get_all_bonus_data():
	stock_info = Stock_info()
	info_df = stock_info.data_df
	pool = Pool(10)
	for row in info_df.iterrows():
		symbol = row[1]['SYMBOL']
		pool.apply_async(func=get_bonus_data, args=(symbol,))
	pool.close()
	pool.join()

def get_index_data(code):
	index_data = Index_data()
	index_data.get_data(code)

def get_all_index_data():
	index_info = Index_info()
	info_df = index_info.data_df
	pool = Pool(10)
	for row in info_df.iterrows():
		code = row[1]['CODE']
		pool.apply_async(func=get_index_data, args=(code,))
	pool.close()
	pool.join()

def get_stock_data(code):
	stock_data = Stock_data()
	stock_data.get_data(code)

def get_all_stock_data():
	stock_info = Stock_info()
	info_df = stock_info.data_df
	pool = Pool(10)
	for row in info_df.iterrows():
		code = row[1]['CODE']
		pool.apply_async(func=get_stock_data, args=(code,))
	pool.close()
	pool.join()

def get_info():
	stock_info = Stock_info()
	index_info = Index_info()
	stock_info.get_data()
	index_info.get_data()

if __name__ == '__main__':
    get_info()
    get_all_stock_data()
    get_all_index_data()
    get_all_bonus_data()
