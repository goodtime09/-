from sklearn.mixture import GaussianMixture
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import calinski_harabaz_score

data = pd.read_csv('heros.csv', encoding='gbk')
features = ['最大生命', '生命成长', '初始生命', '最大法力', '法力成长', '初始法力', '最高物攻'
    , '物攻成长', '初始物攻', '最大物防', '物防成长', '初始物防', '最大每5秒回血', '每5秒回血成长',
            '初始每5秒回血', '最大每5秒回蓝', '每5秒回蓝成长', '初始每5秒回蓝', '最大攻速', '攻击范围'
            ]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
corr = data[features].corr()
plt.figure(figsize=(14, 14))
# annot=True
sns.heatmap(corr, annot=True)
# plt.show()
features_remain = ['最大生命', '初始生命', '最大法力', '最高物攻', '初始物攻', '最大物防', '初始物防'
    , '最大每5秒回血', '最大每5秒回蓝', '初始每5秒回蓝', '最大攻速', '攻击范围']

data_remain = data[features_remain]
pd.options.mode.chained_assignment = None  # 关闭pandas警告
data_remain['最大攻速'] = data_remain['最大攻速'].apply(lambda x: float(x.strip('%')) / 100)
data_remain['攻击范围'] = data_remain['攻击范围'].map({'远程': 1, '近战': 0})
ss = StandardScaler()
data_remain = data_remain.astype('float64')
data_remain = ss.fit_transform(data_remain)
gmm = GaussianMixture(n_components=30, covariance_type='full')
gmm.fit(data_remain)
prediction = gmm.predict(data_remain)
data.insert(0, '分组', prediction)
data.to_csv('heros_em.csv', index=False, sep=',', encoding='gbk')
print(calinski_harabaz_score(data_remain, prediction))
