import pandas as pd

df = pd.read_table("./popular-names.txt", header=None)
print(df.sort_values([2], ascending=False))
