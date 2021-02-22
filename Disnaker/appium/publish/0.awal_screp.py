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
import _crop_foto
def unique(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]
def prasyaratan(posisi):
    batas_p = posisi.find_all(True)[0]
    batas_posisi= [i for i,li in enumerate(posisi.find_all(True)) if (li.name == 'h3' or li.name == 'h2' or li.name == 'h4') and li.next_element.name == 'strong']
    
    batas_akhir = [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'hr']
    print (batas_akhir)
    # # Posisi
    Posisi = [li.text for li in posisi.find_all(True) if (li.name == 'h3' or li.name == 'h2' or li.name == 'h4') and li.next_element.name == 'strong']
    
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
        P_code = []
        for li in batass:
            if li.name == 'p' and len(li.text)<30:
                if '•' in li.text:
                    P_code.append(li.text[:li.text.index(":")-1])
                else:
                    P_code.append(li.text)
        # Deskripsi = [li.text.split("\n") for li in batass if (li.name == 'p' and "•" in li.text) or li.name == 'ul' or li.name == 'ol']
        Deskripsi = [[rey.text for rey in y] for y in batass if y.name == 'ol' or y.name == 'ul']
        # print ("ini_coba",rep)
        P_code_fix.append(P_code)
        Deskripsi_fix.append(Deskripsi)
    
    for ini in range (len(P_code_fix)):
        if len(P_code_fix[ini]) > len(Deskripsi_fix[ini]):
            Deskripsi_fix[ini].append([])
        if len(P_code_fix[ini]) < len(Deskripsi_fix[ini]):
            P_code_fix[ini].append(".")
        else:
            pass


    # Keterangan 
    tag_a_link = []
    for tag1 in posisi.find_all(True)[batas_akhir[-1]:]:
        if tag1.name == 'div':
            for i in tag1.findAll('a'):
                tty = str(i.get("href"))
                if "goletskerja.com" in tty:
                    pass
                if "api.whatsapp" in tty:
                    pass
                else:
                    tag_a_link.append(tty)
        elif tag1.name == 'p':
            if tag1.text is None:
                print ("yes")
                pass
            elif "Baca Juga :" in tag1.text or "Join Channel Telegram" in tag1.text or "GOLETSKERJA" in tag1.text or "Goletskerja" in tag1.text:
                pass
            else:
                tag_a_link.append(tag1.text.replace("\n",", "))
        elif tag1.name == 'li':
            tag_a_link.append(tag1.text)

    Ket = tag_a_link
    if len(Posisi) == 0 or len(P_code)== 0 or len(Deskripsi_fix)== 0:
        pass
    else:
        print (Posisi)
        print (P_code_fix)
        print (Deskripsi_fix)
        print (unique(Ket))
        print (batas_p)
    return Posisi, P_code_fix,Deskripsi_fix,unique(Ket),batas_p
        
import _download_gambar
# URL = "https://goletskerja.com/lowongan-kerja-pt-indonesia-oppo-electronics-2/" fix
# URL ="https://goletskerja.com/lowongan-kerja-pt-len-rekaprima-semesta-2/" fix
# URL = "https://goletskerja.com/lowongan-kerja-pt-infomedia-nusantara-telkom-group-2/"
import _tgl_
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
URL2 = "https://goletskerja.com/"
time.sleep(1)
content1 = requests.get(URL2)
soup1 = BeautifulSoup(content1.text, 'html.parser')
conten = soup1.find('div',{"class":"td_block_inner"})
tgls = soup1.find_all('span',{"class":"td-post-date"})
month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
month_id = ["Januari","Februari","Maret","April","Mai","Juni","Juli","Agustus","September","Oktober","November","Desember"]
io = [i.findPrevious("a").get("href") for i in conten.find_all(True) if i.text.replace(i.text.split(' ')[0],month[month.index(_tgl_.baca_file().split(' ')[0])]) == _tgl_.baca_file()]
URL1s = list(set(io))
# print (len(URL1s))
tgl = _tgl_.baca_file()
for URL1 in URL1s:
    time.sleep(1)
    content = requests.get(URL1)
    time.sleep(4)
   
    soup = BeautifulSoup(content.text, 'html.parser')
    # posisi = soup.find('div',{"class":"td-post-content"})
    # newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/text'.format(tgl) 
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)
    # texts = open("E:/Belajar/www.disnakerja.com/hasil/%s/text/%s.txt"%(tgl,"soapp"), "w", encoding='utf-8-sig')
    # texts.write(str(soup11))
    # texts.close()
    judul = soup.find('h1',{ "class" : "entry-title"}).get_text()
    print (judul+"ya")
    try:
        # posisi = soup1.find('div',{"class":"entry-content"})
        posisi = soup.find_all('div',{"class":"td-post-content"})
        for y in posisi:
            if y.name == 'blockquote':
                print (y.find('blockquote').decompose())
        # print (posisi)
        # if "Jika dokumen dibawah" in posisi.text() :
        #     alamat_error.append(URL1)
        #     print ("ini ",judull)
        #     pass   
        # else:
        tag_atas = []
        r = 0
        for i,y in enumerate(posisi): 
            if y.name =='div' or y.name =='script'or y.name =='ins' and y == '\n' or y == " ":
                pass
            else:
                tag_atas.append(y)
                r += 1
        tagss = tag_atas

        batas_hr = [o for o,u in enumerate(tagss) if u.name == 'hr']
        tags_html = " "
        atas_text = [li.text for li in tagss[0:batas_hr[0]] if li.name == 'p' and "Adapun hal-hal yang perlu untuk kamu" not in li.text and "Tentang kami\xa0goletskerja.com\xa0" not in li.text and "goletskerja.com" not in li.text and "adalah situs Portal lowongan kerja yang menjangkau seluruh " not in li.text]         
        tags_html += ' '.join(str(i) for i in atas_text)
        tags_html +='''<p> Untuk beberapa orang, dalam mencari pekerjaan adalah sesuatu hal yang cukup sulit. kalaupun mendapatkan pekerjaan itu mudah, belum tentu itu sesuai dengan apa yang kita inginkan. Yang terpenting sekarang adalah ikhtiar, Semangat, dan berusaha. Sesulit apapun dalam mencari kerja, kita tetap yakin kita masih punya Allah SWT yang maha kaya dan tetap pantang menyerah.</p>
                    <p> Kegagalan bukan bearti Anda berakhir dalam menjalani kehidupan, Manakala Anda Masih diberikan kenikmatan hidup sembari terus mencoba dan belajar dalam mengembangkan bisnis. Orang-orang mungkin menganggap anda telah gagal. Namun jika anda masih tetap terus berjuang mencoba dan menikmati hidup, maka anda belum berada pada kegagalan. Durasi Hidup Anda Akan Terasa Singkat Ketika Rasa Dendam Masih Memenuhi Kepala Anda. Jangan biarkan isi kepala dan hari-hari anda dipenuhi rasa dendam, karena itu akan membuat hidup anda penuh kegelapan dan takkan memiliki makna. Ujung -ujungnya adalah mempersingkat hidup anda. Yang Berani Mendengar adalah Mereka yang Memiliki Sejuta Angan-angan Belaka. Yang Berani Melihat adalah Mereka yang Memiliki Sejuta Impian Belaka. Dan Yang Berani Mencoba adalah Mereka yang Akan Memiliki Angan-angan dan Impian yang Nyata.</p>
                    '''
        alamats.append(URL1)
        # print (tgl_post)
        
        judull.append(judul)
        judul = judul.replace("Lowongan Kerja ","")
        judul = judul.replace("/n","")
        judul = judul.replace("/"," ")
        judul = judul.replace(".","")
        foto = soup.find('div',{"class":"td-post-featured-image"})
        gambar = foto.find('img').attrs['src']
        urllib.request.urlretrieve(gambar,str('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg'))
        daftar_perusahan_hari_ini.append(judul)
        _crop_foto.save_foto('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
        gambar_path.append('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
        masuk = prasyaratan(posisi)
        posisi_perusahaan.append(masuk[0])
        Kualifikasi.append(masuk[2])
        kode_kual.append(masuk[1])
        Keterangan.append(masuk[3])
        tgl_now.append(tgl)
        header.append(tags_html)
    except Exception as e:
        print ("error",judul)
        print ("errornya: ",e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        alamat_error.append(URL1)
        # gambar_path.remove('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
        # daftar_perusahan_hari_ini.remove(judul)
        # alamats.remove(URL1)
        # tgl_now.remove(tgl)
        pass

Kolom_1 = pd.Series(daftar_perusahan_hari_ini)
Kolom_2 = pd.Series(posisi_perusahaan)
Kolom_3 = pd.Series(Kualifikasi)
Kolom_4 = pd.Series(kode_kual)
Kolom_5 = pd.Series(gambar_path)
Kolom_6 = pd.Series(Keterangan)
Kolom_7 = pd.Series(tgl_now)
kolom_8 = pd.Series(alamats)
kolom_9 = pd.Series(header)
# # 
Ex = {'Nama':Kolom_1,'Posisi':Kolom_2,'Kualifikasi':Kolom_3,'kode_kual':Kolom_4,'Path_Gambar':Kolom_5,'Keterangan':Kolom_6,'Tanggal':Kolom_7,'Alamat':kolom_8,'header':kolom_9}
df = pd.DataFrame(Ex)
print (df)
alamat_er = pd.Series(alamat_error)
df_er = pd.DataFrame(alamat_er)
newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}'.format(tgl) 
if not os.path.exists(newpath):
    os.makedirs(newpath)
df_er.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/data_alamat_error_new.csv'%tgl, mode='a', header=False)

df.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/data_namapekerjaan1_new.csv'%tgl)

# URL2 = "https://goletskerja.com/"
# time.sleep(1)
# content1 = requests.get(URL)
# soup = BeautifulSoup(content1.text, 'html.parser')
# posisi = soup.find('div',{"class":"td-post-content"})
# # conten = soup1.find('div',{"class":"td_block_inner"})
# tag_atas = []
# r = 0
# for i,y in enumerate(posisi.find_all(True)): 
#     if y.name =='div' or y.name =='script'or y.name =='ins' and y == '\n' or y == " ":
#         pass
#     else:
#         tag_atas.append(y)
#         r += 1
# tagss = tag_atas

# batas_hr = [o for o,u in enumerate(tagss) if u.name == 'hr']
# tags_html = " "
# atas_text = [li.text for li in tagss[0:batas_hr[0]] if li.name == 'p' and "Adapun hal-hal yang perlu untuk kamu" not in li.text and "Tentang kami\xa0goletskerja.com\xa0" not in li.text and "goletskerja.com" not in li.text and "adalah situs Portal lowongan kerja yang menjangkau seluruh " not in li.text]         
# tags_html += ' '.join(str(i) for i in atas_text)
# print (atas_text)

# data = prasyaratan(posisi)
# print ("posisi =", data[0])
# print ("posisi =", len(data[0]))
# print ("code =", data[1])
# print ("code =", len(data[1]))
# print ("desc =", data[2])
# print ("desc =", len(data[2]))
# print ("ket =", data[3])


