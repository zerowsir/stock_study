# coding=utf-8
"""
　　__title__ = ''
　　__file__ = ''
　　__author__ = 'tianmuchunxiao'
　　__mtime__ = '2019/7/6'
"""

import tushare as ts
import pandas as pd

pro_api = ts.pro_api(token='3531aac4e2b7e3752304be0e83df5c39a2977fa57aa0e5e43fe16a38')
trade_cal = pro_api.trade_cal(start='19900101', fields=['cal_date', 'is_open', 'pretrade_date'])
trade_cal['cal_date'] = pd.to_datetime(trade_cal['cal_date'])
trade_cal['pretrade_date'] = pd.to_datetime(trade_cal['pretrade_date'])
trade_cal.to_csv('F:/Stock_Data/trade_cal.csv',
                 encoding='utf-8',
                 index=False)




