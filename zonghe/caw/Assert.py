'''
断言
'''
import pytest_check as ck


# check(r.json(),login_data['expect'],"code,msg,status")
def check(r_json, exptct, keys):
    '''
    校验r_json与expect中，相应的key对应的value是否相同
    :param r_json: 实际的响应结果
    :param exptct:  预期结果
    :param keys: 校验的key列表，用逗号分隔code，msg，status
    :return:
    '''
    ks = keys.split(",")
    for k in ks:  # 遍历key
        real = r_json[k]  # 根据key取r_json中的value值
        exp = exptct[k]  # 根据key取expect中的value值
        try:
            # assert str(real) == str(exp)
            ck.equal(str(real), str(exp))
        except Exception as e:
            print(f" 响应信息:{r_json},预期结果:{exptct},校验{k}失败")
