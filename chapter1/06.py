def ngram(n, word):
  return list(zip(*[word[i:] for i in range(n)]))

def main():
    str1 = "paraparaparadise"
    str2 = "paragraph"
    X = set(ngram(2, str1))
    Y = set(ngram(2, str2))
    
    print("X=", X)
    print("Y=", Y)
    print("和=", X | Y)
    print("積=", X & Y)
    print("差=", X - Y)
    if ("s","e") in X:
        print("seはXに含まれる")
    else:
        print("seはXに含まれない")
    if ("s","e") in Y:
        print("seはYに含まれる")
    else:
        print("seはYに含まれない")

if __name__ == "__main__":
    main()
