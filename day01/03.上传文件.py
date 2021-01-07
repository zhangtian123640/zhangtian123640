'''
上传文件：
    本地文件上传到服务器上，比如上传头像，上传附件等
'''

import requests

# 上传文件的接口
url = "http://www.httpbin.org/post"
# 要上传的文件(本地磁盘上的文件)
filepath1 = "d:/test.doc"
filepath2 = "d:/Koala.jpg"
with open(filepath1, 'rb') as f:
    with open(filepath2, 'rb') as f2:
        file = {
            "file1": (filepath1, f),  # 2-tuple('filename',fileobj)
            # content_type MIME 类似， 大类型、子类型 text/plain image/jpg application/json....
            "file2": (filepath2, f2, "image/png")
        }
        r = requests.post(url, files=file)
        print(r.text)
