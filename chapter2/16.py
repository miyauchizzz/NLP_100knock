import sys

f = "./popular-names.txt"

with open(f,"r") as r:
    n = sys.argv[1]
    if 2780 % int(n) != 0:
        print("この引数では2780は割り切れません")
    else:
        lines = r.readlines()
        split_line = len(lines) // int(n)
        for i in range(int(n)):
            x = i * split_line
            contexts = lines[x:x + split_line]
            filename = "splitfile_" + str(i) + ".txt"
            with open(filename,"w") as w:
                w.write("".join(contexts))
