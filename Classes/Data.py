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
		with open(self.file_path + code[1:] + '.csv', 'w', newline='') as f:
			f.write(response.content.decode('gbk'))
		data_df = pd.read_csv(self.file_path + code[1:] + '.csv', encoding='gbk')
		self.data_df = data_df.sort_values(by='日期', ascending=True)
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
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
		          'application/signed-exchange;v=b3',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
		'Connection': 'keep-alive',
		'Host': 'quotes.money.163.com',
		'Referer': 'http://quotes.money.163.com/trade/lsjysj_000009.html',
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
