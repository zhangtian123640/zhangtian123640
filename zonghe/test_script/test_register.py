'''
注册的测试脚本
'''

# 注册失败 的测试脚本
import pytest

from zonghe.baw import Member, Db
from zonghe.caw import DataRead, BaseRequests, Assert


# pytest 数据驱动的方式
# 从yaml中读取测试数据
@pytest.fixture(params=DataRead.read_yaml(r"data_case/register_fail.yaml"))
def fail_data(request):
    return request.param


# 注册失败的测试脚本
def test_register_fail(url, baserequests, fail_data):
    print(f'{fail_data}')

    # 下发注册的请求
    r = Member.register(url, baserequests, fail_data['data'])
    # 断言结果
    print(r.text)
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # assert r.json()['status'] == fail_data['expect']['status']
    Assert.check(r.json(), fail_data['expect'], "code,msg,status")

# 把注册成功的数据写到register_pass.yaml
# 注册成功的脚本，下发请求，断言响应的结果
@pytest.fixture(params=DataRead.read_yaml(r"data_case/register_success.yaml"))
def success_data(request):
    return request.param


def test_register_pass(url, baserequests, success_data, db):
    mobilephone = success_data['data']['mobilephone']
    # 初始化环境：删除注册的用户(数据库中可能有其他人测试的环境,与本用例冲突)
    Db.delete_user(db, mobilephone)
    # 下发注册的请求
    r = Member.register(url, baserequests, success_data['data'])
    print(r.text)
    # 断言响应结果
    # assert r.json()['code'] == success_data['expect']['code']
    # assert r.json()['msg'] == success_data['expect']['msg']
    # assert r.json()['status'] == success_data['expect']['status']
    Assert.check(r.json(), success_data['expect'], "code,msg,status")
    # 调用查询的接口，在查询的结果中能找到本次注册的手机号
    r1 = Member.list(url, baserequests)
    assert mobilephone in r1.text
    # 清理环境：删除注册的用户（在数据库中添加的数据,测试完成后清理掉）
    Db.delete_user(db, mobilephone)


# @pytest.fixture(params=DataRead.read_yaml(r"data_case/register_repeat.yaml"))
# def repeat_data(request):
#     return request.param


# def test_register_repeat(url, baserequests, register_data, db):
#     mobilephone = success_data['data']['mobilephone']
#     # 初始化环境
#     Db.delete_user(db, mobilephone)
#     # 下发注册请求
#     Member.register(url, baserequests, register_data['data'])
#     # 重复注册
#     r = Member.register(url, baserequests, register_data['data'])
#     print(r.text)
#     # 断言响应的结果
#     assert r.json()['code'] == register_data['expect']['code']
#     assert r.json()['code'] == register_data['expect']['code']
#     assert r.json()['code'] == register_data['expect']['code']
#     # 清理环境：删除注册用户（在数据库中添加的数据，测试完成之后清理掉）
#     Db.delete_user(db, mobilephone)
