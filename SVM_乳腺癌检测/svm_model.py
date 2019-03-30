from sklearn import svm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split    #切割训练集测试集
from sklearn import preprocessing
from sklearn import metrics

if __name__=='__main__':
    data=pd.read_csv('data.csv')
    features_mean=list(data.columns[2:12])
    features_se=list(data.columns[12:22])
    features_worst=list(data.columns[22:32])
    data.drop('id',axis=1,inplace=True)
    data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
    # #将肿瘤诊断结果可视化
    # sns.countplot(data['diagnosis'],label='Count')
    # plt.show()
    # #热力图呈现features_mean字段之间的相关性
    # corr=data[features_mean].corr()
    # plt.figure(figsize=(14,14))
    # #annot=True显示每个方格的数据
    # sns.heatmap(corr,annot=True)
    # plt.show()
    features_remain=['radius_mean','texture_mean','smoothness_mean','compactness_mean','symmetry_mean','fractal_dimension_mean']
    train,test=train_test_split(data,test_size=0.3)
    train_X=train[features_remain]
    train_y=train['diagnosis']
    test_X=test[features_remain]
    test_y=test['diagnosis']
    ss=preprocessing.StandardScaler()
    train_X=ss.fit_transform(train_X)
    test_X=ss.fit_transform(test_X)
    #创建SVM分类器
    model=svm.SVC(kernel='rbf',C=1.0,gamma='auto')
    #用训练集做训练
    model.fit(train_X,train_y)
    prediction=model.predict(test_X)
    print('准确率:',metrics.accuracy_score(prediction,test_y))








if __name__=='__main__':
    data=pd.read_csv('data.csv')
    data.drop('id',axis=1,inplace=True)
    data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
    features=data.columns.tolist()[1:11]
    train,test=train_test_split(data,test_size=0.3)
    train_X=train[features]
    train_y=train['diagnosis']
    test_X=test[features]
    test_y=test['diagnosis']
    ss=preprocessing.StandardScaler()
    train_X=ss.fit_transform(train_X)
    test_X=ss.fit_transform(test_X)

    model=svm.LinearSVC()
    model.fit(train_X,train_y)
    prediction=model.predict(test_X)
    prediction_1=model.predict((train_X))
    print('准确率:',metrics.accuracy_score(prediction,test_y))
    print('准确率:',metrics.accuracy_score(prediction_1,train_y))

