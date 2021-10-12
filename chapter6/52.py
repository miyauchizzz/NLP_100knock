import pandas as pd
from sklearn.linear_model import LogisticRegression

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    
    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])

if __name__ == "__main__":
    main()
