import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from wordcloud import WordCloud
import jieba
import time

def create_word_cloud(f, STOPWORDS):
    print('根据词频计算词云')
    text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    wc = WordCloud(
        font_path='./simsun.ttc',
        stopwords=STOPWORDS,
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(text)
    # 写词云图片
    wordcloud.to_file("wordcloud.jpg")
    # 显示词云文件
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

plt.rcParams['font.sans-serif']=['SimHei']
def education(data):
    plt.bar(data['学历'], ['本科', '不限', '硕士', '大专', '博士'])
    plt.show()
    # sns.barplot(a,b,data=c)
    # plt.show()

data = pd.read_csv('data.csv', names=['岗位ID', '城市', '公司全名', '福利待遇', '工作地点', '学历' , '工作类型', '发布时间', '职位', '薪资', '工作经验']
                   , header=None, encoding='gb2312')
data = data.drop_duplicates()
data_pay = data['薪资'].value_counts()
pay_list = []
for pay in data_pay.index:
    if data_pay[pay] > 2:
        pay_list.append(pay)
cities = data['城市'].value_counts()
print(cities)
city_list =[]
for city in cities.index:
    if cities[city]>1:
        city_list.append(city)
print('-'*30)
plt.subplot(221)
data['学历'].value_counts().plot(kind='barh', rot=0)
plt.title('学历要求')
plt.subplot(222)
plt.title('工作经验')
data['工作经验'].value_counts().plot(kind='bar', rot=0, color='b')
plt.subplot(223)
data['薪资'].value_counts()[pay_list].plot(kind='pie', rot=0, title='薪资')
plt.legend()
plt.subplot(224)
data['城市'].value_counts()[city_list].plot(kind='pie', autopct='%1.2f%%', explode = np.linspace(0,2,13))
#
plt.show()
text = ''.join(data['福利待遇'].values)
print(text)
STOPWORDS = []
create_word_cloud(text, STOPWORDS)
