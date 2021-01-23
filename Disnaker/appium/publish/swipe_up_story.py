import pandas as pd
import ast
import win32com.client as win32
import os
import textwrap
import datetime

now = datetime.datetime.now()
# tgl = str(now.strftime("%B %d, %Y"))
tgl = "December 22, 2020"
df = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl)
print (df.columns)