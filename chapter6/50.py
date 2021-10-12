import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df = pd.read_csv('./newsCorpora.csv', header=None, sep='\t', names=('ID', 'TITLE', 'URL', 'PUBLISHER', 'CATEGORY', 'STORY', 'HOSTNAME', 'TIMESTAMP'))
    
    df = df.loc[df['PUBLISHER'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['CATEGORY', 'TITLE']]
    
    train, valid_test = train_test_split(df, test_size=0.2, random_state=42, stratify = df['CATEGORY'])
    valid, test = train_test_split(valid_test, test_size=0.5, random_state=42, stratify = valid_test['CATEGORY'])
    
    train.to_csv('./train.txt', sep='\t', index = False)
    valid.to_csv('./valid.txt', sep='\t', index = False)
    test.to_csv('./test.txt', sep='\t', index = False)
    
    print('学習データ')
    print(train['CATEGORY'].value_counts())
    print('検証データ')
    print(valid['CATEGORY'].value_counts())
    print('評価データ')
    print(test['CATEGORY'].value_counts())

if __name__ == "__main__":
    main()

