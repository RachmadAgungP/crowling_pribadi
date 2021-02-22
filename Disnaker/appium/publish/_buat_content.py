import pandas as pd
import _parafrase
import ast
import re
import os
from datetime import date
# >>> ast.literal_eval('["A","B" ,"C" ," D"]')
def htmll(tgl,index,dataw,on_off_parafrase,content_FB):
    artikels_pendahuluan = " "
    if content_FB == True:
        text_artikel = ""
    # dataw = pd.read("hasil\%s\data_namapekerjaan1.csv"%tgl)
    nama_p = dataw["Nama"][index]
    print (nama_p)
    Ket = ast.literal_eval(dataw["Keterangan"][index])
    header = dataw["header"][index]
    link = dataw["Alamat"][index]
    Posisi = ast.literal_eval(dataw["Posisi"][index])
    P_code_fix = ast.literal_eval(dataw["kode_kual"][index])
    Deskripsi_fix = ast.literal_eval(dataw["Kualifikasi"][index])
    if content_FB == True:
        text_artikel += "Lowongan kerja " + nama_p +'\n'
    # ketera = ast.literal_eval(ket)
    artikels_pendahuluan += _parafrase.pendahuluan(header,on_off_parafrase)
    # artikels_pendahuluan += "<p>"+header+"</p>"
    artikels_pendahuluan += "<hr>"
    for ui in range(len(Posisi)):
        if content_FB == True:
            st_text = '\t'+str(Posisi[ui])+'\n'
            text_artikel += st_text.expandtabs(2)
        artikels_pendahuluan += "<h5>" + str(Posisi[ui])+"</h5>"
        for oi in range(len(P_code_fix[ui])):
            if content_FB == True:
                if oi <= 3:
                    st_text = '\t'+str(P_code_fix[ui][oi])+'\n'
                    text_artikel += st_text.expandtabs(4)

            artikels_pendahuluan += "<p>" + str(P_code_fix[ui][oi])+"</p>"
            artikels_pendahuluan += "<ol>" 
            for ip in range(len(Deskripsi_fix[ui][oi])):
                if ip == len(Deskripsi_fix[ui][oi])-1:
                    artikels_pendahuluan += "</ol>"
                elif Deskripsi_fix[ui][oi][ip] == "":
                    pass
                else:
                    if content_FB == True:
                        if ip <= 3:
                            st_text = '\t'+'- '+str(Deskripsi_fix[ui][oi][ip])+'\n'
                            text_artikel += st_text.expandtabs(4)

                    artikels_pendahuluan += "<li>"+ str(Deskripsi_fix[ui][oi][ip])+"</li>"
    regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regex_url = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    artikels_pendahuluan += "<hr>"
    for op in Ket:
        if (re.search(regex_url,op)):
            artikels_pendahuluan += '''<div class="wp-block-button;"> <a class="wp-block-button__link has-text-color has-background" style="border-radius:2px;background-color:#1d345b;color:#fffffa;" href="%s" >Apply</a></div>"'''%op
            # artikels_pendahuluan += '''<p style="text-align: center;"> <a class="button" style="vertical-align: middle;" href="%s" target="_blank" rel="noopener noreferrer"><button>Apply </button></a> </p>"'''%op
        elif (re.search(regex_email,op)):  
            artikels_pendahuluan += "<p>%s</a></p>"%op
        elif op == "Apply " or op == " Apply " or op == "Apply":
            pass
        else:
            artikels_pendahuluan += "<p>"+op+"</p>"
    st_text = '\t'+'- ...\n'
    text_artikel += st_text.expandtabs(4)
    tgl_a = re.sub(r"\D", " ", tgl)
    tgl_b = tgl_a.split()
    tgl_c = int(tgl_b[0])
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    bulan = month.index(tgl.split()[0])+1
    tahun = tgl.split()[-1]

    tgll = date(int(tahun), bulan,tgl_c).isoformat().replace('-','/')
    nama_p = dataw["Nama"][index]
    text_artikel += "-> Informasi lebih lanjut di https://foloker.com/%s/%s/"%(tgll,"lowongan-kerja-"+nama_p.replace(" ","-"))

    # print(artikels_pendahuluan)
    nama_p = dataw["Nama"][index]
    newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/html'.format(tgl) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    htmml = open("E:/Belajar/www.disnakerja.com/hasil/%s/html/%s.html"%(tgl,nama_p), "w", encoding='utf-8-sig')
    htmml.write(artikels_pendahuluan.replace("/cdn-cgi/l/email-protection",""))
    htmml.close()

    newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/text'.format(tgl) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    texts = open("E:/Belajar/www.disnakerja.com/hasil/%s/text/%s.txt"%(tgl,nama_p), "w", encoding='utf-8-sig')
    texts.write(text_artikel.replace("/cdn-cgi/l/email-protection",""))
    texts.close()
    # print (text_artikel)
    return (artikels_pendahuluan,text_artikel)

# import _tgl_
# from datetime import date
# tgl = _tgl_.baca_file()

# dataw = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl)
# list_data = _tgl_.data_proses(tgl)
# print (list_data)
# list_text_FB = " "
# for y in list_data:
#     list_text_FB += htmll(tgl,y,dataw,False,True)[1]+"\n\n"
# print (list_text_FB)
# nama_p = dataw["Nama"][index]


