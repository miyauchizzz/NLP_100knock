import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score, f1_score

def calculate_scores(y_true, y_pred):
    precision = precision_score(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    precision = np.append(precision, precision_score(y_true, y_pred, average='micro'))
    precision = np.append(precision, precision_score(y_true, y_pred, average='macro'))
    
    recall = recall_score(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    recall = np.append(recall, recall_score(y_true, y_pred, average='micro'))
    recall = np.append(recall, recall_score(y_true, y_pred, average='macro'))
    
    f1 = f1_score(y_true, y_pred, average=None, labels=['b', 'e', 't', 'm'])
    f1 = np.append(f1, f1_score(y_true, y_pred, average='micro'))
    f1 = np.append(f1, f1_score(y_true, y_pred, average='macro'))
    
    scores = pd.DataFrame({'適合率': precision, '再現率': recall, 'F1スコア': f1},
                          index=['b', 'e', 't', 'm', 'マイクロ平均', 'マクロ平均'])
    
    return scores

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    test = pd.read_csv('./test.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    X_test = pd.read_csv('./X_test.txt', sep='\t')
    
    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])
    
    print(calculate_scores(test['CATEGORY'], clf.predict(X_test)))

if __name__ == "__main__":
    main()
