import pandas as pd
import openpyxl
df = pd.read_excel("C:\projects\mysite\static\행정_법정동 중심좌표.xlsx", engine="openpyxl")

df2 = df[['시도', '시군구', '읍면동', '위도', '경도']]


for idx,row in df2.iterrows():

    addr = str(row['시도'])+" "+str(row['시군구'])+" "+str(row['읍면동'])
    print(addr)