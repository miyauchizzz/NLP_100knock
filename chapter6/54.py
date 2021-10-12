import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    test = pd.read_csv('./test.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    X_test = pd.read_csv('./X_test.txt', sep='\t')
    
    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])
    
    train_accuracy = accuracy_score(train['CATEGORY'], clf.predict(X_train))
    test_accuracy = accuracy_score(test['CATEGORY'], clf.predict(X_test))
    print(f"正解率（学習データ）：{train_accuracy:.3f}")
    print(f"正解率（評価データ）：{test_accuracy:.3f}")

if __name__ == "__main__":
    main()
