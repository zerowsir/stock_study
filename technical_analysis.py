# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/3'
"""

import Config
import pandas as pd

data_path = Config.STOCK_DATA_PATH
index_path = Config.INDEX_PATH
technical_analysis_path = Config.TECHNICAL_ANALYSIS_PATH
bonus_path = Config.BONUS_PATH
allot_path = Config.ALLOT_SHARES_PATH
info_path = Config.STOCK_INFO_PATH

def reinstate():
	stock_info_df = pd.read_csv(info_path + 'stocks_info.csv', encoding='gbk')
	for row in stock_info_df.iterrows():
		symbol ='{:0>6}'.format(row[1]['SYMBOL'])
		

if __name__ == '__main__':
	reinstate()
