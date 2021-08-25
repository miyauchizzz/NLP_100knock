import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('./train.txt', sep='\t', names=('CATEGORY', 'TITLE'))
test = pd.read_csv('./test.txt', sep='\t', names=('CATEGORY', 'TITLE'))
X_train = pd.read_csv('./X_train.txt', sep='\t')
X_test = pd.read_csv('./X_test.txt', sep='\t')

clf = LogisticRegression(random_state=42, max_iter=10000)
clf.fit(X_train, train['CATEGORY'])


import numpy as np

np.set_printoptions(suppress=True) 
train_pred = (clf.predict_proba(X_train), clf.predict(X_train))
test_pred = (clf.predict_proba(X_test), clf.predict(X_test))

#確認用　print(train_pred)
