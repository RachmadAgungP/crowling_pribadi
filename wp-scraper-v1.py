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
def prasyaratan(posisi):
    h_all = posisi.find_all(True)
    y = -1
    no = 0
    Kualifikasi = []
    kode_kualif = []
    Posisi = []
    link = []
    keterangan = []
    footer = []
    for tag in posisi.find_all(True):
        lii = []
        if tag.name =='h5':
            Posisi.append(tag.get_text().replace("\n",""))
            kode_kualif.append([])
            Kualifikasi.append([])
            y+=1
            if tag.next_sibling.next_sibling.name == 'p':
                if tag.next_sibling.next_sibling.string is None :
                    kode_kualif[y].append(tag.next_sibling.string.replace("\n",""))
                else:  
                    kode_kualif[y].append(tag.next_sibling.next_sibling.string.replace("\n",""))
            elif tag.next_sibling.next_sibling.name == 'h5':
                Kualifikasi[y].append([])
                kode_kualif[y].append([])
            else:
                kode_kualif[y].append([])
        elif tag.name == 'ol' or  tag.name == 'ul':
            if tag.next_sibling.next_sibling.name == 'ol':
                pass
            else:
                for yo in tag.findAll('li'):
                    lii.append(yo.text)
                Kualifikasi[y].append(lii)
            try:
                if tag.next_sibling.next_sibling.name == 'p':
                    kode_kualif[y].append(tag.next_sibling.next_sibling.string.replace("\n",""))
            except Exception as exception:
                if tag.name =='h5':
                    print ("error ",tag.text)
                    print ("errornya ",exception)
                pass
        elif tag.name == 'hr':
            footer.append(no)
            if tag.next_sibling.next_sibling.name == "div":
                if tag.next_sibling.next_sibling.name == 'p':
                    kode_kualif[y].append(tag.next_sibling.next_sibling.string.replace("\n",""))
            if tag.previous_sibling.previous_sibling.name == 'p':
                if tag.previous_sibling.previous_sibling["style"] == "text-align: center;" or tag.previous_sibling.previous_sibling["style"] == "text-align: justify;":
                    pass
                else:
                    Kualifikasi[y].append([])
            else:
                pass
        no += 1
    for t in range(footer[-1],len(h_all)-1):
        if h_all[t].text == "" or h_all[t].text == "|||":
            continue
        if h_all[t].name == 'p':
            for i in h_all[t].findAll('a'):
                tty = str(h_all[t].text.replace(" Apply "," ")+i.get("href"))
                link.append(tty)
        if "Apply \xa0– " in h_all[t].text or " Apply " in h_all[t].text:
            continue
        keterangan.append(h_all[t].text.replace("\n",", "))

    return (Posisi,kode_kualif,Kualifikasi,link,keterangan,footer,h_all)

now = datetime.datetime.now()
tgl = now.strftime("%B %d, %Y")
# "November 19, 2020"
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
for i in range (1,2):
    URL = 'https://www.disnakerja.com/page/%s/'%i
    # URL = 'https://loker.disnakerja.com/page/%s/'%i
    print ("URL 1 ->",URL)
    time.sleep(1)
    content = requests.get(URL)
    time.sleep(4)
    soup = BeautifulSoup(content.text, 'html.parser')
    objek = soup.find('div')
    cards  = objek.find_all('tr')
    # print (cards)
    for card in cards:
        judul = card.find('h3',{ "class" : "entry-title"}).get_text()
        alamat = card.find('a').get('href')
        bulan_tahun = str(tgl_post[0]+' '+tgl_post[-1])
        URL1 = alamat
        print ("URL 2 ->",URL1)
        time.sleep(1)
        content1 = requests.get(URL1)
        time.sleep(4)
        soup1 = BeautifulSoup(content1.text, 'html.parser')
        cards1  = soup1.find('span',{ "class" : "entry-date"}).get_text()
        print(cards1[3:].split())
        if tgl_post[1][0] == '0':
            tgl_post[1] = tgl_post[1][1:]
        else:
            tgl_post[1] = tgl_post[1]
        if (cards1[3:].split() == tgl_post):
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
                    gambar = card.find('img').attrs['src']
                    urllib.request.urlretrieve(gambar,str('images/'+judul+'.jpg'))
                    daftar_perusahan_hari_ini.append(judul)
                    gambar_path.append('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
                    
                    masuk =  prasyaratan(posisi)
                    print (judul)
                    posisi_perusahaan.append(masuk[0])
                    Kualifikasi.append(masuk[2])
                    kode_kual.append(masuk[1])
                    Applys.append(masuk[3])
                    Keterangan.append(masuk[4])
                    tgl_now.append(tgl)


            except Exception as e:
                print ("error",judul)
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                alamat_error.append(URL1)
                gambar_path.remove('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
                daftar_perusahan_hari_ini.remove(judul)
        else:
            pass

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
print (df)
alamat_er = pd.Series(alamat_error)
df_er = pd.DataFrame(alamat_er)
# df_er.to_csv('data_alamat_error.csv')
# df.to_csv('data_namapekerjaan1.csv')

df_er.to_csv('Loker1_data_alamat_error.csv')
df.to_csv('Loker1_data_namapekerjaan1.csv')

# print(df)

# for y in alamat_error:
#     print (y)
print (judull)
print (len(judull))

    

