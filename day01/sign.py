import requests

url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = {"mobilephone": "15091072727", "pwd": "123455", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
data = {"mobilephone": "15091077653", "pwd": "123456", "regname": "nihao"}
r = requests.get(url, params=data)
print(r.text)

# 验证用户使用合法的手机号码，昵称、密码为空，注册失败
data = {"mobilephone": "", "pwd": "123456", "regname": "nihao"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

data = {"mobilephone": "15091077623", "pwd": "", "regname": "nihao"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "密码不能为空"
data = {"mobilephone": "", "pwd": "", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

# 验证用户使用合法的手机号码，密码输入5位，注册失败
data = {"mobilephone": "15092077776", "pwd": "12345", "regname": "hhha"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"
# 验证用户使用合法的手机号码，密码输入19位，注册失败
data = {"mobilephone": "15092077776", "pwd": "1234567889199999999", "regname": "hhha"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "密码长度必须为6~18"
data = {"mobilephone": "15092077776", "pwd": "1234567889199999999", "regname": "hhha"}

# 输入手机号（10位、12位，输入不合法数字）
data = {"mobilephone": "1509207777", "pwd": "123456", "regname": "hhha"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
data = {"mobilephone": "150920777722", "pwd": "123456", "regname": "hhha"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
data = {"mobilephone": "1509207777q1", "pwd": "123456", "regname": "hhha"}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号码格式不正确"
# 注册手机号
data = {"mobilephone": "15091077727", "pwd": "123455", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
assert r.json()['msg'] == "手机号码已被注册"
# 注册成功
data = {"mobilephone": "15091077724", "pwd": "123456", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
data = {"mobilephone": "15091077716", "pwd": "123456a123456a1234", "regname": ""}
r = requests.get(url, params=data)
print(r.text)
