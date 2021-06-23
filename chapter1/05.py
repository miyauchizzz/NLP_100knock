def ngram(n, word):
  return list(zip(*[word[i:] for i in range(n)]))

str = 'I am an NLPer'
splits = str.split()
word_bigram = ngram(2, splits)
char_bigram = ngram(2, str)

print('単語bi-gram:', word_bigram)
print('文字bi-gram:', char_bigram)
