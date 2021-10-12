def main():
    with  open('popular-names.txt','r', encoding="utf-8") as f:
        x = f.readlines()
    
    print(len(x))

if __name__ == "__main__":
    main()

