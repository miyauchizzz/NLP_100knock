import sys

def main():
    f = "./popular-names.txt"
    
    with open(f,"r") as r:
        n = sys.argv[1]
        lines = r.readlines()
        if len(lines) % int(n) != 0:
            print("この引数では {} は割り切れません".format(len(lines)))
        else:
            split_line = len(lines) // int(n)
            for i in range(int(n)):
                x = i * split_line
                contexts = lines[x:x + split_line]
                filename = "splitfile_" + str(i) + ".txt"
                with open(filename,"w") as w:
                    w.write("".join(contexts))

if __name__ == "__main__":
    main()
