# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/8/2'
"""

import requests
import json

URL = 'http://quotes.money.163.com/hs/service/diyrank.php'

HEADERS = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
	'Connection': 'keep-alive',
	'Host': 'quotes.money.163.com',
	'Referer': 'http://quotes.money.163.com/old/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
	}

PARAMS = {
	'host': 'http://quotes.money.163.com/hs/service/diyrank.php',
	'page': '0',
	'query': 'STYPE:EQA',
	'fields': 'NO,SYMBOL,NAME,PRICE,PERCENT,UPDOWN,FIVE_MINUTE,OPEN,YESTCLOSE,HIGH,LOW,VOLUME,TURNOVER,HS,LB,WB,ZF,PE,MCAP,TCAP,MFSUM,MFRATIO.MFRATIO2,MFRATIO.MFRATIO10,SNAME,CODE,ANNOUNMT,UVSNEWS',
	'sort': 'SYMBOL',
	'order': 'asc',
	'count': '10240',
	'type': 'query'
	}

response = requests.get(url=URL, params=PARAMS, headers=HEADERS)
total = json.loads(response.content.decode('gbk'))['total']
PARAMS['count'] = total

response = requests.get(url=URL, params=PARAMS, headers=HEADERS)
data_list = json.loads(response.content.decode('gbk'))['list']

for row in data_list:
	print('CODE','代码',row['CODE'])
	print('FIVE_MINUTE','五分钟涨跌',row['FIVE_MINUTE'])
	print('HIGH','最高价',row['HIGH'])
	print('LOW','最低价',row['LOW'])
	print('NAME','股票名称',row['NAME'])
	print('OPEN','开盘价',row['OPEN'])
	print('PERCENT','涨跌幅',row['PERCENT'])
	print('PRICE','价格',row['PRICE'])
	print('SYMBOL','股票代码',row['SYMBOL'])
	print('TURNOVER','成交额',row['TURNOVER'])
	print('UPDOWN','涨跌额',row['UPDOWN'])
	print('VOLUME','成交量',row['VOLUME'])
	print('YESTCLOSE','昨收',row['YESTCLOSE'])
	print('ZF','振幅',row['ZF'])
	

