import pandas as pd
import _parafrase
import ast
import re
import os
# >>> ast.literal_eval('["A","B" ,"C" ," D"]')
def htmll(tgl,index,dataw):
    artikels_pendahuluan = " "
    # dataw = pd.read("hasil\%s\data_namapekerjaan1.csv"%tgl)
    nama_p = dataw["Nama"][index]
    Ket = ast.literal_eval(dataw["Keterangan"][index])
    header = dataw["header"][index]
    Posisi = ast.literal_eval(dataw["Posisi"][index])
    P_code_fix = ast.literal_eval(dataw["kode_kual"][index])
    Deskripsi_fix = ast.literal_eval(dataw["Kualifikasi"][index])

    # ketera = ast.literal_eval(ket)
    artikels_pendahuluan += _parafrase.pendahuluan(header)
    artikels_pendahuluan += "<hr>"
    for ui in range(len(Posisi)):
        artikels_pendahuluan += "<h5>" + str(Posisi[ui])+"</h5>"
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
    artikels_pendahuluan += "<hr>"
    for op in Ket:
        if (re.search(regex_url,op)):
            artikels_pendahuluan += '''<p style="text-align: center;"> <a class="button" style="vertical-align: middle;" href="%s" target="_blank" rel="noopener noreferrer"><button>Apply </button></a> </p>"'''%op
        elif (re.search(regex_email,op)):  
            artikels_pendahuluan += "<p><a href="+"mailto:%s"+">Send email</a></p>"%op
        elif op == "Apply " or op == " Apply " or op == "Apply":
            pass
        else:
            artikels_pendahuluan += "<p>"+op+"</p>"
    print(artikels_pendahuluan)
    nama_p = dataw["Nama"][index]
    newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/html'.format(tgl) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    htmml = open("E:/Belajar/www.disnakerja.com/hasil/%s/html/%s.html"%(tgl,nama_p), "w", encoding='utf-8-sig')
    htmml.write(artikels_pendahuluan)
    htmml.close()

    return (artikels_pendahuluan)

import _tgl_
tgl = _tgl_.baca_file()
dataw = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl)
list_data = _tgl_.data_proses(tgl)
print (list_data)
for y in list_data:
    htmll(tgl,y,dataw)

