import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    test = pd.read_csv('./test.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    X_test = pd.read_csv('./X_test.txt', sep='\t')
    
    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])
    
    np.set_printoptions(suppress=True) 
    train_pred = (np.max(clf.predict_proba(X_train), axis=1), clf.predict(X_train))
    test_pred = (np.max(clf.predict_proba(X_test), axis=1), clf.predict(X_test))

    #確認用
    print(train_pred)

if __name__ == "__main__":
    main()
