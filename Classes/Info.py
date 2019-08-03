# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/4'
"""
import requests
import io
import json
import pandas as pd

class Info_base(object):
	URL = ''
	PARAMS = {}
	HEADERS = {}
	file_path = ''
	
	def __init__(self):
		try:
			self.data_df = pd.read_csv(self.file_path)
		except:
			self.get_data()
		
		
	def get_data(self):
		response = requests.get(url=self.URL,
		                             params=self.PARAMS,
		                             headers= self.HEADERS)
		
		data_json = json.loads(io.StringIO(response.text).read())
		self.PARAMS['count'] = data_json['total']
		print('正在获取数据……')
		response = requests.get(url=self.URL,
		                        params=self.PARAMS,
		                        headers=self.HEADERS)
		
		data_json = json.loads(io.StringIO(response.content.decode('gbk')).read())
		print(data_json)
		self.data = data_json['list']
		
		self.columns = list(self.data[0].keys())
		
		self.data_df = pd.DataFrame(self.data, columns=self.columns)
		
		self.data_df.to_csv(self.file_path, encoding='gbk', index=False)
		print('数据处理完成')
		
		
class Stock_info(Info_base):
	PARAMS = {
		'host': 'http://quotes.money.163.com/hs/service/diyrank.php',
		'page': '0',
		'query': 'STYPE:EQA',
		'fields': 'NO,SYMBOL,NAME,PRICE,PERCENT,UPDOWN,FIVE_MINUTE,OPEN,YESTCLOSE,HIGH,LOW,VOLUME,TURNOVER,HS,LB,WB,'
		          'ZF,PE,MCAP,TCAP,MFSUM,MFRATIO.MFRATIO2,MFRATIO.MFRATIO10,SNAME,CODE,ANNOUNMT,UVSNEWS',
		'sort': 'SYMBOL',
		'order': 'asc',
		'count': '20',
		'type': 'query'
		}
	HEADERS = {
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'Accept-Encoding': 'gzip, deflate',
		'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
		'Connection': 'keep-alive',
		'Host': 'quotes.money.163.com',
		'Referer': 'http://quotes.money.163.com/old/',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
		              'Chrome/75.0.3770.100 Safari/537.36',
		'X-Requested-With': 'XMLHttpRequest'
		}
	URL = PARAMS['host']
	file_path = 'F:/Stock_Data/stock_info.csv'

class Index_info(Info_base):
	PARAMS = {
	'host': '/hs/service/hsindexrank.php',
	'page': '0',
	'query': 'IS_INDEX:true',
	'fields': 'no,SYMBOL,NAME,PRICE,UPDOWN,PERCENT,zhenfu,VOLUME,TURNOVER,YESTCLOSE,OPEN,HIGH,LOW',
	'sort': 'SYMBOL',
	'order': 'asc',
	'count': '25',
	'type': 'query',
	'callback': '',
	'req': '31254'
	}
	HEADERS = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
	'Connection': 'keep-alive',
	'Host': 'quotes.money.163.com',
	'Referer': 'http://quotes.money.163.com/old/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
	}
	URL = 'http://quotes.money.163.com/hs/service/hsindexrank.php'
	file_path = 'F:/Stock_Data/index_info.csv'