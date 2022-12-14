import pandas as pd
import glob
import os

# setting the path for joining multiple files
files = os.path.join("C:\\Users\\akhil.suresh\\Desktop\\tabul\\input", "*.csv")


# list of merged files returned
files = glob.glob(files)


# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)

df.to_csv('output\Combined.csv', index=False)

print("Sucessfully generated output CSV")
