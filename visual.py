# -*- coding:utf-8 -*-

import pandas as pd
from pylab import *
import pymysql
from config import HOST, PORT, USER, PASS, DB, TABLE
from wordcloud import WordCloud
import cv2
import jieba
import os

class View(object):
    def __init__(self):
        self.connect = pymysql.connect(host=HOST, user=USER, passwd=PASS, db=DB, port=PORT, charset='utf8')
        self.dirname = os.path.dirname(os.path.realpath(__file__))
        mpl.rcParams['font.sans-serif'] = ['SimHei']

    def meishi_top10(self):
        """当前地区评论前10的店铺"""
        df = pd.read_sql("select title,comments from {table}".format(table=TABLE), self.connect)
        # 排序
        df2 = df.sort_values(by='comments', ascending=False)
        # 设置索引
        df3 = df2.set_index('title')[0:10].sort_values(by='comments', ascending=True)
        # 柱状图
        fig = df3.plot(kind='barh', alpha=0.3).get_figure()
        plt.tight_layout()
        fig.savefig('{}\\{}\\{}.jpg'.format(self.dirname, '\\view', '\\top10'))
        # plt.show()

    def avgscore_ratio(self):
        """美食店铺各评分占比"""
        df = pd.read_sql('select avgscore from {table}'.format(table=TABLE), self.connect)
        # 饼状图
        fig = df['avgscore'].value_counts().plot(kind='pie').get_figure()
        fig.savefig('{}\\{}\\{}.jpg'.format(self.dirname, '\\view', '\\ratio'))
        # plt.show()

    def avgprice_comments(self):
        """店铺价格与评论数量的关联性"""
        df = pd.read_sql('select avgprice, comments from {table}'.format(table=TABLE), self.connect)
        fig = df.plot(kind='scatter', x='avgprice', y='comments').get_figure()
        fig.savefig('{}\\{}\\{}.jpg'.format(self.dirname, '\\view', '\\pricom'))

    def wrodcloud(self):
        """词云"""
        # 读取title
        titles = pd.read_sql("select title from {table}".format(table=TABLE), self.connect)
        dirname = self.dirname + '\\view'
        text_path = dirname + '\\title.txt'
        # if not os.path.exists(text_path):
        #     open(text_path)

        with open(text_path, 'w', encoding='utf-8') as f:
            for title in titles['title']:
                title = title.split('（')[0]
                f.write('%s\n' % str(title))

        if text_path:
            with open(text_path, 'r', encoding='utf-8') as f:
                text = f.read()
            cut_text = " ".join(jieba.cut(text))
            color_mask = cv2.imread(dirname + '\\qin.png')
            cloud = WordCloud(
                # 设置字体，不指定就会出现乱码
                font_path= dirname + "\\FZSTK.TTF",
                # 设置背景色
                background_color='white',
                # 词云形状
                mask=color_mask,
                # 允许最大词汇
                max_words=2000,
                # 最大号字体
                max_font_size=50
            )
            wCloud = cloud.generate(cut_text)
            wCloud.to_file(dirname + '\\key.png')
            plt.imshow(wCloud, interpolation='bilinear')
            plt.axis('off')
            plt.show()

if __name__ == '__main__':
    view = View()
    view.meishi_top10()
    # view.avgscore_ratio()
    # view.avgprice_comments()
    # view.wrodcloud()