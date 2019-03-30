from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import  DecisionTreeClassifier ,DecisionTreeRegressor #分类树,回归树
from sklearn.datasets import load_iris #数据集

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.datasets import load_boston
from sklearn.datasets import load_digits

import pandas as pd
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import cross_val_score

# iris=load_iris()
# features=iris.data
# labels=iris.target
# train_features,test_features,train_labels,test_labels=train_test_split(features,labels,test_size=0.33,random_state=0)
# clf=DecisionTreeClassifier(criterion='gini')
# clf=clf.fit(train_features,train_labels)
# test_predict=clf.predict(test_features)
# score=accuracy_score(test_labels,test_predict)
# print('CART分类树准确率%.4lf'%score)


# boston=load_boston()
# print(boston.feature_names)
# features=boston.data
# prices=boston.target
# train_features,test_features,train_price,test_price=train_test_split(features,prices,test_size=0.33)
# dtr=DecisionTreeRegressor()
# dtr=dtr.fit(train_features,train_price)
# predict_price=dtr.predict(test_features)
# print('回归树二乘偏差均值:',mean_squared_error(test_price,predict_price))
# print('回归树绝对值偏差均值:',mean_absolute_error(test_price,predict_price))
# print(test_price)

# digits=load_digits()
# print(digits.keys())
# features=digits.data
# target=digits.target
# train_features,test_features,train_target,test_target=train_test_split(features,target,test_size=0.33)
# clf=DecisionTreeClassifier(criterion='entropy')
# clf=clf.fit(train_features,train_target)
# test_predict=clf.predict(test_features)
# score=accuracy_score(test_target,test_predict)
# print('准确率:',score)


train=pd.read_csv('train.csv')
test=pd.read_csv("test.csv")
# print(train.info())
# print('-'*30)
# print(test.info())
train['Age'].fillna(train['Age'].mean(),inplace=True)
train['Embarked'].fillna('S',inplace=True)
test['Age'].fillna(test['Age'].mean(),inplace=True)
test['Fare'].fillna(test['Fare'].mean(),inplace=True)

features=['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
train_features=train[features]
train_labels=train['Survived']
test_features=train[features]

dvec=DictVectorizer(sparse=False)
train_features=dvec.fit_transform(train_features.to_dict(orient='record'))
test_features=dvec.fit_transform(test_features.to_dict(orient='record'))
dtc=DecisionTreeClassifier(criterion='gini')
dtc=dtc.fit(train_features,train_labels)
test_labels=dtc.predict(test_features)

a=np.mean(cross_val_score(dtc,train_features,train_labels,cv=10))
print(a)

