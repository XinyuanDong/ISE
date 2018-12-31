import pandas as pd
import re
df = pd.read_csv("/Users/dongxinyuan/Desktop/Projektpraktikum Information Service Engineering/data/rawdata/split/finaldataset_item_title.csv",
                 delimiter = ",,,")
df.columns = ['uri', 'title']
print(df.head(100))
pattern = input("Enter a pattern: ")
print(df['title'].str.findall(pattern, flags=re.IGNORECASE))