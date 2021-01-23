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


def urai_disnaker(posisi):
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
        for tag1 in posisi.find_all(True)[batas_akhir[-1]:-2]:
            if tag1.name == 'p':
                tag_a_link.append(tag1.get_text().replace("\n",", "))
                for i in tag1.findAll('a'):
                    tty = str(i.get("href"))
                    if "disnakerja.com" in tty:
                        pass
                    else:
                        tag_a_link.append(tty)
            if tag1.text == "" or tag1.text == "|||":
                continue
            if "Apply" in tag1.text or "\xa0" in tag1.text: 
                continue 
        Ket = tag_a_link

        # Artikel
        artikels = ''
        for y in posisi:
            if y.name =='div' or y.name =='script'or y.name =='ins':
                pass
            else:
                artikels += str(y)
    else:
        pass
    return Posisi, P_code_fix,Deskripsi_fix,Ket,artikels


URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-putra-perkasa-abadi-ppa-2/"

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
DATA_WEB = urai_disnaker(posisi)
print ("posisi = ", DATA_WEB[0])
print ("Persyaratan = ", DATA_WEB[2])
print ("Persyaratan = ", len(DATA_WEB[2][0]))
print ("Deskripsi = ", DATA_WEB[1])
print ("Deskripsi = ", len(DATA_WEB[1][0]))
print ("keterangan = ", DATA_WEB[3])
# batas_h1= [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'h1']
# print(batas_h1)
# batas_h4 = [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'h4']
# batas_hr = [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'hr']

# atas_text = [li.text.replace("\xa0"," ") for li in posisi.find_all(True)[0:batas_h4[0]] if li.text != "" and li.text != "\n\n" and li.text != "\n\n\n"]
# tengah_text =  [li.text for li in posisi.find_all(True)[batas_h4[0]:batas_hr[-1]] if li.text != "" and li.text != "\n\n" and li.text != "\n\n\n"]
# bawah_text = [li.text for li in posisi.find_all(True)[batas_hr[-1]:-2] if li.text != "" and li.text != "\n\n" and li.text != "\n\n\n" and li.text != "\n\n\n\n" and li.text !="\n\n\n\n " ]
# print (atas_text)

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import textwrap
from google_trans_new import google_translator

def remove_values_from_list(the_list, val):
    for i in range(the_list.count(val)):
        the_list.remove(val)
    return the_list
def artikel(posisi,parafrase1,parafrase2,parafrase3):
    def _potong(ele):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('https://aiarticlespinner.co/paraphrasing-tool')

        translator = google_translator()
        deteksi = translator.detect(ele)
        print (deteksi)
        if deteksi[0] == 'en':
            pass
        else:
            print (ele)
            ro = 0
            translations_en_list = []
            translations_en = translator.translate(ele,lang_src='id',lang_tgt='en')
            translations_en_list.append(translations_en)
            print (translations_en_list)
            time.sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[3]/div[1]/div[3]/ul/li[4]/input').click()
            time.sleep(2)
            kalimat = []
            for uo in translations_en_list:
                inputs = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[3]/div[1]/div[2]/textarea')
                inputs.send_keys(uo)
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[3]/div[3]/div/button').click()
                time.sleep(30)
                kalimatnya = driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[3]/div[1]/div[5]/div[1]').text
                kalimat.append(kalimatnya)
                driver.find_element_by_xpath('/html/body/div[1]/section[1]/div/div[3]/div[1]/div[2]/textarea').clear()
            translations_id_list = []
            for you in kalimat:
                translations_id = translator.translate(you,lang_src='en',lang_tgt='id')
                translations_id_list.append(translations_id)
            print (translations_id_list)
            '[``, `Production Operator`,` Job description`, [`Check the machine check sheet before starting work`,` CNC machine operation / lathe / machining`], `Qualification`, [` Understanding the processing process`, ` CNC `,` shelf`, `production process`,` kanban`, `pendidikan minimal D3 jurusan permesinan mobil / 1 tahun pengalaman profesional`],` terms`, (`akta kelahiran`,` CV (Curriculum Vitae) ` , `FC E-KTP Karawang`,` FC Ijazah / SKHUN`, `FC Pakelaring CNC (Pemesinan)`, `Foto 4 × 6`,` Salinan KIR Dokter`, `Kartu Keluarga`,` SIM A / C`, `SKCK`,` Surat Keterangan Kehamilan AS (Khusus Wanita) `,` Surat Keterangan Belum Menikah di Kota`, `Rapor (Nilai PBB)`]] '
        return (translations_id_list[0].split(';'))

    tag_atas = []
    r = 0
    for i,y in enumerate(posisi): 
        if y.name != 'p' or y.name !='ol' or y.name !='ul':
            pass
        else:
            tag_atas.append(y)
        r += 1
    tagss = tag_atas
    print ("uni",tagss)
    batas_h1= [0]
    print("h1",batas_h1)
    batas_hr = [o for o,u in enumerate(posisi.find_all(True)) if u.name == 'hr']
    print("hr",batas_hr)
    print("hr",batas_hr)
    batas_h4 = [i for i,li in enumerate(tagss) if li.name == 'h4' or li.name == 'hr']
    print("h4",batas_h4)
    
    def spliting(tengah_text,parafrase):
        tengah_text_final = []
        tengah_tag_final = []
        for you in tengah_text:
            lii = []
            if you.name == 'ol' or you.name == 'ul':
                tengah_text_final.append(you.text.replace('\n',',').split(','))
                for iu in you:
                    lii.append(iu)
                tengah_tag_final.append(lii)
            else:
                tengah_text_final.append(you.text)
                tengah_tag_final.append(you)
        print (len(tengah_text_final))
        print (len(tengah_tag_final))
        
        e = 0
        for iu in range(len(tengah_text_final)):
            # remove_values_from_list(tengah_tag_final[iu], '\n')
            if type(tengah_text_final[iu]) == list:
                tengah_text_final[iu] = remove_values_from_list(tengah_text_final[iu], '')
                # e += 1
            if type(tengah_tag_final[iu]) == list:
                tengah_tag_final[iu] = remove_values_from_list(tengah_tag_final[iu], '\n')
            e += 1
        text_final = '; '.join([str(elem) for elem in tengah_text_final])
        print (text_final)

        if parafrase == True:
            tengah_text_final = (_potong(text_final))
        else:
            tengah_text_final = tengah_text_final
        # tengah_text_final = text_final.split('| ')
        print (tengah_text_final)
        print (tengah_tag_final)
        return tengah_text_final,tengah_tag_final

    def replaceing(tengah_text,parafrase):
        datas = spliting(tengah_text,parafrase)
        tag_ = datas[1]
        textss = datas[0]
        for x in range(len(tag_)):
            if type(tag_[x]) == list:
                for y in range(len(tag_[x])):
                    tag_[x][y].string = tag_[x][y].text.replace(tag_[x][y].text,textss[x][y])
            else:
                tag_[x].string = tag_[x].text.replace(tag_[x].text,textss[x])
        print (tag_)
        return ' '.join(str(i) for i in tag_)

    tags_html = " "
    tags_html +='''<p> Untuk beberapa orang, dalam mencari pekerjaan adalah sesuatu hal yang cukup sulit. kalaupun mendapatkan pekerjaan itu mudah, belum tentu itu sesuai dengan apa yang kita inginkan. Yang terpenting sekarang adalah ikhtiar, Semangat, dan berusaha. Sesulit apapun dalam mencari kerja, kita tetap yakin kita masih punya Allah SWT yang maha kaya dan tetap pantang menyerah.</p>
                   <p> Kegagalan bukan bearti Anda berakhir dalam menjalani kehidupan, Manakala Anda Masih diberikan kenikmatan hidup sembari terus mencoba dan belajar dalam mengembangkan bisnis. Orang-orang mungkin menganggap anda telah gagal. Namun jika anda masih tetap terus berjuang mencoba dan menikmati hidup, maka anda belum berada pada kegagalan. Durasi Hidup Anda Akan Terasa Singkat Ketika Rasa Dendam Masih Memenuhi Kepala Anda. Jangan biarkan isi kepala dan hari-hari anda dipenuhi rasa dendam, karena itu akan membuat hidup anda penuh kegelapan dan takkan memiliki makna. Ujung -ujungnya adalah mempersingkat hidup anda. Yang Berani Mendengar adalah Mereka yang Memiliki Sejuta Angan-angan Belaka. Yang Berani Melihat adalah Mereka yang Memiliki Sejuta Impian Belaka. Dan Yang Berani Mencoba adalah Mereka yang Akan Memiliki Angan-angan dan Impian yang Nyata.</p>
                '''
    atas_text = [r for r in posisi.find_all(True)[0:batas_hr[0]] if r.name == "p" or r.name == "span" ]
    print ("atas_text ",atas_text)
    tags_html += replaceing(atas_text,parafrase1)
    
    # tengah_text = [li for li in tagss[batas_h4[0]:batas_hr[-1]] if li != '\n']
    # print ("tengah_textt ",tengah_text)
    
    # tags_html += replaceing(tengah_text,parafrase2)

    # bawah_text = [li for li in tagss[batas_h4[-1]:-2] if li != '\n']
    # print ("bawah_text ",bawah_text)
    # tags_html += replaceing(bawah_text,parafrase3)
    
    print (tags_html)
    return (tags_html)

artikel(posisi,False,False,False)
print (posisi.values)

batas_h1= [0]
print("h1",batas_h1)
batas_hr = [o for o,u in enumerate(posisi.find_all(True)) if u.name == 'hr']
print("hr",batas_hr)

pp = [r for r in posisi.find_all(True)[0:batas_hr[0]] if r.name == "p" or r.name == "span" ]
print (pp)