---
typora-root-url: Meituan\view
---

##  美团（美食）店铺信息爬虫

&emsp; 通过接口抓取美团美食店铺信息，并做相关的数据分析。

## 项目目录

```html
Meituan
│  common.py
│  config.py
│  meituan.py
│  parse.py
│  token_.py
│  visual.py
│  requirements.txt
│  
├─utils
│      br.json
│      cities.json
│      ua.log
│      uuid.log
│      
└─view
        FZSTK.TTF
        key.png
        qin.png
        title.txt
```

## 环境依赖

```python
pip3 install -r requirements.txt
```

## 解释说明

1.  接口动态参数：uuid,  _token。
2.  接口参数 uuid 需要不定时从网页源码获取 ，否则_token 的 uuid 就会失效。
3.  接口 _token 参数加密：二进制压缩、Base64 编码， 解密：Base64 解码、二进制解压。另外、生成 token 的 sign 参数加密解密过程与 _token 相同。

## 运行

&emsp; 切换至 Meituan 文件夹的根目录执行：

```
# pip3 install -r requirements.txt
python common.py
python meituan.py
```

&emsp; 或将 common.py、meituan.py 中的相关函数引入到 run.py 后执行：

```
python run.py
```

## 数据分析

- 美食店铺名称词云

![词云](/key.png)

- 西安美食店铺排行榜前10名( 仅限美团数据 ) 

![2](/top10.jpg)

- 评分占比

  ![3](/ratio.jpg)

- 人均价格与评论数量的相关性分析

  ![4](/pricom.jpg)

- MySql 数据

  ![5](/db.png)

## 公告

&emsp; **本代码仅作学习交流，切勿用于商业用途，否则后果自负。若涉及点评网侵权，请邮箱联系，会尽快处理。**

