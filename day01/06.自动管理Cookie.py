'''
自动管理cookie
requests中的Session类，能够自动获取和管理cookie
'''

import requests

s = requests.session()
print(s.cookies)

# 登录接口login
# 使用session发送请求
loginData = {
    "access_type": "1",
    "loginType": "1",
    "emailLoginWay": "0",
    "account": "2780487875@qq.com",
    "password": "qq2780487875",
    "remindeBox": "on",
    "reminde": "1"
}
r = s.post("https://www.bagevent.com/user/login", data=loginData)
# print(r.text)

print("登陆之后的cookie：", s.cookies)

# dashboard 接口
r = s.get("https://www.bagevent.com/account/dashboard")
# print(r.text)

# 退出登录 logout
r = s.get("https://www.bagevent.com/user/login_out")
# print(r.text)

print("退出登录后的cookie", s.cookies)

# RequestsCookieJar转成字典
d = requests.utils.dict_from_cookiejar(s.cookies)
print(d)
