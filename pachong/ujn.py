import re
import os
import urllib
from urllib import request, error

os.chdir('D://python project')


def getHTML():
    url = 'http://www.ujn.edu.cn/index.php/article/26136/cid/4'
    req = request.Request(url)
    return request.urlopen(req)


try:
    res = getHTML()
    content = res.read().decode('utf-8')
    print(content)
except error.URLError as e:
    if hasattr(e, 'code'):
        print(e.code)
    if hasattr(e, 'reason'):
        print(e.reason)
