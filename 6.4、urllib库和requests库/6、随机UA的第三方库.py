#随机UA的第三方库
from fake_useragent import FakeUserAgent


for i in range(10):
    print(FakeUserAgent().random)



