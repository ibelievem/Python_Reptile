from urllib.error import URLError,HTTPError
from urllib import request
url='htttp://www.baidu.com'

try:
    html=request.urlopen(url)
except URLError as e:
    if(hasattr(e,'code')):
        print('http error'+str(e.code))
    if(hasattr(e,'reason')):
        print('url error'+e.reason)