
import os
from ast import literal_eval
# string = "when an unknown printer took a galley of type and scrambled it to make a type specimen book."
import urllib.request
# import textwrap
# print (textwrap.wrap(string,20))
import re 
import string
import time
import datetime
import sys
from bs4 import BeautifulSoup, NavigableString, Tag # BeautifulSoup is in bs4 package
import requests
import pandas as pd
# p

tgl = "December 10, 2020"
tgl_post = tgl.split()
print (tgl)
# judul PT
gambar_path = []
daftar_perusahan_hari_ini = []
Kualifikasi = []
posisi_perusahaan =  []
kode_kual = []
Keterangan = []
Applys = []
tgl_now = []
alamats = []
alamat_error = []
judull = []
def prasyaratan(posisi):
    HTML_tag_names = []
    HTML_tag_name = []
    index_h5 = []
    index_hr = []
    index_div = []
    h = 0
    for tag in posisi.find_all(True):
        if tag.name == 'h5':
            index_h5.append(h) 
        if tag.name == 'hr':
            index_hr.append(h)
        if tag.name == 'div':
            index_div.append(h)
        h+=1
    # print ("index_hr ",index_hr)
    # print("ininini",posisi.find_all(True)[49])
    DATA_Posisi = []
    DATA_kode = []
    DATA_kualif = []

    # DATA_POSISI = []
    index_h5.append(index_hr[-1])
    # print ("index ",index_h5)
    for u in range(len(index_h5)-1):
        HTML_tag_name = []

        # tag_h5_Posisi = []
        tag_p_kode = []
        tag_p_kualif = []

        ind = index_h5[u]
        for tagg in posisi.find_all(True)[index_h5[u]:index_h5[u+1]]:
            if tagg.name == 'h5':
                DATA_Posisi.append(tagg.get_text().replace("\n",""))
            elif tagg.name == 'p':
               
                text = ''
                if isinstance(tagg, NavigableString):
                    text += str(tagg).strip()
                elif isinstance(tagg, Tag):
                    if tagg.name != 'br':
                        text += tagg.text.strip()
                    else:
                        text += '\n'
                if posisi.find_all(True)[ind+1].name == 'span':
                    print ("dsd")
                    pass
                else:
                    # print (text)
                    result = text.strip().split('\n')
                    indx = 0
                    for yss in result:
                        if indx == 0:
                            if len(yss) > 26:
                                pass
                            else:
                                tag_p_kode.append(yss)
                        if len(yss) > 26:
                            if posisi.find_all(True)[ind+1].name == 'br':
                                pass
                            else:
                                tag_p_kualif.append([yss])
                        indx += 1
                    if posisi.find_all(True)[ind+1].name == 'br':
                        tag_p_kualif.append(result[1:])

             
            HTML_tag_name.append([tagg.name])
            ind +=1

        yus = []
        for yo in posisi.findAll("li"):
            yus.append(yo.text)
        tag_p_kualif.append(yus) 

        HTML_tag_names.append(HTML_tag_name)
        # DATA_Posisi.append(tag_h5_Posisi)
        DATA_kode.append(tag_p_kode)
        DATA_kualif.append(tag_p_kualif)

        if len(DATA_kode[0]) > len(DATA_kualif[0]):
            for iu in range(len(DATA_kualif[0]),len(DATA_kode[0])):
                DATA_kualif[0].append([])
        else:
            for iui in range(len(DATA_kode[0]),len(DATA_kualif[0])):
                DATA_kode[0].append([])
    footer = posisi.find_all(True)[index_hr[-1]:h]
    HTML_tag_footer = [] #keteranagan
    tag_a_link = []
    for tag1 in footer:
        if tag1.name == 'p':
            HTML_tag_footer.append(tag1.get_text().replace("\n",", "))
            for i in tag1.findAll('a'):
                tty = str(tag1.text.replace(" Apply "," ")+i.get("href"))
                tag_a_link.append(tty)
        if tag1.text == "" or tag1.text == "|||":
            continue
        if "Apply \xa0– " in tag1.text or " Apply " in tag1.text:
            continue
    return (DATA_Posisi,DATA_kode,DATA_kualif,tag_a_link,HTML_tag_footer,index_h5,HTML_tag_names)

now = datetime.datetime.now()
tgl = now.strftime("%B %d, %Y")
# "November 19, 2020"
tgl = "December 10, 2020"
tgl_post = tgl.split()

# prasyaratan(posisi)

bulan_tahun = str(tgl_post[0]+' '+tgl_post[-1])
# URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-cakrawala-andalas-televisi-antv-2/"
# URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-temas-tbk/"
URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-pt-pan-brothers-tbk/'
print ("URL 2 ->",URL1)
time.sleep(1)
content1 = requests.get(URL1)
time.sleep(4)
soup1 = BeautifulSoup(content1.text, 'html.parser')
judul = soup1.find('h1',{ "class" : "entry-title"}).get_text()
cards1  = soup1.find('span',{ "class" : "entry-date"}).get_text()
print(cards1[3:].split())

alamats.append(URL1)
print (tgl_post)
judull.append(judul)
try:
    posisi = soup1.find('div',{"class":"entry-content"})
    # print (posisi)
    h_all = posisi.find_all(True)
    if "Jika dokumen dibawah" in posisi.get_text() :
        alamat_error.append(URL1)
        print ("ini ",judull)
        pass
    else:
        judul = judul.replace("Lowongan Kerja ","")
        judul = judul.replace("/n","")
        judul = judul.replace("/"," ")
        judul = judul.replace(".","")
        gambar = 'images/'+judul+'.jpg'
        # urllib.request.urlretrieve(gambar,str('images/'+judul+'.jpg'))
        daftar_perusahan_hari_ini.append(judul)
        gambar_path.append('E:/Belajar/www.disnakerja.com/%s'%gambar)
        
        masuk =  prasyaratan(posisi)
        print (judul)
        posisi_perusahaan.append(masuk[0])
        print (posisi_perusahaan)
        Kualifikasi.append(masuk[2])
        print(Kualifikasi)
        kode_kual.append(masuk[1])
        print(kode_kual)
        Applys.append(masuk[3])
        Keterangan.append(masuk[4])
        print (Keterangan)
        tgl_now.append(tgl)

except Exception as e:
    print ("error",judul)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    alamat_error.append(URL1)
    gambar_path.remove('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
    daftar_perusahan_hari_ini.remove(judul)


Kolom_1 = pd.Series(daftar_perusahan_hari_ini)
Kolom_2 = pd.Series(posisi_perusahaan)
Kolom_3 = pd.Series(Kualifikasi)
Kolom_4 = pd.Series(kode_kual)
Kolom_5 = pd.Series(gambar_path)
Kolom_6 = pd.Series(Keterangan)
Kolom_7 = pd.Series(Applys)
kolom_8 = pd.Series(tgl_now)
# # 
Ex = {'Nama':Kolom_1,'Posisi':Kolom_2,'Kualifikasi':Kolom_3,'kode_kual':Kolom_4,'Path_Gambar':Kolom_5,'Keterangan':Kolom_6,'Apply':Kolom_7,'Tanggal':kolom_8}
df = pd.DataFrame(Ex)
alamat_er = pd.Series(alamat_error)
df_er = pd.DataFrame(alamat_er)

# df_er.to_csv('Debug_data_error.csv')
df.to_csv('Debug_data_namapekerjaan1.csv')

# for i in df['Kualifikasi'][0]:
#     print (t,"->>",i[0])
#     t+=1
print(df['kode_kual'][0])
# print (df['Kualifikasi'])
# tgl_now.append(tgl)