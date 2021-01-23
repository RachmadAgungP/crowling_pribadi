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

def prasyaratan(posisi):
    
    batas_posisi= [i for i,li in enumerate(posisi.find_all(True)) if (li.name == 'h3' or li.name == 'h2' or li.name == 'h4') and li.next_element.name == 'strong']
    
    batas_akhir = [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'hr']
    print (batas_akhir)
    # # Posisi
    Posisi = [li.text for li in posisi.find_all(True) if (li.name == 'h3' or li.name == 'h2' or li.name == 'h4') and li.next_element.name == 'strong']
    # print (Posisi)
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
            if li.name == 'p' and li.next_element.name == 'strong':
                if '•' in li.text:
                    P_code.append(li.text[:li.text.index(":")-1])
                else:
                    P_code.append(li.text)
        Deskripsi = [li.text.split('•')[1:] for li in batass if li.name == 'p' and "•" in li.text]
        P_code_fix.append(P_code)
        Deskripsi_fix.append(Deskripsi)
    print (P_code_fix)
    print (Deskripsi_fix)
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
        if tag1.name == 'p':
            tag_a_link.append(tag1.text.replace("\n",", "))
            for i in tag1.findAll('a'):
                tty = str(i.get("href"))
                if "goletskerja.com" in tty:
                    pass
                else:
                    tag_a_link.append(tty)
        
    Ket = tag_a_link
    print (Ket)
    # # Artikel
    # artikels = ''
    # for y in posisi:
    #     if y.name =='div' or y.name =='script'or y.name =='ins':
    #         pass
    #     else:
    #         artikels += str(y)
    # if '<button> Apply </button><button> Apply </button>' in artikels:
    #     print ("adasdadas")
    #     artikels = artikels.replace('<button> Apply </button><button> Apply </button>','')
    # elif  '<button> Apply </button></a><button> Apply </button>' in artikels:
    #     artikels = artikels.replace('<button> Apply </button></a><button> Apply </button>','</a>')


    # return Posisi, P_code_fix,Deskripsi_fix,Ket,artikels

# now = datetime.datetime.now()
# tgl = now.strftime("%B %d, %Y")
# tgl = "Desember 23, 2020"
# tgl_post = tgl.split()

# URL = 'https://goletskerja.com/'
# # URL = 'https://%s/page/%s/'%(web2,i)
# print ("URL 1 ->",URL)
# time.sleep(1)
# content = requests.get(URL)
# time.sleep(4)
# soup = BeautifulSoup(content.text, 'html.parser')

# conten = soup.find('div',{"class":"td_block_inner"})
# waktu = soup.findAll('time',{"class":"entry-date updated td-module-date"})
# # print (conten)
# nama_perusahaan = [i.previous_element.previous_element.previous_element.get_text() for i in conten.find_all(True) if i.name == "div" and i.next_element.next_element.next_element.name == "time" and i.next_element.next_element.next_element.get_text() == tgl]
# href_link = [i.previous_element.previous_element.previous_element.get("href") for i in conten.find_all(True) if i.name == "div" and i.next_element.next_element.next_element.name == "time" and i.next_element.next_element.next_element.get_text() == tgl]
# # for y in href_link:

URL = "https://goletskerja.com/lowongan-kerja-pt-pos-indonesia-persero-4/"
print ("URL 1 ->",URL)
time.sleep(1)
content = requests.get(URL)
time.sleep(4)
soup = BeautifulSoup(content.text, 'html.parser')
posisi = soup.find('div',{"class":"td-post-content"})

prasyaratan(posisi)


# selectt = [tagg for tagg in conten.find_all(True) if tagg.name == 'h3']
# print (selectt)
# for i in conten:
#     if tgl in i:
#         print (waktu)