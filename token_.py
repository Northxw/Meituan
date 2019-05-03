# -*- coding:utf-8 -*-

import base64, zlib
import time
import random
import pandas as pd
import os
from config import SIGN_PARAM

def sign():
    """生成sign参数"""
    # 默认编码
    # coding = sys.getdefaultencoding()
    # 二进制压缩
    binary_data = zlib.compress(SIGN_PARAM.encode())
    # base64编码
    base64_data = base64.b64encode(binary_data)
    # 返回utf8编码的字符串
    return base64_data.decode()


def encrypt_token():
    """生成_token参数"""
    ts = int(time.time() * 1000)    # time.time()返回1970年至今的时间(以秒为单位)
    # 伪装机型
    json_path = os.path.dirname(os.path.realpath(__file__)) + '\\utils\\br.json'
    df = pd.read_json(json_path)
    brVD, brR_one, brR_two  = df.iloc[random.randint(0, len(df)-1)]
    token_data = {
        "rId": 100900,
        "ver": "1.0.6",
        "ts": ts,
        "cts": ts + random.randint(100,120),        # 经测,cts - ts 的差值大致在 90-130 之间
        # "cts": ts + 100,
        "brVD": eval(brVD),
        "brR": [eval(brR_one), eval(brR_two), 24, 24],
        "bI":["https://bj.meituan.com/meishi/",""],
        "mT": [],
        "kT": [],
        "aT": [],
        "tT": [],
        "aM": "",
        "sign": sign()
    }
    # 二进制压缩
    binary_data = zlib.compress(str(token_data).encode())
    # base64编码
    base64_data = base64.b64encode(binary_data)
    return base64_data.decode()


# 解码解压逻辑测试
def decrypt_token_sign(token_sign):
    """base64解码, 二进制解压"""
    token_decode = base64.b64decode(token_sign.encode())
    return zlib.decompress(token_decode)


if __name__ == '__main__':
    # sign = 'eJxVjl1vgkAQRf/LvkrcXRAoJj5gEYRikI8q2vQBcaTIx1pAqm3637umbdImk9w7Z87DfKDG3qMxJUQjREA9NGiM6JAMFSSgruUXWVZkIioqGamqgNL/TNZGAto1KwONn6ikEEEk2vONBBx8E1W5exb+VHHE5+bYXEEvXXdqxxjvjsMK8u6c1MOUVZj39iXH/AfE1SriKs/iJ5Of7H73BX+au22e1byB81YeI+rp7zM/OA/Ct45WIty3hmO7pc4cElv6Om7Fah1pDM82edT76ahKs6Xnw53vSHuvPmHosqkJfUx9I4twBlEz993kig9LaaBtYcMC2O5fy2ka7Jj8sA6Pj23RgproIZHVfHrFou24bqppy4u00ovsdFFXLrPk1NDCxsDnbb2xStMTL1YZgO/FJlvQhdzDrHYZdTeN9Wo27wf62IBSmwOxyox6WxziJJ1Th0x7oJl/PgSVVYAE7GEeOvZVn0zQ5xf47IrC'
    # print(decrypt_token_sign(sign).decode())
    print(encrypt_token())