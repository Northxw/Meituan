# -*- coding:utf-8 -*-

import requests
from pyquery import PyQuery as pq
import hashlib
import pymysql
from sqlalchemy import create_engine
import pandas as pd
import logging
import random
import json
from config import *
import re


def get_cities():
    """城市名称-拼音简写对照字典"""
    doc = pq(requests.get('https://www.meituan.com/changecity/').text)
    a_lists = doc('.cities a').items()
    cities = {}
    [cities.update({a.text(): a.attr('href').replace('.', '/').split('/')[2]}) for a in a_lists]
    print(cities)
    with open('./utils/cities.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(cities, indent=2, ensure_ascii=False))

def get_uuid():
    """获取uuid"""
    url = 'https://bj.meituan.com/meishi/'
    # url = "http://localhost:8050/render.html?url=https://bj.meituan.com/meishi/&wait=5"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }
    res = requests.get(url, headers=headers).text
    uuid = re.findall(r'"uuid":"(.*?)"', res, re.S)[0]
    with open('./utils/uuid.log', 'w') as f:
        f.write(uuid)

def save(data):
    """存储数据"""
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USER, PASS, HOST, PORT, DB))
    connect = engine.connect()
    try:
        df = pd.DataFrame(data, index=[0])
        df.to_sql(name=TABLE, con=connect, if_exists='append', index=False)
    except Exception as e:
        logging.error("\nError: %s, Please check the error.\n" % e.args)
        _ = e

def get_md5(url):
    """md5处理"""
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

def xdaili_proxy():
    results = requests.get(url=API).json()['RESULT']
    agents = ["http://{}:{}".format(res['ip'], res['port']) for res in results]
    proxies = {
        "http": random.choice(agents),
        "https": random.choice(agents)
    }
    return proxies

def abuyun_proxy():
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": PROXY_HOST,
        "port": PROXY_PORT,
        "user": PROXY_USER,
        "pass": PROXY_PASS,
    }
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    return proxies

if __name__ == '__main__':
    get_cities()
    get_uuid()