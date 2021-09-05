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

#print(train_pred)


from sklearn.metrics import accuracy_score, confusion_matrix

train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])
#print(f"正解率（学習データ）：{train_accuracy:.3f}")
#print(f"正解率（評価データ）：{test_accuracy:.3f}")

import seaborn as sns
import matplotlib.pyplot as plt

train_cm = confusion_matrix(train['CATEGORY'], train_pred[1])
#print(train_cm)
fig = plt.figure()
sns.heatmap(train_cm, annot=True)
fig.savefig("confusion1.png")
test_cm = confusion_matrix(test['CATEGORY'], test_pred[1])
#print(test_cm)
fig = plt.figure()
sns.heatmap(test_cm, annot=True)
fig.savefig("confusion2.png")

from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_scores(y_true, y_pred):
  precision = precision_score(test['CATEGORY'], test_pred[1], average=None, labels=['b', 'e', 't', 'm'])
  precision = np.append(precision, precision_score(y_true, y_pred, average='micro'))
  precision = np.append(precision, precision_score(y_true, y_pred, average='macro'))  

  recall = recall_score(test['CATEGORY'], test_pred[1], average=None, labels=['b', 'e', 't', 'm'])
  recall = np.append(recall, recall_score(y_true, y_pred, average='micro'))
  recall = np.append(recall, recall_score(y_true, y_pred, average='macro'))

  f1 = f1_score(test['CATEGORY'], test_pred[1], average=None, labels=['b', 'e', 't', 'm'])
  f1 = np.append(f1, f1_score(y_true, y_pred, average='micro'))
  f1 = np.append(f1, f1_score(y_true, y_pred, average='macro'))

  scores = pd.DataFrame({'適合率': precision, '再現率': recall, 'F1スコア': f1},
                        index=['b', 'e', 't', 'm', 'マイクロ平均', 'マクロ平均'])

  return scores

#print(calculate_scores(test['CATEGORY'], test_pred[1]))

feature = X_train.columns.values
index = [i for i in range(1, 11)]
for c, coef in zip(clf.classes_, clf.coef_):
  print(f'カテゴリ={c}')
  Best10 = pd.DataFrame(feature[np.argsort(coef)[::-1][:10]], columns=['上位10'], index=index).T
  Worst10 = pd.DataFrame(feature[np.argsort(coef)[:10]], columns=['下位10'], index=index).T
  print(pd.concat([Best10, Worst10], axis=0))
  print('\n')
