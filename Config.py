# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/3'
"""

GET_BONUS_URL = 'http://quotes.money.163.com/f10/fhpg_{}.html'


GET_INDEX_URL = 'http://quotes.money.163.com/service/chddata.html'
GET_INDEX_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
	'Connection': 'keep-alive',
	'Host': 'quotes.money.163.com',
	'Referer': 'http://quotes.money.163.com/trade/lsjysj_zhishu_000003.html',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
	}
GET_INDEX_PARAMS = {
	'start': '19900101',
	'fields': 'TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER '
	}


GET_ALL_INDEX_URL = 'http://quotes.money.163.com/hs/service/hsindexrank.php'
GET_ALL_INDEX_HEADERS = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
	'Connection': 'keep-alive',
	'Host': 'quotes.money.163.com',
	'Referer': 'http://quotes.money.163.com/old/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
	}
GET_ALL_INDEX_PARAMS = {
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


GET_HISTORY_DATA_URL = 'http://quotes.money.163.com/service/chddata.html'
GET_HISTORY_DATA_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
	'Connection': 'keep-alive',
	'Host': 'quotes.money.163.com',
	'Referer': 'http://quotes.money.163.com/trade/lsjysj_000009.html',
	'Upgrade-Insecure-Requests': '1',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
	}
GET_HISTORY_DATA_PARAMS = {
	'code': '1000009',
	'start': '19900101',
	'end': '',
	'fields': 'TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
	}


GET_STOCK_INFO_PARAMS = {
	'host': 'http://quotes.money.163.com/hs/service/diyrank.php',
	'page': '0',
	'query': 'STYPE:EQA',
	'fields': 'NO,SYMBOL,NAME,PRICE,PERCENT,UPDOWN,FIVE_MINUTE,OPEN,YESTCLOSE,HIGH,LOW,VOLUME,TURNOVER,HS,LB,WB,ZF,PE,MCAP,TCAP,MFSUM,MFRATIO.MFRATIO2,MFRATIO.MFRATIO10,SNAME,CODE,ANNOUNMT,UVSNEWS',
	'sort': 'SYMBOL',
	'order': 'asc',
	'count': '20',
	'type': 'query'
	}
GET_STOCK_INFO_HEADERS = {
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh,en-US;q=0.9,en;q=0.8,zh-TW;q=0.7,zh-CN;q=0.6',
	'Connection': 'keep-alive',
	'Host': 'quotes.money.163.com',
	'Referer': 'http://quotes.money.163.com/old/',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
	}
GET_STOCK_INFO_URL = GET_STOCK_INFO_PARAMS['host']

STOCK_INFO_PATH = 'F:/Stock_Data/list/'
STOCK_DATA_PATH = 'F:/Stock_Data/data/'
INDEX_INFO_PATH = 'F:/Stock_Data/list/'
INDEX_PATH = 'F:/Stock_Data/index/'
BONUS_PATH = 'F:/Stock_Data/bonus/'
ALLOT_SHARES_PATH = 'F:/Stock_Data/allot_shares/'
ISSUE_PATH = 'F:/Stock_Data/issue/'
FINANCING_PATH = 'F:/Stock_Data/financing/'
TECHNICAL_ANALYSIS_PATH = 'F:/Stock_Data/technical_analysis/'