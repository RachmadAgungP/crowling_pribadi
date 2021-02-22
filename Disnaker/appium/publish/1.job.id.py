from bs4 import BeautifulSoup # BeautifulSoup is in bs4 package 
import requests
import re 
import string
import _download_gambar
import _tgl_
import pandas as pd
import urllib.request
from PIL import Image

tgl = _tgl_.baca_file()
gambar_path = []
daftar_perusahan_hari_ini = []
Kualifikasi = []
posisi_perusahaan =  []
kode_kual = []
Keterangan = []
tgl_now = []
alamats = []
alamat_error = []
judull = []
header = []
datas = []
"https://www.jobs.id/lowongan-kerja?halaman=1"
for inn in range(1,4):
    path_image = "E:/Belajar/www.disnakerja.com/images/"
    URL = "https://www.jobs.id/lowongan-kerja?halaman=%s"%inn
    print ("URL 1 ->",URL)
    content = requests.get(URL)
    soup = BeautifulSoup(content.text, 'html.parser')
    objek = soup.find('div',{"id": "job-ads-container"})
    tui = objek.find("div",{"class":"col-xs-12 single-job-ads"})
    for y in tui.find_all(True):
        if y.get("class")==["text-muted"]:
            if y.text.strip() == "Hari ini" or y.text.strip() == "Kemarin":
                for y in objek.find_all("div",{"class":"col-xs-12 single-job-ads"}):
                    data = []
                    for oi in y.find("div",{"class":"col-xs-8 col-md-10"}):
                        if oi.name == "p":
                            if oi.get("class")==["text-muted"]:
                                if oi.text.strip() == "Hari ini":
                                    for oio in y.find("div",{"class":"col-xs-8 col-md-10"}):
                                        if oio.name == "h3":
                                            # data.append(oio.get_text().replace("\n"," "))
                                            posisi_perusahaan.append([oio.get_text().replace("\n"," ")])
                                            for iy in oio.find_all('a', href=True):
                                                datas.append(str(iy.get("href")))
                                                alamats.append(str(iy.get("href")))
                                        if oio.name == "p":
                                            for io in oio.find_all('strong',{"class":"text-muted"}):
                                                # data.append(str(io.text))
                                                daftar_perusahan_hari_ini.append(str(io.text))
                                            for io in oio.find_all('a',{"class":"bold"}, href=True):
                                                # data.append(str(io.text))
                                                daftar_perusahan_hari_ini.append(str(io.text))  
                                                
                                    iu = 0
                                    for ooi in y.find("div",{"class":"col-xs-2 col-md-2"}):
                                        if ooi.name == "img":
                                            gambar = ooi.attrs['src']
                                            if "https:" in gambar :
                                                gambar = gambar
                                            else:
                                                gambar = gambar.replace("//","https://")
                                            pathh = path_image+daftar_perusahan_hari_ini[-1]+".png"
                                            if ".jpg" in gambar:
                                                pathh = path_image+daftar_perusahan_hari_ini[-1]+".jpg"
                                                urllib.request.urlretrieve(gambar,str(path_image+daftar_perusahan_hari_ini[-1]+".jpg"))
                                            else:
                                                pathh =path_image+daftar_perusahan_hari_ini[-1]+".png"
                                                urllib.request.urlretrieve(gambar,str(path_image+daftar_perusahan_hari_ini[-1]+".png"))
                                                # im1 = Image.open(r'path_image%s'%daftar_perusahan_hari_ini[-1])
                                                # im1.save(r'path_image%s'%daftar_perusahan_hari_ini[-1]+'.jpg')

                                            # _download_gambar.maine(gambar,str('path_image'+data[2]+'.jpg'))
                                            # urllib.request.urlretrieve(gambar,str('path_image'+daftar_perusahan_hari_ini[-1]+'.jpg'))
                                            # im1 = Image.open(r'')
                                            # im1.save(r'path where the JPG will be stored\new file name.jpg')

                                            gambar_path.append(pathh)
                                            # print (ooi.attrs['src'])
                                            print (daftar_perusahan_hari_ini[-1])
                                        iu += 1
            else:
                ("break")
                break

# # print (datas)
# # print (gambar_path)
# # print (daftar_perusahan_hari_ini)
# # print (posisi_perusahaan)
# # print (alamats)
# # header = []

index = 0
for you in datas:
    links = datas[index]
    content = requests.get(links)
    soup = BeautifulSoup(content.text, 'html.parser')
    posisi = soup.find('div',{"class": "panel-body"})
    kod_kual = []
    kual = []
    for too in posisi.find_all(True):
        if too.name == "h3":
            kod_kual.append(too.text.replace('\n'," ").strip())
            # print (too.text)
        if too.name == "div":
            # print (too.get("class")== ['job_desc'])
            if too.get("class")== ['job_desc']:
                kual.append(too.text.replace('\xa0'," ").split('\n'))
                # print (too)
            elif too.get("class")== ["job_req"]:
                kual.append(too.text.replace('\xa0'," ").split('\n'))
            else:
                pass
    Kualifikasi.append([kual])
    kode_kual.append([kod_kual])

    str_keterangan = " "
    location = soup.find("span",{"class":"location"}).text.replace("\n"," ").strip()
    str_keterangan += "\n lokasi: %s"%location
    gaji = soup.find_all("div",{"class":"col-xs-12 col-sm-6 col-md-4"})
    str_keterangan += ("\n"+"\n ".join([" ".join(i.text.replace("\n","").strip().split()) for i in gaji]))
    batas_waktu = soup.find_all("div",{"class":"col-xs-6"})
    str_keterangan += ("\n"+" - ".join([" ".join(i.text.replace("\n","").strip().split()) for i in batas_waktu][:2]))
    link_daftar = links
    str_keterangan += ("\n link: %s"%link_daftar)
    Keterangan.append(str_keterangan.split("\n"))
    if soup.find("div",{"class":"about-company"}) == None:
        header.append("_None_")
    else:
        headerr = soup.find("div",{"class":"about-company"}).text.replace("\n","").replace("\r","").replace("\t","").strip()
        header.append(headerr)
        tgl_now.append(tgl)
        print ("in",daftar_perusahan_hari_ini[index])
    index += 1

Kolom_1 = pd.Series(daftar_perusahan_hari_ini)
Kolom_2 = pd.Series(posisi_perusahaan)
Kolom_3 = pd.Series(Kualifikasi)
Kolom_4 = pd.Series(kode_kual)
Kolom_5 = pd.Series(gambar_path)
Kolom_6 = pd.Series(Keterangan)
Kolom_7 = pd.Series(tgl_now)
kolom_8 = pd.Series(alamats)
kolom_9 = pd.Series(header)

Ex = {'Nama':Kolom_1,'Posisi':Kolom_2,'Kualifikasi':Kolom_3,'kode_kual':Kolom_4,'Path_Gambar':Kolom_5,'Keterangan':Kolom_6,'Tanggal':Kolom_7,'Alamat':kolom_8,'header':kolom_9}
df = pd.DataFrame(Ex)
df = df[df.header != "_None_"]
df = df [df.Nama != "Perusahaan Dirahasiakan"]
df.to_csv("E:/Belajar/www.disnakerja.com/hasil/%s/data_namapekerjaan1.csv"%tgl, mode='a', header=False)

