
from sklearn.feature_extraction.text import TfidfVectorizer
import io,os
from sklearn.naive_bayes import MultinomialNB
from sklearn import datasets
from sklearn import metrics
import jieba
if __name__=='__main__':
    # f=open('stop\stopword.txt','r',encoding='utf-8').readlines()
    # print(f)
    stop_words=[line.strip() for line in open('stop/stopword.txt',encoding='utf-8').readlines()]
    tf=TfidfVectorizer(stop_words=stop_words,token_pattern=r"(?u)\b\w+\b",max_df=0.5,tokenizer=jieba.cut)
    train_contents=datasets.load_files('train', description=None, categories=None, load_content=True, shuffle=True,
                                        encoding='GBK', decode_error='ignore', random_state=0)
    test_contents = datasets.load_files('test', description=None, categories=None, load_content=True,shuffle=True,
                                        encoding='GBK', decode_error='ignore', random_state=0)


    features=tf.fit_transform(train_contents.data)
    test_features=tf.transform(test_contents.data)
    clf=MultinomialNB(alpha=0.001).fit(features,train_contents.target)
    predicted_labels=clf.predict(test_features)
    print('准确率:',metrics.accuracy_score(test_contents.target, predicted_labels))
