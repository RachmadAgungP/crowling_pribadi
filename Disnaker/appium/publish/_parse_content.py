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
import _parafrase
def grouping(sequence):
    sequence = sequence
    datas = []
    for y in sequence:
        ti = []
        # print (set(y))
        for u in y:
            if u == '':
                pass
            else:
                ti.append(u)
        datas.append(ti)
    def grouper(sequence):
        result = []  # will hold (members, group) tuples

        for item in sequence:
            for members, group in result:
                if members.intersection(item):  # overlap
                    members.update(item)
                    group.append(item)
                    break
            else:  # no group found, add new
                result.append((set(item), [item]))

        return [group for members, group in result]

    # for group in grouper(data):
        # print (grouper(data))
    asw = grouper(datas)
    po = []
    for t in asw:
        wew = []
        for u in t:
            for y in u:
                if y not in wew:
                    wew.append(y)
        po.append(wew)
    return (po)
datas = ["General Requirements","Persyaratan Umum","Ketentuan","Berkas Lamaran","Tahapan seleksi"]
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
    batas_posisi= [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'h5' or (li.name == 'p' and li.text in datas)]
    # print (batas_posisi)
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
        Posisi = [li.text for li in posisi.find_all(True) if li.name == 'h5' ]
        
        # Kode
        P_code_fix = []
        Deskripsi_fix = []
        for i in range(len(batas_posisi)):
            if i == len(batas_posisi)-1:
                batass = posisi.find_all(True,recursive=True)[batas_posisi[-1]:batas_akhir[-1]]
                batassli = posisi.find_all(True,recursive=False)
                
                print (batas_posisi[i],"-->",batas_akhir[-1])
            else:
                batass = posisi.find_all(True,recursive=True)[batas_posisi[i]:batas_posisi[i+1]]
                batassli = posisi.find_all(True,recursive=False)
                
                print (batas_posisi[i],"-->",batas_posisi[i+1])
                
            P_code = [li.text for li in batass if li.name == 'p' and len(str(li.text)) <= 30]
            Deskripsi = [li.text.split('\n') for li in batass if (li.name == 'ul' or li.name == 'ol') or li.previous_sibling.name == "p"]
            tag_deskip = [li.text.split('\n') for li in batassli if (li.name == 'ul' or li.name == 'ol')]
            P_code_fix.append(P_code)
            # print (P_code_fix)
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
            else:
                pass
        Ket = remove_values_from_list(tag_a_link,'')
        Ket = remove_values_from_list(Ket,', , , ')
        Ket = list(dict.fromkeys(Ket))
        # Artikel
        artikels_pendahuluan += "_"
    else:
        pass
    des = [] 
    # print ("->",Deskripsi_fix)
    io = 0
    for uu in range(len(P_code_fix)):
        # banding = set(Deskripsi_fix[uu][0]) & set(Deskripsi_fix[uu][1])
        for iu in P_code_fix[uu]:
            if iu in datas:
                Posisi.append("Tambahan Info")       
                print (len(Deskripsi_fix[0]))
    e = 0
    # [['ul'], ['ol']]
    print (tag_deskip)
    po = []
    for y in Deskripsi_fix:
        po.append(grouping(y))
        if len(y) != len(P_code_fix[e]):
            print ("yes")
            y.pop(-1)
        else:
            continue
        e+=1

    # print (po)
    wew = 0
    for oi in po:
        if len(oi) != len(P_code_fix[wew]):
            print ("yes")
            P_code_fix[wew].pop(-1)
        else:
            continue
        wew += 1
        
    return Posisi, P_code_fix,po,Ket,artikels_pendahuluan


# # F URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-honda-prospect-motor-2/"
# # F URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-sawit-sumbermas-sarana-tbk/"
# # F URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-astra-international-tbk-astra-ud-trucks/"
# # F URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-putra-perkasa-abadi-ppa-2/"
# # F URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-yamaha-music-manufacturing-asia/"
# # N URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-paiton-operation-maintenance-indonesia/"
# # F URL1 = "https://www.disnakerja.com/job/lowogan-kerja-pt-dharma-satya-nusantara-tbk-dsn-group/"
# # F URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-djabesmen-dbc-co/"
# print ("URL 2 ->",URL1)
# time.sleep(1)
# content1 = requests.get(URL1)
# time.sleep(4)
# soup1 = BeautifulSoup(content1.text, 'html.parser')
# posisi = soup1.find('div',{"class":"entry-content"})
# data = prasyaratan(posisi)
# print ("posisi =", data[0])
# print ("posisi =", len(data[0]))
# print ("code =", data[1])
# print ("code =", len(data[1]))
# print ("desc =", data[2])
# print ("desc =", len(data[2]))
# print ("ket =", data[3])