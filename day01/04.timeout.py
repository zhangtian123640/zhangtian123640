'''
timeout 超时
1.上传文件，上传2m耗时比较短，但是2g的文件，韩式比较长，可以使用timeout设置比较长的超时的时间
2.接口测试时，测试接口的性能，返回结果是否在某个时间范围内。
    比如获取用户列表的接口，是否在100ms以内。
'''

import requests

url = "http://jy001:8081/futureloan/mvc/api/member/list"
# Read time out.
r = requests.get(url, timeout=0.1)  # 100ms
print(r.text)

'''
代理 proxies
1. 用界面操作某个功能，结果正常。但是用自动化操作同样的功能，报错。
    界面操作时，抓包。
    自动化脚本执行时，抓包。
    对比抓到的包，检查差异点。
2. 频繁的向服务器发起请求，服务器当做攻击处理，将ip地址禁掉了。使用代理ip发送请求
'''

url = "http://jy001:8081/futureloan/mvc/api/member/list"
proxy = {
    "http": "http://127.0.0.1:8888",  # http协议，使用http://127.0.0.1:8888代理
    "https": "http://127.0.0.1:8888"
}
r = requests.get(url, proxies=proxy)  # 设置代理后，打开fiddler抓包
print(r.text)
# https的请求，使用代理时，
r = requests.get("http://www.baidu.com", proxies=proxy, verify=False)
print(r.text)