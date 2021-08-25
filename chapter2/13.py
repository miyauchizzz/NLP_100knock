f1 = "./col1.txt"
f2 = "./col2.txt"
f3 = "./col_merge.txt"

with open(f1, "r") as fr1, open(f2, "r") as fr2, open(f3, "w") as fw:
    for x1 in fr1:
        x2 = fr2.readline()
        fw.write(x1.strip() + "\t" + x2.strip() + "\n")
