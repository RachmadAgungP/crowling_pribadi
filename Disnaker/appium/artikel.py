from bs4 import BeautifulSoup, NavigableString, Tag # BeautifulSoup is in bs4 package
import requests
import re 
import string
import time
import pandas as pd
import datetime
import urllib.request
import os
import time
import sys



now = datetime.datetime.now()
tgl = now.strftime("%B %d, %Y")
# "November 19, 2020"
tgl = "December 17, 2020"
tgl_post = tgl.split()
print (tgl)
# judul PT

artikels = []
web1 = 'www.disnakerja.com'
web2 = 'loker.disnakerja.com'
for i in range (1,3):
    URL = 'https://%s/page/%s/'%(web1,i)
    # URL = 'https://%s/page/%s/'%(web2,i)
    print ("URL 1 ->",URL)
    time.sleep(1)
    content = requests.get(URL)
    time.sleep(4)
    soup = BeautifulSoup(content.text, 'html.parser')
    objek = soup.find('div')
    cards  = objek.find_all('tr')
    # print (cards)
    time.sleep(4)
    artikelsr = ''' '''
    for y in posisi.find_all(True):
        if y.name =='div' or y.name =='script'or y.name =='ins':
            pass
        else:
            artikelsr += str(y)
    artikels.append(artikelsr)

kolom_10 = pd.Series(artikels)
# # 
Ex = {'artikel':kolom_10}
df = pd.DataFrame(Ex)
print (df)
alamat_er = pd.Series(alamat_error)
df_er = pd.DataFrame(alamat_er)
newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/artikel'.format(tgl) 
if not os.path.exists(newpath):
    os.makedirs(newpath)
df.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/artikel/artikel.csv'%tgl)
# df.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/data_coba.csv'%tgl)
# df_er.to_csv('Loker1_data_alamat_error.csv')
# df.to_csv('Loker1_data_namapekerjaan1.csv')

# print(df)

# for y in alamat_error:
#     print (y)
print (judull)
print (len(judull))

    

