# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/4'
"""
import requests
import datetime
import pandas as pd
import csv
from io import StringIO

TODAY = datetime.date.strftime(datetime.date.today(), '%Y%m%d')

class Data(object):
	URL = ''
	PARAMS = {}
	HEADERS = {}
	file_path = ''
	
	def get_data(self, code, end=TODAY):
		self.PARAMS['code'] = code
		self.PARAMS['end'] = end
		print('正在获取{}数据……'.format(code))
		response = requests.get(url=self.URL,
		                        params=self.PARAMS,
		                        headers=self.HEADERS)
		print('正在处理{}数据...'.format(code))
		data_df = pd.read_csv(StringIO(response.text), skip_blank_lines=True)
		data_df = data_df.sort_values(by='日期')
		if data_df.empty:
			print('空数据', code)
		else:
			data_df.to_csv(self.file_path + str(code[1:]) + '.csv', encoding='gbk',index=False)
			print('{}数据处理完成！！'.format(code))
		
class Stock_data(Data):
	URL = 'http://quotes.money.163.com/service/chddata.html'
	PARAMS = {
		'code': '',
		'start': '19900101',
		'end': '',
		'fields': 'TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
		}
	HEADERS = {
		'Cookie': 'Province=0; City=0; UM_distinctid=16c05496622f1-00e8d8cb7044e48-4c312272-15f900-16c054966245cc; _ntes_nnid=0213f9288c03916f18ed2634a6a3506d,1563456793050; vjuids=1be4f793f.16c054a41b6.0.6b5b7a77d19a78; vjlast=1563456848.1563930352.13; vinfo_n_f_l_n3=ad2a50d90e25c7dc.1.4.1563456848324.1563950911150.1563963465898; usertrack=ezq0ZV03rush6S+BCCg6Ag==; _ntes_nuid=0213f9288c03916f18ed2634a6a3506d; NNSSPID=bcf860b5427949c599552390d570c1d0; _ntes_stock_recent_plate_=%7Chy006000%3A%E6%89%B9%E5%8F%91%E9%9B%B6%E5%94%AE; _ntes_stock_recent_=0601857%7C0601326%7C0600682; _ntes_stock_recent_=0601857%7C0601326%7C0600682; _ntes_stock_recent_=0601857%7C0601326%7C0600682; ne_analysis_trace_id=1563963422398; s_n_f_l_n3=ad2a50d90e25c7dc1563963422401; _antanalysis_s_id=1563963428611; pgr_n_f_l_n3=ad2a50d90e25c7dc15639634493333113',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
		          'application/signed-exchange;v=b3',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
		'Connection': 'keep-alive',
		'Host': 'quotes.money.163.com',
		'Referer': 'http://quotes.money.163.com / trade / lsjysj_601857.html',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/75.0.3770.100 Safari/537.36'
		}
	file_path = 'F:/Stock_Data/stock_data/'


class Index_data(Data):
	URL = 'http://quotes.money.163.com/service/chddata.html'
	HEADERS = {
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
		          'application/signed-exchange;v=b3',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
		'Connection': 'keep-alive',
		'Host': 'quotes.money.163.com',
		'Referer': 'http://quotes.money.163.com/trade/lsjysj_zhishu_000003.html',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/75.0.3770.100 Safari/537.36'
		}
	PARAMS = {
		'start': '19900101',
		'fields': 'TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER '
		}
	file_path = 'F:/Stock_Data/index_data/'
