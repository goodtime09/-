from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from sklearn import preprocessing


data=pd.read_csv('data.csv',encoding='gbk')
print(data)
kmeans=KMeans(n_clusters=3)
train_x=data[['2019年国际排名','2018世界杯','2015亚洲杯']]
train_x=train_x.astype('float')
df=pd.DataFrame(train_x)
# 规范化
# ss=preprocessing.StandardScaler()
# train_x=ss.fit_transform(train_x)
min_max_scaler=preprocessing.MinMaxScaler()
train_x=min_max_scaler.fit_transform(train_x)
#kmeans算法

kmeans.fit(train_x)
predict_y=kmeans.predict(train_x)
#合并聚类结果，插入原数据中
result=pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类'},axis=1,inplace=True)
print(result)