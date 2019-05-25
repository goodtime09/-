from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn import svm
import matplotlib.pyplot as plt
rf = RandomForestClassifier()
data = pd.read_csv('UCI_Credit_Card.csv')
# print(data.info())
# print(data.columns)
data = data.astype('float64')
features = ['ID', 'LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_0',
       'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'BILL_AMT2',
       'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6', 'PAY_AMT1',
       'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
train_x, test_x, train_y, test_y = train_test_split(data[features], data['default.payment.next.month'],test_size=0.3)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    # ('model',svm.SVC())
    ('randomforestclassifier', rf)
])
parmeters = {'randomforestclassifier__n_estimators':range(1,11)}
clf = GridSearchCV(estimator=pipeline, param_grid=parmeters, cv=3)
clf.fit(train_x, train_y)
print('最优分数:%.4lf'%clf.best_score_)
print('最优参数:', clf.best_params_)
predict = clf.predict(test_x)
print(predict)
print(metrics.accuracy_score(predict, test_y))
plt.hist(predict, bins=2)
plt.show()


