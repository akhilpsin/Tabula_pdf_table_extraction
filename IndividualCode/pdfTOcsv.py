import tabula
import requests
import csv
import pandas as pd


# Read a PDF File
df = tabula.read_pdf("pdf.pdf", pages='all')
#print(df[0])

# convert PDF into CSV
count=0
for i in df:
    name="input\\"+str(count)+".csv"
    df[count].to_csv(name, index=False)
    count+=1



