def main():
    f1 = "./col1.txt"
    f2 = "./col2.txt"
    f4 = "./col_merge2.txt"

    with open(f1, "r") as fr1, open(f2, "r") as fr2, open(f4, "w") as fw:
        merge = [name.strip() + "\t" + sex for name, sex in zip(fr1, fr2)]
        fw.write("".join(merge))

if __name__ == "__main__":
    main()
