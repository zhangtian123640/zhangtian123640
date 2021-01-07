'''
用户模块的接口，杰模块管理
'''


def register(url, baserequests, data):
    '''
    注册接口
    :param url: 环境数据，比如http://jy001:8081/
    :param baserequests:BaseRequests的实例
    :param data:
    :return: 响应
    '''
    url = url + "/futureloan/mvc/api/member/register"
    return baserequests.post(url, data=data)


def login(url, baserequests, data):
    '''
    登录接口
    :param url:
    :param baserequests:
    :param data:
    :return:
    '''
    url = url + "/futureloan/mvc/api/member/login"
    return baserequests.post(url, data=data)


def list(url, baserequests):
    url = url + "/futureloan/mvc/api/member/list"
    return baserequests.get(url)
