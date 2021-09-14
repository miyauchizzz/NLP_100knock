import sys

def main():
    f = "./popular-names.txt"
    
    with open(f,"r") as r:
        n = sys.argv[1]
        x = r.readlines()
        print("".join(x[:int(n)]))

if __name__ == "__main__":
    main()
