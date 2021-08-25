with open("popular-names.txt", "r", encoding="utf-8") as f:
    x = f.read()
    for i in x:
        if( i == "\t"):
            x = x.replace(i, " ")

print(x)
