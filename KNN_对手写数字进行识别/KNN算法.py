from sklearn.neighbors import KNeighborsClassifier  #做分类
from sklearn.neighbors import  KNeighborsRegressor  #做回归
from sklearn.datasets import load_digits
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics
#构造函数
knn=KNeighborsClassifier(n_neighbors=5,weights='uniform',algorithm='auto',leaf_size=30)
#数据加载
digits=load_digits()
data=digits.data

# # 数据探索
# print(data.shape)
# #查看第一幅图像
# print(digits.images[0])
# #第一幅图像代表的数字含义
# print(digits.target[0])
# #将第一幅图像显示出来
# plt.gray()
# plt.imshow(digits.images[0])
# plt.show()

train_x,test_x,train_y,test_y=train_test_split(data,digits.target,test_size=0.25,random_state=33)


mm=MinMaxScaler()
train_mm_x=mm.fit_transform(train_x)
test_mm_x=mm.fit_transform(test_x)



#采用Z-Score规范化
ss=StandardScaler()
train_x=ss.fit_transform(train_x)
test_x=ss.fit_transform(test_x)
knn.fit(train_x,train_y)
predict_y=knn.predict(test_x)
print('KNN准确率:',metrics.accuracy_score(predict_y,test_y))


from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(criterion='entropy')
clf.fit(train_x,train_y)
predict_tree=clf.predict(test_x)
print('决策树准确率:',metrics.accuracy_score(predict_tree,test_y))

from sklearn.naive_bayes import MultinomialNB
bys=MultinomialNB(alpha=0.001)
bys=bys.fit(train_mm_x,train_y)
predict_bys=bys.predict(test_mm_x)
print('贝叶斯分类器准确率:',metrics.accuracy_score(predict_bys,test_y))



from sklearn import svm
model=svm.SVC(gamma='auto')
model.fit(train_x,train_y)
predict_svm=model.predict(test_x)
print('SVM准确率:',metrics.accuracy_score(predict_svm,test_y))