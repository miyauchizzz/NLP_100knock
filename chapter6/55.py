import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    test = pd.read_csv('./test.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    X_test = pd.read_csv('./X_test.txt', sep='\t')
    
    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])
    
    train_cm = confusion_matrix(train['CATEGORY'], clf.predict(X_train))
    print(train_cm)
    fig = plt.figure()
    sns.heatmap(train_cm, annot=True)
    fig.savefig("confusion1.png")
    test_cm = confusion_matrix(test['CATEGORY'], clf.predict(X_test))
    print(test_cm)
    fig = plt.figure()
    sns.heatmap(test_cm, annot=True)
    fig.savefig("confusion2.png")

if __name__ == "__main__":
    main()
