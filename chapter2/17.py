f = "popular-names.txt"

with open(f, "r") as fr:
    num = set()
    for i in fr:
        splits = i.split("\t")
        num.add(splits[0])

    print(len(num))

