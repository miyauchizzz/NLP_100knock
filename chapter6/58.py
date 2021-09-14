import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from tqdm import tqdm

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    valid = pd.read_csv('./valid.txt', sep='\t')
    test = pd.read_csv('./test.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    X_valid = pd.read_csv('./X_valid.txt', sep='\t')
    X_test = pd.read_csv('./X_test.txt', sep='\t')
    
    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])
        
    result = []
    for C in tqdm(np.logspace(-5, 4, 10, base=10)):
        clf = LogisticRegression(random_state=42, max_iter=10000, C=C)
        clf.fit(X_train, train['CATEGORY'])
        
        train_accuracy = accuracy_score(train['CATEGORY'], clf.predict(X_train))
        valid_accuracy = accuracy_score(valid['CATEGORY'], clf.predict(X_valid))
        test_accuracy = accuracy_score(test['CATEGORY'], clf.predict(X_test))
        
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
    fig.savefig("accuracy2.png")

if __name__ == "__main__":
    main()
