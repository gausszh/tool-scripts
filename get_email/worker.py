#coding=utf8
from redis import Redis
from pyquery import PyQuery as pq
import json
import threading
rd = Redis()
URL_key = 'GET_EMAIL:URL'
RESULT_KEY = 'GET_EMAIL:RESULT'
THREADING_NUM = 8
def parser_email():
    '''
    根据参数url解析出其中的联系信息
    '''
    while 1:
        url = rd.rpop(URL_key)
        if not url:
            break
        d = pq(url)
        tb = d('#bodyContent table')
        tb = tb.eq(0)
        tr = tb.children('tr')
        m = tr.eq(3)
        span = m('span')
        y = []
        for a in span:
            y.append(a.text)
        rd.lpush(RESULT_KEY,json.dumps(y))
lt = []
for i in THREADING_NUM:
    lt.append(threading.Thread(target=parser_email, args=()))
for th in lt:
    th.start()
for th in lt:
    th.join()
