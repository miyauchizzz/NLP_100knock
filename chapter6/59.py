import pandas as pd
import optuna
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def main():
    train = pd.read_csv('./train.txt', sep='\t')
    valid = pd.read_csv('./valid.txt', sep='\t')
    test = pd.read_csv('./test.txt', sep='\t')
    X_train = pd.read_csv('./X_train.txt', sep='\t')
    X_valid = pd.read_csv('./X_valid.txt', sep='\t')
    X_test = pd.read_csv('./X_test.txt', sep='\t')

    def objective_clf(trial):
    l1_ratio = trial.suggest_uniform('l1_ratio', 0, 1)
    C = trial.suggest_loguniform('C', 1e-4, 1e4)

    clf = LogisticRegression(random_state=42,
                            max_iter=10,
                            penalty='elasticnet',
                            solver='saga',
                            l1_ratio=l1_ratio,
                            C=C)
    clf.fit(X_train, train['CATEGORY'])

    valid_pred = (clf.predict_proba(X_valid), clf.predict(X_valid))

    valid_accuracy = accuracy_score(valid['CATEGORY'], valid_pred[1])

    return valid_accuracy


    clf = LogisticRegression(random_state=42, max_iter=10000)
    clf.fit(X_train, train['CATEGORY'])

    study = optuna.create_study(direction='maximize')
    study.optimize(objective_clf, n_trials=10)

    print('Best trial:')
    trial = study.best_trial
    print('  Value: {:.3f}'.format(trial.value))
    print('  Params: ')
    for key, value in trial.params.items():
        print('    {}: {}'.format(key, value))
        
    l1_ratio = trial.params['l1_ratio']
    C = trial.params['C']
    
    clf = LogisticRegression(random_state=42,
                            max_iter=10,
                            penalty='elasticnet',
                            solver='saga',
                            l1_ratio=l1_ratio,
                            C=C)
    clf.fit(X_train, train['CATEGORY'])
        
    train_accuracy = accuracy_score(train['CATEGORY'], clf.predict(X_train))
    valid_accuracy = accuracy_score(valid['CATEGORY'], clf.predict(X_valid))
    test_accuracy = accuracy_score(test['CATEGORY'], clf.predict(X_test))
    
    print(f'正解率（学習データ）：{train_accuracy:.3f}')
    print(f'正解率（検証データ）：{valid_accuracy:.3f}')
    print(f'正解率（評価データ）：{test_accuracy:.3f}')

if __name__ == "__main__":
    main()



