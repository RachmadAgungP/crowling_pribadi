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
# https://goletskerja.com/
def remove_values_from_list(the_list, val):
    for i in range(the_list.count(val)):
        the_list.remove(val)
    return the_list
def my_filter(tag):
    return (tag.name == 'li' and
        tag.parent.parent.name == 'li')
def prasyaratan(posisi):
    artikels_pendahuluan = ''
    bol = True
    batas_posisi= [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'h5']
    print (batas_posisi)
    batas_akhir = [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'hr']

    for tagi in posisi.find_all(True)[batas_akhir[-1]:-2]:
        for i in tagi.findAll('a'):
            tty = str(i.get("href"))
            if "disnakerja.com" in tty:
                bol = False
            else:
                bol = True
    if bol == True:
        
        # Posisi
        Posisi = [li.text for li in posisi.find_all(True) if li.name == 'h5']
        
        # Kode
        P_code_fix = []
        Deskripsi_fix = []
        for i in range(len(batas_posisi)):
            if i == len(batas_posisi)-1:
                batass = posisi.find_all(True)[batas_posisi[-1]:batas_akhir[-1]]
                print (batas_posisi[i],"-->",batas_akhir[-1])
            else:
                batass = posisi.find_all(True)[batas_posisi[i]:batas_posisi[i+1]]
                print (batas_posisi[i],"-->",batas_posisi[i+1])
            P_code = [li.text for li in batass if li.name == 'p' and (len(li.text)>5 and len(li.text)<26) or (li.next_sibling.name == 'p' or li.next_sibling.name == 'ol' or li.next_sibling.name == 'ul')]
            Deskripsi = [li.text.split('\n') for li in batass if (li.name == 'ul' or li.name == 'ol') or li.previous_sibling.name == 'p']
            P_code_fix.append(P_code)
            Deskripsi_fix.append(Deskripsi)

        for ini in range (len(P_code_fix)):
            if len(P_code_fix[ini]) > len(Deskripsi_fix[ini]):
                Deskripsi_fix[ini].append([])
            if len(P_code_fix[ini]) < len(Deskripsi_fix[ini]):
                P_code_fix[ini].append("")
            else:
                pass

        # Keterangan 
        tag_a_link = []
        for tag1 in posisi.find_all(True)[batas_akhir[-1]:]:
            if tag1.name != 'div' or tag1.name != 'ins' or tag1.name != 'script':
                tag_a_link.append(tag1.get_text().replace("\n",", "))
                for i in tag1.findAll('a'):
                    tty = str(i.get("href"))
                    if "disnakerja.com" in tty:
                        pass
                    else:
                        tag_a_link.append(tty)
            elif tag1.text == "Apply ":
                pass
            else:
                pass
        Ket = remove_values_from_list(tag_a_link,'')
        Ket = remove_values_from_list(Ket,', , , ')
        # Artikel
        # artik = artikels.artikel(posisi,parafrase1,parafrase2,parafrase3)
        
        # artikels_pendahuluan += artikels.pendahuluan(posisi)
        for ui in range(len(Posisi)):
            artikels_pendahuluan += "<p>" + str(Posisi[ui])+"</p>"
            for oi in range(len(P_code_fix[ui])):
                artikels_pendahuluan += "<p>" + str(P_code_fix[ui][oi])+"</p>"
                artikels_pendahuluan += "<ol>" 
                for ip in range(len(Deskripsi_fix[ui][oi])):
                    print (ip)
                    if ip == len(Deskripsi_fix[ui][oi])-1:
                        artikels_pendahuluan += "</ol>"
                    elif Deskripsi_fix[ui][oi][ip] == "":
                        pass
                    else:
                        artikels_pendahuluan += "<li>"+ str(Deskripsi_fix[ui][oi][ip])+"</li>"
        regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        regex_url = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
        for op in Ket:
            if (re.search(regex_url,op)):
                artikels_pendahuluan += '''<p style="text-align: center;"> <a class="button" style="vertical-align: middle;" href="%s" target="_blank" rel="noopener noreferrer"><button>Apply </button></a> </p>"'''%op
            elif (re.search(regex_email,op)):  
                artikels_pendahuluan += "<p><a href="+"mailto:%s"+">Send email</a></p>"
            elif op == "Apply ":
                pass
            else:
                artikels_pendahuluan += "<p>"+op+"</p>"
        print(artikels_pendahuluan)
        # print (Ket)
        # for y in posisi:
        #     if y.name =='div' or y.name =='script'or y.name =='ins':
        #         pass
        #     else:
        #         artikels_pendahuluan += str(y)
    else:
        pass

    return Posisi, P_code_fix,Deskripsi_fix,Ket,artikels_pendahuluan

URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-samator-gas-industri-2/"

time.sleep(1)
content = requests.get(URL1)
time.sleep(4)
soup = BeautifulSoup(content.text, 'html.parser')  
posisi = soup.find('div',{"class":"entry-content"})
gambar_path = []
daftar_perusahan_hari_ini = []
Kualifikasi = []
posisi_perusahaan =  []
kode_kual = []
Keterangan = []
Applys = []
arti = []
DATA_WEB = prasyaratan(posisi)
posisi_perusahaan.append(DATA_WEB[0])


# tgl = "December 15, 2020"
# # URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-cakrawala-andalas-televisi-antv-2/"
# # URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-kino-food-indonesia-3/"
# # URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-pt-kimia-farma-apotek-kfa/' #sub menu
# # URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-wilmar-group-2/'
# # URL1 ='https://www.disnakerja.com/job/lowongan-kerja-pt-pan-brothers-tbk/'
# # URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-pt-surya-madistrindo/' #Posisi sulit 
# URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-pt-siantar-top-tbk/'
# df_eror = pd.read_csv("Disnaker/appium/Debug/Data_debug/%s/data_saat_Debug.csv"%tgl)
# print (df_eror.columns)
# tgl_post = tgl.split()
# gambar_path = []
# daftar_perusahan_hari_ini = []
# Kualifikasi = []
# posisi_perusahaan =  []
# kode_kual = []
# Keterangan = []
# Applys = []
# tgl_now = []
# alamats = []
# alamat_error = []
# judull = []

# # mainnya 
# for index,row in df_eror.iterrows():
#     print ("URL 2 ->",row["Alamat"])
#     time.sleep(1)
#     content1 = requests.get(row["Alamat"])
#     time.sleep(4)
#     soup1 = BeautifulSoup(content1.text, 'html.parser')
#     posisi = soup1.find('div',{"class":"entry-content"})

#     if tgl_post[1][0] == '0':
#         tgl_post[1] = tgl_post[1][1:]
#     else:
#         tgl_post[1] = tgl_post[1]

#     alamats.append(URL1)
#     print (tgl_post)
#     judul = soup1.find('h1',{"class":"entry-title"}).text
#     judull.append(judul)
#     # try:
#     # posisi = soup1.find('div',{"class":"entry-content"})
#     # print (posisi)
#     h_all = posisi.find_all(True)
#     if "Jika dokumen dibawah" in posisi.get_text() :
#         alamat_error.append(URL1)
#         print ("ini ",judull)
#         pass
#     else:
#         judul = judul.replace("Lowongan Kerja ","")
#         judul = judul.replace("/n","")
#         judul = judul.replace("/"," ")
#         judul = judul.replace(".","")
#         gambar = 'E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg'
#         # urllib.request.urlretrieve(gambar,str('images/'+judul+'.jpg'))
#         daftar_perusahan_hari_ini.append(judul)
#         gambar_path.append('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
        
#         DATA_WEB = prasyaratan(posisi)
#         print (judul)
#         posisi_perusahaan.append(DATA_WEB[0])
#         Kualifikasi.append(DATA_WEB[2])
#         kode_kual.append(DATA_WEB[1])
#         Applys.append(DATA_WEB[3])
#         Keterangan.append(DATA_WEB[4])
#         tgl_now.append(tgl)


# Kolom_1 = pd.Series(daftar_perusahan_hari_ini)
# Kolom_2 = pd.Series(posisi_perusahaan)
# Kolom_3 = pd.Series(Kualifikasi)
# Kolom_4 = pd.Series(kode_kual)
# Kolom_5 = pd.Series(gambar_path)
# Kolom_6 = pd.Series(Keterangan)
# Kolom_7 = pd.Series(Applys)
# kolom_8 = pd.Series(tgl_now)

# Ex = {'Nama':Kolom_1,'Posisi':Kolom_2,'Kualifikasi':Kolom_3,'kode_kual':Kolom_4,'Path_Gambar':Kolom_5,'Keterangan':Kolom_6,'Apply':Kolom_7,'Tanggal':kolom_8}
# df = pd.DataFrame(Ex)

# DATA_Posisi = df['Posisi']
# DATA_kode = df['kode_kual']
# DATA_kualif = df['Kualifikasi']

# print (DATA_kode[0][1])
# print (DATA_kualif[0][1])
# print (len(DATA_kode[0][1]),"-",len(DATA_kualif[0][1]))
# # print(DEBUG_TAG_HTML[0])

# df.to_csv('hasil/%s/data_saat_Debug.csv'%tgl, mode = 'a', header = False)

