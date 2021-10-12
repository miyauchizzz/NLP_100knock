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
    
    feature = X_train.columns.values
    index = [i for i in range(1, 11)]
    for c, coef in zip(clf.classes_, clf.coef_):
        print(f'カテゴリ={c}')
        Best10 = pd.DataFrame(feature[np.argsort(coef)[::-1][:10]], columns=['上位10'], index=index).T
        Worst10 = pd.DataFrame(feature[np.argsort(coef)[:10]], columns=['下位10'], index=index).T
        print(pd.concat([Best10, Worst10], axis=0))
        print('\n')

if __name__ == "__main__":
    main()
