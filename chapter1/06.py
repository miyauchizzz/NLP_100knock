def ngram(n, word):
  return list(zip(*[word[i:] for i in range(n)]))

str1 = "paraparaparadise"
str2 = "paragraph"
X = set(ngram(2, str1))
Y = set(ngram(2, str2))

print("X=", X)
print("Y=", Y)
print("和=", X | Y)
print("積=", X & Y)
print("差=", X - Y)
if X & {("s","e")}:
    print("seはXに含まれる")
else:
    print("seはXに含まれない")
if Y & {("s","e")}:
    print("seはYに含まれる")
else:
    print("seはYに含まれない")
