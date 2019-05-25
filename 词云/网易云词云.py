#-*- coding:utf-8 -*-
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
import time
import requests
from lxml import etree
from selenium import webdriver
from PIL import Image
import numpy as np
# 生成词云
def create_word_cloud(f,STOPWORDS):
     print('根据词频计算词云')
     text = " ".join(jieba.cut(f,cut_all=False, HMM=True))
     wc = WordCloud(
           font_path='./simsun.ttc',
           stopwords=STOPWORDS,
           max_words=100,
           width=2000,
           height=1200,
    )
     wordcloud = wc.generate(text)
     # 写词云图片
     wordcloud.to_file("睡前原谅一切，醒后不问过往.jpg")
     # 显示词云文件
     plt.imshow(wordcloud)
     plt.axis("off")
     plt.show()

def loaddata(playlist):
    driver = webdriver.Chrome()
    driver.get(playlist)
    time.sleep(3)
    try:
        driver.switch_to_frame('g_iframe')
        text = driver.find_element_by_xpath('//body').get_attribute('outerHTML')
        html = etree.HTML(text)
        urls = html.xpath('//tbody/tr/td[2]/div/div/div/span/a/@href')
        all_lyric = ''
        for url in urls:
            url = 'https://music.163.com/#' + url
            driver.get(url)
            time.sleep(1)
            driver.switch_to_frame('g_iframe')
            driver.find_element_by_id("flag_ctrl").click()
            text = driver.find_element_by_xpath('//*').get_attribute('outerHTML')
            html = etree.HTML(text)
            lyric_1 = html.xpath('//*[@id="lyric-content"]/text()')
            lyric_2 = html.xpath('//*[@id="flag_more"]/text()')
            for i in lyric_1:
                all_lyric += i
            del lyric_1
            for i in lyric_2:
                all_lyric += i
            del lyric_2
        return all_lyric
    except:
        print('错误')



# playlist = 'https://music.163.com/#/playlist?id=882086412'
# playlist = 'https://music.163.com/#/playlist?id=2722916074'
# text = loaddata(playlist)
# with open('睡前原谅一切，醒后不问过往.text','w',encoding='utf-8') as f:
#     f.write(text)
STOPWORDS = ['作词','作曲','编曲','Arranger','录音','混音','人声','Vocal','制作','吉他']
# driver = webdriver.Chrome()
# driver.get(playlist)

with open('睡前原谅一切，醒后不问过往.text','r',encoding='utf-8') as f:
    text = f.read()
    create_word_cloud(text,STOPWORDS)

