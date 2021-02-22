from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
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
import _parse_content
import _download_gambar
import _tgl_

def decode(cfemail):
    enc = bytes.fromhex(cfemail)
    return bytes([c ^ enc[0] for c in enc[1:]]).decode('utf8')

# URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-tracon-industri/"
# print ("URL 2 ->",URL1)
# time.sleep(1)
# content1 = requests.get(URL1)
# time.sleep(4)
# soup1 = BeautifulSoup(content1.text, 'html.parser')
# posisi = soup1.find('div',{"class":"entry-content"})
# emails = soup1.find_all('a',{"class":"__cf_email__"})
# for y in emails:
#     hashed_email = str(y).split(" ")[2].split('"')[1]
#     # print (str(y).split(" ")[2].split('"')[1])
#     print (decode(hashed_email))


import os
import shutil

# os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
# for i in 

import _tgl_
tgl = _tgl_.baca_file()
nama_folder_foto = _tgl_.data_proses_foto(tgl)[0]
nama_foto = _tgl_.data_proses_foto(tgl)[1]

folder = []
for yo in range(len(nama_foto)):
    nama = []
    for yi in nama_foto[yo]:
        nama.append("hasil/%s/%s/%s"%(tgl,nama_folder_foto[yo],yi))
    shutil.move('hasil/hasil2/0.jpg', str(nama[0]))
    # os.replace(str(nama[0]), 'hasil/hasil2/0.jpg')
    folder.append(nama[0])
    print (nama[0])