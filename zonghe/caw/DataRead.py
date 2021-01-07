'''
读文件相关的方法
'''
import configparser
import os

import yaml


def get_project_path():
    '''
    获取当前工程的路径
    :return:
    '''
    cp = os.path.realpath(__file__)  # D:\APIAutoTest\zonghe\caw\DataRead.py
    print(cp)
    cd = os.path.dirname(cp)  # D:\APIAutoTest\zonghe\caw
    print(cd)
    return os.path.dirname(cd) + "\\"


def read_ini(file_path, key):
    '''
    读取配置文件
    :param file_path:
    :param key:
    :return:
    '''
    file_path = get_project_path() + file_path
    config = configparser.ConfigParser()
    config.read(file_path)
    return config.get("env", key)  # env对于ini文件中env


def read_yaml(file_path):
    '''
    读取yaml文件
    :param file_path
    :return:
    '''
    file_path = get_project_path() + file_path
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        return yaml.load(content,Loader=yaml.FullLoader)


# 测试代码，用完删掉
if __name__ == '__main__':
    get_project_path()
    print()

    url = read_ini(r"data_env\env.ini", "url")
    print(url)
    db = read_ini(r"data_env\env.ini", "db")
    print(db)
    print(type(db))
    db = eval(db)  # 字符串解析为字典
    print(db)
    print(type(db))

    c = read_yaml(r"data_case/register_fail.yaml")
    print(c)
