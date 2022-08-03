#Code:https://github.com/akhilpsin/Tabula_pdf_table_extraction/tree/main/Updatedcode_08.03.22

import tabula
import requests
import csv
import pandas as pd

import re
import parse
import pdfplumber
from collections import namedtuple
import datetime
from datetime import date
import os
import glob
import shutil
from os import path



#Here pdfplumber is used to extract post name , grade name and month repporting.

#----------------------------place pdf file in the same directory as the code, include extention 
file="pdf.pdf"
lines=[]
pnames=[]
gnames=[]
mreports=[]
with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
        try:
            text = page.extract_text()
        except:
            text=''
        if text is not None:
            liness=text.split('\n')
            lines+=liness
        
'''https://github.com/akhilpsin/Tabula_pdf_table_extraction '''           
for li in lines:
    if "Port:"in li:
        li=li.replace("Port:","").strip()
        li_new=li.split("Month Reporting:")[-0].strip()
        m_repor=li.split("Month Reporting:")[-1].strip()
        
        if "Grade Name:" in li_new:
            g_name=li_new.split("Grade Name:")[-1].strip()
            p_name=li_new.split("Grade Name:")[0].strip()
        else:
            g_name=li_new.split()[1:]
            g_name=' '.join(g_name).strip()
            p_name=li_new.split()[0].strip()
        pnames.append(p_name)
        gnames.append(g_name)
        mreports.append(m_repor)
print("PortName: ",len(pnames))
print("GradeName: ",len(gnames))
print("MonthReporting: ",len(mreports))


#This code is used to extract Table perform few cleanup operations and generate final output
df = tabula.read_pdf(file, pages='all')
final_list=[["PORT NAME","GRADE NAME","MONTH REPORTING","BL DATE","VESSEL","DESTINATION","CHARTERERS","API","BSW","POUR POINT","SULPHUR","DENSITY","H2S","SALT","SEDIMENT","RVP","TAN"]]
#final_list=[]
last_df=len(df)
print("Length of tables: ",last_df)

pnames.insert(-2,"Brass")
gnames.insert(-2,"Brass crude oil")
mreports.insert(-2,"Nov-21")

for i in range(last_df):
    op_df=df[i]
    op_df = op_df.dropna(how='all')
    op_df_list = op_df.values.tolist()
    
    for li in op_df_list:
        if str(li[0])== "nan":
            li=li[1:]
        else:
            print("check this case")
            print(li)
        li.insert(0,pnames[i])
        li.insert(1,gnames[i])
        li.insert(2,mreports[i])
        if "BL Date" in li:
            pass
        else:
            final_list.append(li)
        #print(li)

df_2=pd.DataFrame(final_list)
#print(df_2)

df_2.to_csv('FinalOutputFile.csv',header=None, index=False)
print("Sucessfully generated output CSV")

'''
For folder/directory Structure :
<<<https://github.com/akhilpsin/Tabula_pdf_table_extraction/tree/main/Updatedcode_08.03.22
For breakdown of code
<<<https://github.com/akhilpsin/Tabula_pdf_table_extraction/tree/main/IndividualCode
'''

