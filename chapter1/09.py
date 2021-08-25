import random

def shuffle(str1):
    splits = str1.split()
    lst = []
    for word in splits:
        if len(word) > 4:
            lst.append(word[:1] + "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1:])
        else:
            lst.append(word)
    return " ".join(lst)
   

str1 = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind"

print(shuffle(str1))

