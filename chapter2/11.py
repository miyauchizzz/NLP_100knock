def main():
    with open("popular-names.txt", "r", encoding="utf-8") as f:
        x = f.read()
        x = x.replace("\t", " ")
                
    print(x)

if __name__ == "__main__":
    main()
