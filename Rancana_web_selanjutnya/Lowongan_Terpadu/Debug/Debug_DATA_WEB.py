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

# URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-cakrawala-andalas-televisi-antv-2/"
# URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-kino-food-indonesia-3/"
# URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-pt-kimia-farma-apotek-kfa/' #sub menu
# URL1 = 'https://www.disnakerja.com/job/lowongan-kerja-wilmar-group-2/'
# URL1 ='https://www.disnakerja.com/job/lowongan-kerja-pt-pan-brothers-tbk/'
# filey = open('Lowongan_Terpadu\Debug\Lowongan Kerja BUMN PT PP (Persero) Tbk Terbaru Desember 2020.html').read()
# filey = open('Lowongan_Terpadu\Debug\Lowongan Kerja BUMN PT PP (Persero) Tbk Terbaru Desember 2020.html').read()
URL1 = 'https://www.lowonganterpadu.com/2020/12/lowongan-kerja-terbaru-bank-mandiri.html' #Posisi sulit 
# https://www.lowonganterpadu.com/2020/12/lowongan-kerja-terbaru-pt-mandiri-utama.html
print ("URL 2 ->",URL1)
time.sleep(1)
content1 = requests.get(URL1)
time.sleep(4)
soup1 = BeautifulSoup(content1.text, 'html.parser')
# soup1 = BeautifulSoup(filey, 'html.parser')
tgl = soup1.find('abbr',{"class":"published updated"})
print (tgl.text)
posisi = soup1.find('div',{"id":"body-post-it"})

def urai_lowongan_terpadu(posisi):
    Posisi = [li.text for li in posisi.find_all(True) if li.name == 'p' and len(li.text)>5 and (li.text[0].isnumeric() == True or li.text.isupper())]
    batas_posisi= [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'p' and len(li.text)>5 and (li.text[0].isnumeric() == True or li.text.isupper())]
    print (batas_posisi)
    batas_akhir = [i for i,li in enumerate(posisi.find_all(True)) if li.name == 'p' and ("Jika anda tertarik dan memenuhi" in li.text or "Lain" in li.text) and (li.next_sibling.name == "p")]
    P_code_fix = []
    
    Deskripsi_fix = []
    for i in range(len(batas_posisi)-1):
        
        # print (batass)
        if i == len(batas_posisi):
            batass = posisi.find_all(True)[batas_posisi[-1]:batas_akhir[-1]]
        else:
            batass = posisi.find_all(True)[batas_posisi[i]:batas_posisi[i+1]]
        P_code = [li.text for li in batass if li.name == 'p' and li.next_sibling.name == 'p' and (li.next_sibling.next_sibling.name == 'ul' or li.next_sibling.next_sibling.name == 'ol')]
        Deskripsi = [li.text for li in batass if (li.name == 'ul' or li.name == 'ol') and li.previous_sibling.name == 'p' and (len(li.previous_sibling.previous_sibling.text) != 0 )]
        
        P_code_fix.append(P_code)
        Deskripsi_fix.append(Deskripsi)
    
    Keterangan = [w.text for w in posisi.find_all(True)[batas_akhir[0]:-2]]
    
    return Posisi, Deskripsi_fix, P_code_fix, Keterangan

lt = urai_lowongan_terpadu(posisi)
print ("posisi = ", lt[0])
print ("Persyaratan = ", lt[2])
print ("Persyaratan = ", len(lt[2]))
print ("Deskripsi = ", lt[1])
print ("Deskripsi = ", len(lt[1]))
print ("keterangan = ", lt[3])












# def prasyaratan(posisi):
#     HTML_tag_names = []
#     HTML_tag_name = []
#     index_h5 = []
#     index_hr = []
#     index_div = []
#     h = 0
#     for tag in posisi.find_all(True):
#         if tag.name == 'h5':
#             index_h5.append(h) 
#         if tag.name == 'hr':
#             index_hr.append(h)
#         if tag.name == 'div':
#             index_div.append(h)
#         h+=1
#     # print ("index_hr ",index_hr)
#     # print("ininini",posisi.find_all(True)[49])
#     DATA_Posisi = []
#     DATA_kode = []
#     DATA_kualif = []

#     HTML_children_li =[]

#     # DATA_POSISI = []
#     index_h5.append(index_hr[-1])
#     # print ("index ",index_h5)
#     for u in range(len(index_h5)-1):
#         HTML_tag_name = []
#         children_li_f = []
#         # tag_h5_Posisi = []
#         tag_p_kode = []
#         tag_p_kualif = []

#         ind = index_h5[u]
#         for tagg in posisi.find_all(True)[index_h5[u]:index_h5[u+1]]:
#             if tagg.name == 'h5':
#                 DATA_Posisi.append(tagg.get_text().replace("\n",""))
#             elif tagg.name == 'p':
               
#                 text = ''
#                 if isinstance(tagg, NavigableString):
#                     text += str(tagg).strip()
#                 elif isinstance(tagg, Tag):
#                     if tagg.name != 'br':
#                         text += tagg.text.strip()
#                     else:
#                         text += '\n'
#                 if posisi.find_all(True)[ind+1].name == 'span':
#                     print ("dsd")
#                     pass
#                 else:
#                     # print (text)
#                     result = text.strip().split('\n')
#                     indx = 0
#                     for yss in result:
#                         if indx == 0:
#                             if len(yss) > 26:
#                                 pass
#                             else:
#                                 tag_p_kode.append(yss)
#                         if len(yss) > 26:
#                             if posisi.find_all(True)[ind+1].name == 'br':
#                                 pass
#                             else:
#                                 tag_p_kualif.append([yss])
#                         indx += 1
#                     if posisi.find_all(True)[ind+1].name == 'br':
#                         tag_p_kualif.append(result[1:])
            
#             elif tagg.name == 'ul' or tagg.name == 'ol':
#                 children_li = []
#                 for a in tagg(my_filter): # or soup.find_all(my_filter)
#                     children_li.append(a.text)
#                 children_li_f = children_li

#                 yus = []
#                 for yo in tagg.findAll("li" , recursive=False):
#                     yus.append(yo.text)
#                 tag_p_kualif.append(yus)
                
#                 next_li_element = tagg.find_next_sibling("li")
#                 # # print (tag.next_sibling())
#                 if next_li_element is None:
#                     next_ol_element = tagg.find_next_sibling("ol")
#                     if next_ol_element is None:
#                         pass
#                 # print("op")
                
#                 print (tagg.name)
            

#             HTML_tag_name.append([tagg.name])
#             ind +=1
#         HTML_tag_names.append(HTML_tag_name)
#         HTML_children_li.append(children_li_f)

#         # DATA_Posisi.append(tag_h5_Posisi)
#         DATA_kode.append(tag_p_kode)
#         DATA_kualif.append(tag_p_kualif)

#         if len(DATA_kode[0]) > len(DATA_kualif[0]):
#             for iu in range(len(DATA_kualif[0]),len(DATA_kode[0])):
#                 DATA_kualif[0].append([])
#         else:
#             for iui in range(len(DATA_kode[0]),len(DATA_kualif[0])):
#                 DATA_kode[0].append([])
        
#     for d in range (len(DATA_kualif)):
#         # print (d)
#         print (DATA_kualif[d])
#         print (HTML_children_li[d])
#         if HTML_children_li[d] in DATA_kualif[d]:
#             print ("ada")
#             DATA_kualif[d].remove(HTML_children_li[d])
            
            

#     footer = posisi.find_all(True)[index_hr[-1]:h]
#     HTML_tag_footer = [] #keteranagan
#     tag_a_link = []
#     for tag1 in footer:
#         if tag1.name == 'p':
#             HTML_tag_footer.append(tag1.get_text().replace("\n",", "))
#             for i in tag1.findAll('a'):
#                 tty = str(tag1.text.replace(" Apply "," ")+i.get("href"))
#                 tag_a_link.append(tty)
#         if tag1.text == "" or tag1.text == "|||":
#             continue
#         if "Apply \xa0– " in tag1.text or " Apply " in tag1.text:
#             continue
#     return (DATA_Posisi,DATA_kode,DATA_kualif,tag_a_link,HTML_tag_footer,index_h5,HTML_tag_names)

# DATA_WEB = prasyaratan(posisi)
# DATA_Posisi = DATA_WEB[0]
# DATA_kode = DATA_WEB[1]
# DATA_kualif = DATA_WEB[2]
# DATA_link = DATA_WEB[3]
# DATA_ket = DATA_WEB[4]
# DEBUG_TAG_HTML = DATA_WEB[6]
# print (DATA_kode[0])
# print (DATA_kualif[0])
# print (len(DATA_kualif[0]),"-",len(DATA_kode[0]))
# print(DEBUG_TAG_HTML[0])

# df = pd.read_csv('hasil\December 11, 2020\data_namapekerjaan1.csv')
# print (df['Kualifikasi'][1])
#




# import awal as urai
# URL1 = "https://www.disnakerja.com/job/lowongan-kerja-pt-kao-indonesia/"
# print ("URL 2 ->",URL1)
# time.sleep(1)
# content1 = requests.get(URL1)
# time.sleep(4)
# soup1 = BeautifulSoup(content1.text, 'html.parser')
# cards1  = soup1.find('span',{ "class" : "entry-date"}).get_text()
# posisi = soup1.find('div',{"class":"entry-content"})
# lii  = []
# for tag in posisi.find_all(True):
#     if tag.name == 'ol' or  tag.name == 'ul':
#         for yo in tag.findAll('li'):
#             lii.append(yo.string)

# print (lii)







#lowongankerja 
#lowongan 
#loker
#lokerja
#lowonganbumn 
#lowongancpns
#lowonganpekerjaan 
#kerja
#lokerjawatimur
#lokersumatra
#lokerjawa
#lokermadura
#lokerbali
#lokerkalimantan
#lokersulawesi
#lokermaluku
#lokerpapua
#Karir
#jobstreet
#disnaker
#jobs
#klob
#lokersurabaya
#lokerjakarta
#lokerjogja

#lowongankerja #lowongan #loker #lokerja #lowonganbumn #lowongancpns #lowonganpekerjaan #kerja #lokerjawatimur #lokersumatra #lokerjawa #lokermadura #lokerbali #lokerkalimantan #lokersulawesi #lokermaluku #lokerpapua #Karir #jobstreet #disnaker #jobs #klob #lokersurabaya #lokerjakarta #lokerjogja
# print (len("-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd"))
# a = ["-  zxdsaCorporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd","-  Corporate Legal Officer hljhskjfh dfsf dsfs dffd sfssdfsdfsdfsd dsfsdfsdf fd"]
# len(a)
# import textwrap
# maxi = max(a, key=len)
# mini = min(a, key=len)
# maxx = len(maxi)
# minii = len(mini)
# if len(a) < 10 and len(a) > 9:
#     if maxx <= 63:
#         print ("font besar ", 30)
#     elif maxx >= 63
    


# for i in range (len(a)):
#     if len(a[i]) > 79:
#         v = len(a[i])-79 #sebagai pemotong
#         print (v)
#         print (len(a[i]))
#         uu = textwrap.wrap(a[i],len(a[i])-(v)) #pemotong
#         print (uu)
#         print ("besar font ",28+(len(a[i])-79))

# https://www.disnakerja.com/job/lowongan-kerja-pt-tower-bersama-infrastructure-tbk/
# 8,PT Kelola Mina Laut,['Management Trainee (MT)'],"[[['MT Operating & Production', 'MT Marketing Export', 'MT Domestic Sales', 'MT Finance & Accounting', 'MT Human Resources Development & General Affair', 'MT Quality Assurance (QA)', 'MT R&D (Research & Development)'], ['Minimum S1 / D4 / D3', 'Min GPA 3,00', 'Graduated from reputable university (Accreditation minimum B)', 'Maximum 30 years old', 'Good communication skills in English', 'Major softwares computer skills', 'Ready to work full of challenges and have a strong ambition to get ahead', 'Active in organization and willing to be placed in all areas of operation of KML Food']]]","[[[], 'General Requirements']]",E:/Belajar/HackersFriend-NewsAggregator/images/PT Kelola Mina Laut.jpg,"['If you meet the requirements above and are interested in the position, please send your latest CV and photograph to:', 'HRD Department – PT. Kelola Mina Laut, Jl. KIG Raya Selatan Kav. C-5. (Kawasan Industri Gresik), Gresik 61121- Jawa Timur', 'Or via email with the name of the position as the subject to:', 'arya@kmlseafood.com and hrd@kmlseafood.com', ', , , ']",[],"November 30, 2020"
