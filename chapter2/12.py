def main():
    f = "./popular-names.txt"
    f1 = "./col1.txt"
    f2 = "./col2.txt"
    
    with open(f, "r") as fr, open(f1, "w") as fw1, open(f2, "w") as fw2:
        for line in fr:
            splits = line.strip().split("\t")
            fw1.write(splits[0] + "\n")
            fw2.write(splits[1] + "\n")

if __name__ == "__main__":
    main()
