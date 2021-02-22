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

# now = datetime.datetime.now()
# tgl = now.strftime("%B %d, %Y")
# "November 19, 2020"
# tgl = "December 10, 2020"
def maine(tgl):
    tgl_post = tgl.split()
    print (tgl)
    # judul PT
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
    for i in range (1,3):
        URL = 'https://www.disnakerja.com/page/%s/'%i
        # URL = 'https://loker.disnakerja.com/page/%s/'%i
        print ("URL 1 ->",URL)
        time.sleep(5)
        content = requests.get(URL)
        # time.sleep(4)
        soup = BeautifulSoup(content.text, 'html.parser')
        try:
            objek = soup.find('div')
            cards  = objek.find_all('tr')
            # print (cards)
            for card in cards:
                
                judul = card.find('h3',{ "class" : "entry-title"}).get_text()
                alamat = card.find('a').get('href')
                bulan_tahun = str(tgl_post[0]+' '+tgl_post[-1])
                URL1 = alamat
                print ("URL 2 ->",URL1)
                time.sleep(5)
                content1 = requests.get(URL1)
                # time.sleep(4)
                soup1 = BeautifulSoup(content1.text, 'html.parser')
                cards1  = soup1.find('span',{ "class" : "entry-date"}).get_text()
                print(cards1[3:].split())
                # if tgl_post[1][0] == '0':
                #     tgl_post[1] = tgl_post[1][1:]
                # else:
                #     tgl_post[1] = tgl_post[1]
                if cards1[3:].split()[1] >= tgl_post[1]:
                    if cards1[3:].split()[1] == "31,":
                        break
                    if (cards1[3:].split() == tgl_post):
                        try:
                            posisi = soup1.find('div',{"class":"entry-content"})
                            h_all = posisi.find_all(True)
                            if "Jika dokumen dibawah" in posisi.get_text() :
                                alamat_error.append(URL1)
                                print ("ini ",judull)
                                pass
                            else:
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
                                atas_text = [li for li in tagss[0:batas_hr[0]] if li != '\n']
                                profil_prusahaan = [li.text for li in tagss[0:batas_hr[0]] if li != '\n']
                                
                                tags_html += ' '.join(str(i) for i in atas_text)
                                tags_html +='''<p> Untuk beberapa orang, dalam mencari pekerjaan adalah sesuatu hal yang cukup sulit. kalaupun mendapatkan pekerjaan itu mudah, belum tentu itu sesuai dengan apa yang kita inginkan. Yang terpenting sekarang adalah ikhtiar, Semangat, dan berusaha. Sesulit apapun dalam mencari kerja, kita tetap yakin kita masih punya Allah SWT yang maha kaya dan tetap pantang menyerah.</p>
                                            <p> Kegagalan bukan bearti Anda berakhir dalam menjalani kehidupan, Manakala Anda Masih diberikan kenikmatan hidup sembari terus mencoba dan belajar dalam mengembangkan bisnis. Orang-orang mungkin menganggap anda telah gagal. Namun jika anda masih tetap terus berjuang mencoba dan menikmati hidup, maka anda belum berada pada kegagalan. Durasi Hidup Anda Akan Terasa Singkat Ketika Rasa Dendam Masih Memenuhi Kepala Anda. Jangan biarkan isi kepala dan hari-hari anda dipenuhi rasa dendam, karena itu akan membuat hidup anda penuh kegelapan dan takkan memiliki makna. Ujung -ujungnya adalah mempersingkat hidup anda. Yang Berani Mendengar adalah Mereka yang Memiliki Sejuta Angan-angan Belaka. Yang Berani Melihat adalah Mereka yang Memiliki Sejuta Impian Belaka. Dan Yang Berani Mencoba adalah Mereka yang Akan Memiliki Angan-angan dan Impian yang Nyata.</p>
                                            '''

                                alamats.append(URL1)
                                print (tgl_post)
                                judull.append(judul)

                                judul = judul.replace("Lowongan Kerja ","")
                                judul = judul.replace("/n","")
                                judul = judul.replace("/"," ")
                                judul = judul.replace(".","")
                                gambar = card.find('img').attrs['src']
                                _download_gambar.maine(gambar,str('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg'))
                                daftar_perusahan_hari_ini.append(judul)
                                gambar_path.append('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
                                
                                masuk =  _parse_content.prasyaratan(posisi,URL1)
                                print (judul)

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
                            gambar_path.remove('E:/Belajar/www.disnakerja.com/images/'+judul+'.jpg')
                            daftar_perusahan_hari_ini.remove(judul)
                            alamats.remove(URL1)
                            tgl_now.remove(tgl)
                            pass
                    else:
                        pass
                else:
                    break
                
        except Exception as e:
            print ("error",judul)
            print ("errornya: ",e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            alamat_error.append(URL1)

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
    df_er.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/data_alamat_error.csv'%tgl)
    df.to_csv('E:/Belajar/www.disnakerja.com/hasil/%s/data_namapekerjaan1.csv'%tgl)

tgl = "February 11, 2021"
tgll = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "w", encoding='utf-8-sig')
tgll.write(tgl)
tgll.close()
tgl_post = tgl.split()
maine(tgl)

