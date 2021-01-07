'''
pytest脚本
1、文件以test_开头
2、测试类以Test开头
3、测试函数或者方法以test_开头
'''
import requests

url = "http://jy001:8081/futureloan/mvc/api/member/register"


def test_register_001():
    cs = {"mobilephone": "18012345678", "pwd": "123456"}
    r = requests.get(url, data=cs)
    print(r.text)
    assert r.json()['code'] == '20103'


def test_register_002():
    cs = {"mobilephone": "18012345678", "pwd": "12345"}
    r = requests.get(url, data=cs)
    assert r.json()['msg'] == '手机号不能为空'


def test_register_003():
    cs = {"mobilephone": "18012345678"}
    r = requests.get(url, data=cs)
    assert r.json()['msg'] == '手机号不能为空'

