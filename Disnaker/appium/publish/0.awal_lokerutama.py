
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
    batas_posisi= [i for i,li in enumerate(posisi.find_all(True)) if (li.name == 'h3') and li.next_element.name == 'strong']
    
    batas_akhir = [i for i,li in enumerate(posisi.find_all(True))]
    print (batas_akhir)
    # # Posisi
    Posisi = [li.text for li in posisi.find_all(True) if (li.name == 'h3') and li.next_element.name == 'strong' and li.text != 'Sekedar Informasi' and li.text != 'Cara Mendaftar']
    
    # Kode
    P_code_fix = []
    for i in range(len(Posisi)):
        if i == len(batas_posisi)-1:
            batass = posisi.find_all(True)[batas_posisi[-1]:batas_akhir[-1]]
            print (batas_posisi[i],"-->",batas_akhir[-1])
        else:
            batass = posisi.find_all(True)[batas_posisi[i]:batas_posisi[i+1]]
            print (batas_posisi[i],"-->",batas_posisi[i+1])
        P_code = []
        for li in batass:
            if li.name == 'h3' and len(li.text)<30 and li.text != 'Sekedar Informasi' and li.text != 'Cara Mendaftar':
                P_code.append(li.text)
        P_code_fix.append(P_code)
        Deskripsi = []
        
        Deskripsi_fix = []
        # Deskripsi = [[rey.get_text() for rey in y if rey != '\n'] for y in posisi.find_all(True) if y.name == 'ol' or y.name == 'ul' and y.previous_element.previous_element.text == "Sekedar Informasi" or y.previous_element.previous_element.text == "Cara Mendaftar"]
        for y in posisi.find_all(True):
            if y.name == 'ol' or y.name == 'ul':
                try:
                    # if y.previous_sibling.previous_sibling.text == None:
                    #     pass
                    # else:
                    print (y.text)
                except:
                    pass
                    # print (y)
        # print ("ini_coba",rep)
        Deskripsi_fix.append(Deskripsi)
    
    # for ini in range (len(P_code_fix)):
    #     if len(P_code_fix[ini]) > len(Deskripsi_fix[ini]):
    #         Deskripsi_fix[ini].append([])
    #     if len(P_code_fix[ini]) < len(Deskripsi_fix[ini]):
    #         P_code_fix[ini].append(".")
    #     else:
    #         pass

    # # Keterangan 
    # tag_a_link = []
    # for tag1 in posisi.find_all(True)[batas_akhir[-1]:]:
    #     if tag1.name == 'div':
    #         for i in tag1.findAll('a'):
    #             tty = str(i.get("href"))
    #             if "goletskerja.com" in tty:
    #                 pass
    #             if "api.whatsapp" in tty:
    #                 pass
    #             else:
    #                 tag_a_link.append(tty)
    #     elif tag1.name == 'p':
    #         if tag1.text is None:
    #             print ("yes")
    #             pass
    #         elif "Baca Juga :" in tag1.text or "Join Channel Telegram" in tag1.text or "GOLETSKERJA" in tag1.text or "Goletskerja" in tag1.text:
    #             pass
    #         else:
    #             tag_a_link.append(tag1.text.replace("\n",", "))
    #     elif tag1.name == 'li':
    #         tag_a_link.append(tag1.text)

    # Ket = tag_a_link
    # if len(Posisi) == 0 or len(P_code)== 0 or len(Deskripsi_fix)== 0:
    #     pass
    # else:
    print (Posisi)
    print (P_code_fix)
    print (Deskripsi_fix)
        # print (unique(Ket))
        # print (batas_p)
    return Posisi, P_code_fix,Deskripsi_fix,unique(Ket),batas_p
import _tgl_
tgl = _tgl_.baca_file()
# URL2 = "https://lokerutama.com/"
# time.sleep(1)
# content1 = requests.get(URL2)
# soup1 = BeautifulSoup(content1.text, 'html.parser')
# contents = soup1.find('div',{"class":"content-inner rb-row"})
# tgll = soup1.find('abbr',{"class":"date published"})
# month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
# month_id = ["Januari","Februari","Maret","April","Mai","Juni","Juli","Agustus","September","Oktober","November","Desember"]
# io = [i.findPrevious("a").get("href") for i in contents.find_all(True) if i.text.replace(i.text.split(' ')[0],month[month.index(_tgl_.baca_file().split(' ')[0])]) == _tgl_.baca_file()]
# URL1s = list(set(io))
# print (URL1s[0])
# time.sleep(1)
# content = requests.get(URL1s[0])
# time.sleep(4)
soup = BeautifulSoup(open('C:/Users/Lenovo/Documents/Lowongan Kerja Shopee Indonesia Terbaru Februari 2021.html'), 'html.parser')
posisi = soup.find('div',{"class":"entry-content clearfix"})
prasyaratan(posisi)
print (soup)
