# -*- coding:utf-8 -*-

from fake_useragent import UserAgent
import random
import pandas as pd
import os


CITYNAME = '西安'
cities_path = os.path.dirname(os.path.realpath(__file__)) + '\\utils\\cities.json'
with open(cities_path, encoding='utf-8') as f:
    CITIES = eval(f.read())

BASE_URL = "https://{}.meituan.com/meishi/api/poi/getPoiList?".format(CITIES[CITYNAME])

# USER-AGENT
log_path = os.path.dirname(os.path.realpath(__file__)) + '\\utils\\ua.log'
df = pd.read_csv(log_path, sep='\t')
user_agent = df["UA"].iloc[random.randint(0,1000)]

HEADERS = {
    "Accept": "application/json",
    "Referer": "https://{}.meituan.com/".format(CITIES[CITYNAME]),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36",
    # "User-Agent": UserAgent().random,
    # "User-Agent": user_agent
}

# UUID
uuid_path = os.path.dirname(os.path.realpath(__file__)) + '\\utils\\uuid.log'
with open(uuid_path) as f:
    UUID = f.read()

DATA = {
    "cityName": CITYNAME,
    "cateId": '0',
    "areaId": "0",
    "sort": "",
    "dinnerCountAttrId": "",
    "page": "1",
    "userId": "",
    "uuid": UUID,
    # "uuid": "5a794ab1247b427fb2c8.1556452305.1.0.0",
    "platform": "1",
    "partner": "126",
    "originUrl": "https://{}.meituan.com/meishi/".format(CITIES[CITYNAME]),
    "riskLevel": "1",
    "optimusCode": "1"
}

# GET PARAMETER
GET_PARAM =  {
        "cityName": DATA["cityName"],
        "cateId": DATA["cateId"],
        "areaId": DATA["areaId"],
        "sort": DATA["sort"],
        "dinnerCountAttrId": DATA["dinnerCountAttrId"],
        "page": DATA["page"],
        "userId": DATA["userId"],
        "uuid": DATA["uuid"],
        "platform": DATA["platform"],
        "partner": DATA["partner"],
        "originUrl": DATA["originUrl"],
        "riskLevel": DATA["riskLevel"],
        "optimusCode": DATA["optimusCode"],
        # "_token": encrypt_token()
}

# SIGN PARAMETER
SIGN_PARAM = "areaId={}&cateId={}&cityName={}&dinnerCountAttrId={}&optimusCode={}&originUrl={}&page={}&partner={}&platform={}&riskLevel={}&sort={}&userId={}&uuid={}".format(
    DATA["areaId"],
    DATA["cateId"],
    DATA["cityName"],
    DATA["dinnerCountAttrId"],
    DATA["optimusCode"],
    DATA["originUrl"],
    DATA["page"],
    DATA["partner"],
    DATA["platform"],
    DATA["riskLevel"],
    DATA["sort"],
    DATA["userId"],
    DATA["uuid"]
)

# TIME OUT
TIMEOUT = 5

# MAX PAGES
MAX_PAGES = 50

# MYSQL SETTINGS
HOST = 'localhost'
USER = 'root'
PASS = '123456'
PORT = 3306
DB = 'meituan'
TABLE = 'meishi'

# PROXY API
API = ''

# PROXY SETTINGS
PROXY_HOST = "http-dyn.abuyun.com"
PROXY_PORT = "9020"
PROXY_USER = "HU4C31nmfiDR57D"
PROXY_PASS = "2D4F3B8489F5FC91"

if __name__ == '__main__':
    # print(os.path.dirname(os.path.realpath(__file__)))
    pass
