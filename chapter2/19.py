import pandas as pd

def main():
    df = pd.read_table("./popular-names.txt", header=None)
    print(df[0].value_counts())

if __name__ == "__main__":
    main()
