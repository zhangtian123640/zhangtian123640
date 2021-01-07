import requests

url = "http://jy001:8081/futureloan/mvc/api/member/login"
# 验证用户输入合法的手机号码、密码，登录成功
data = {"mobilephone": "15091077724", "pwd": "123456"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "登录成功"



# 验证用户输入合法的密码，手机号码为空，登录失败
data = {"mobilephone": "", "pwd": "123456"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# 验证用户输入合法的手机号码，密码为空，登录失败
data = {"mobilephone": "15091077724", "pwd": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "密码不能为空"
# 验证手机号、密码为空，登录失败
data = {"mobilephone": "", "pwd": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"


# 输入未注册手机号，输入手机号长度不合法（10,12位）
# 验证输入未注册的手机号，登录失败
data = {"mobilephone": "15091077790", "pwd": "123456"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"
# 验证输入长度不合法的手机号，登录失败
# 手机号长度10位
data = {"mobilephone": "1509107779", "pwd": "123456"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"
#手机号长度12位
data = {"mobilephone": "150910777901", "pwd": "123456"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"

# 验证输入合法的手机号码，密码不合法，登录失败
data = {"mobilephone": "15091077724", "pwd": "12345"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"
# 验证输入已注册的手机号码，密码错误，登录失败
data = {"mobilephone": "15091077724", "pwd": "123457"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "用户名或密码错误"





