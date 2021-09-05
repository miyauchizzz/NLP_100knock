import pandas as pd
from sklearn.linear_model import LogisticRegression

train = pd.read_csv('./train.txt', sep='\t', names=('CATEGORY', 'TITLE'))
valid = pd.read_csv('./valid.txt', sep='\t', names=('CATEGORY', 'TITLE'))
test = pd.read_csv('./test.txt', sep='\t', names=('CATEGORY', 'TITLE'))
X_train = pd.read_csv('./X_train.txt', sep='\t')
X_valid = pd.read_csv('./X_valid.txt', sep='\t')
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
  #print(f'カテゴリ={c}')
  Best10 = pd.DataFrame(feature[np.argsort(coef)[::-1][:10]], columns=['上位10'], index=index).T
  Worst10 = pd.DataFrame(feature[np.argsort(coef)[:10]], columns=['下位10'], index=index).T
  #print(pd.concat([Best10, Worst10], axis=0))
  #print('\n')

from tqdm import tqdm

result = []
for C in tqdm(np.logspace(-5, 4, 10, base=10)):
  clf = LogisticRegression(random_state=42, max_iter=10000, C=C)
  clf.fit(X_train, train['CATEGORY'])

  np.set_printoptions(suppress=True)
  train_pred = (clf.predict_proba(X_train), clf.predict(X_train))
  valid_pred = (clf.predict_proba(X_valid), clf.predict(X_valid))
  test_pred = (clf.predict_proba(X_test), clf.predict(X_test))

  train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1])
  valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])
  test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1])

  result.append([C, train_accuracy, valid_accuracy, test_accuracy])

result = np.array(result).T
fig = plt.figure()
plt.plot(result[0], result[1], label='train')
plt.plot(result[0], result[2], label='valid')
plt.plot(result[0], result[3], label='test')
plt.ylim(0, 1.1)
plt.ylabel('Accuracy')
plt.xscale ('log')
plt.xlabel('C')
plt.legend()
fig.savefig("accuracy1.png") 

import optuna

def objective_clf(trial):
  l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
  C = trial.suggest_loguniform('C', 1e-4, 1e4)

  clf = LogisticRegression(random_state=42,
                          max_iter=10000,
                          penalty='elasticnet',
                          solver='saga',
                          l1_ratio=l1_ratio,
                          C=C)
  clf.fit(X_train, train['CATEGORY'])

  valid_pred = (clf.predict_proba(X_valid), clf.predict(X_valid))

  valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])

  return valid_accuracy

study = optuna.create_study(direction='maximize')
study.optimize(objective_clf, timeout=3600)

print('Best trial:')
trial = study.best_trial
print('  Value: {:.3f}'.format(trial.value))
print('  Params: ')
for key, value in trial.params.items():
  print('    {}: {}'.format(key, value))

l1_ratio = trial.params['l1_ratio']
C = trial.params['C']

clf = LogisticRegression(random_state=42, 
                        max_iter=10000, 
                        penalty='elasticnet', 
                        solver='saga', 
                        l1_ratio=l1_ratio, 
                        C=C)
clf.fit(X_train, train['CATEGORY'])

train_pred = (clf.predict_proba(X_train), clf.predict(X_train))
valid_pred = (clf.predict_proba(X_valid), clf.predict(X_valid))
test_pred = (clf.predict_proba(X_test), clf.predict(X_test))

train_accuracy = accuracy_score(train['CATEGORY'], train_pred[1]) 
valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1]) 
test_accuracy = accuracy_score(test['CATEGORY'], test_pred[1]) 

print(f'正解率（学習データ）：{train_accuracy:.3f}')
print(f'正解率（検証データ）：{valid_accuracy:.3f}')
print(f'正解率（評価データ）：{test_accuracy:.3f}')
