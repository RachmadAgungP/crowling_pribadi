import pandas as pd
import ast
import win32com.client as win32
import os
import textwrap
import datetime

adobe_app = win32.GetActiveObject("Illustrator.Application")
adobe_document = adobe_app.ActiveDocument
layer1 = adobe_document.Layers("Layer1")
layer2 = adobe_document.Layers("Layer2")
layer3 = adobe_document.Layers("Layer3")

save_pic(nama,tt)

def layer_sama(nama_layer, layer_ke, isi, ukuran_font, visible):
    var = layer_ke.TextFrames(nama_layer)
    var.TextRange.Contents = str(isi)
    tR = var.textRange
    tR.characterAttributes.size = ukuran_font
    var.hidden = visible
    return (var)

def save_pic(nama,tt):
    # Define the Export JPEG Options.
    jpeg_export_options = win32.Dispatch("Illustrator.ExportOptionsJPEG")

    # Export the document.
    newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/{}'.format(tgl,str(nama)) 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    adobe_document.Export(
        ExportFile=r"E:/Belajar/www.disnakerja.com/hasil/{}/{}/{}".format(
            str(tgl),str(nama),str(tt)
        ),
        ExportFormat=1,
        Options=jpeg_export_options
    )
def listToString(s,skalar,kod,uk):  
    str1 = ""
    tnpa_tnd_bca = ""
    str1_over = ""
    kod = kod
    if kod == []:
        kod = "Pilihan"
        print (kod)
   
    print (kod)
    tampungan = {kod:[]} 
    items = {kod:[]}
    w = 1
    hitung_baris = 0
    ukuran = uk
    if skalar ==  False:
        ukuran = uk
    else:
        ukuran = uk
    for ele in s:  
        if len(ele)>=ukuran:
            kk = textwrap.wrap(ele,ukuran)
            kal = ""
            io = 0 
            for i in kk:
                if io == 0:
                    kal += i
                else:
                    kal +=  os.linesep+ "   " +i 
                io += 1
            str1 += os.linesep+"- "+" "+ kal
            tnpa_tnd_bca += os.linesep+ kal
            tampungan[kod].append(os.linesep+"- "+" "+ kal)
            hitung_baris +=1
        else:
            str1 += os.linesep+"- "+" "+ ele
            tnpa_tnd_bca += os.linesep+ ele
            tampungan[kod].append(os.linesep+"- "+" "+ ele)
            hitung_baris += 1
        # print (str1,"i======")
        w += 1
    # tampungan[kod].append(str1)
    if len(tampungan[kod]) >=10:
        if skalar == True:
            items[kod] = tampungan[kod][10:len(tampungan[kod])]
            tampungan[kod] = tampungan[kod][:10]
            tampungan[kod].append(os.linesep+"- penjelasan ada di bawah ...")
            print (items)
            for i in tampungan[kod]:
                str1_over += i
        else:
            for i in tampungan[kod]:
                str1_over += i 
    else:
        for i in tampungan[kod]:
            str1_over += i    
    print ("kualifikasi-> ",str1_over)

    return str1_over,items,str1,tnpa_tnd_bca

# layer_sama("Nama_Posisi", layer2, posisis[y], 35, False)

# def peletakan(kode,letak_kod_i,deskripsi,letak_des_i,uk_font, len_text, layer_vis):
#     lis_des = textwrap.wrap(deskripsi,len_text)
#     des = " "
#     des = des.join(lis_des)
#     layer2.visible = True
#     if kode == "":
#         visual = layer_vis
#     else:
#         visual = layer_vis
#     layer_sama("kode_Prasaratan "+str(letak_kod_i), layer2, kode,  35, visual)
#     layer_sama("Prasaratnya "+str(letak_des_i), layer2, des, uk_font, visual)

# posisi = ""
# kode = "1. Trainee Agronomi"
# letak_kod_i = 0
# deskripsi = ''''''
# letak_des_i = 0
# uk_font = 24
# len_text = 55
# layer1.visible = False
# layer2.visible = True
# layer3.visible = False
# layer_vis = False
# peletakan(kode,letak_kod_i,deskripsi,letak_des_i,uk_font, len_text,layer_vis)





# if len(str_tolist_kode[y]) >= 5:
#     print ("============ skip ==================")
#     pass
# else:
#     if "Lowongan Kerja" in posisis[y] and len(str_tolist_kode[0][0]) == 0 and len(kualifikasis[0]) == 0:
#         print ("asadas")
#         pass
#     elif len(str_tolist_kode[y][0]) == 0 and len(kualifikasis[y][0]) == 0:
#         print ("asadas",str_tolist_kode[y][0],kualifikasis[y][0])
#         pass
#     else:
#         for oo in range (len(str_tolist_kode[y])):
#             tampung = []
            
#             # subjudul kualifikasi (kode_kualifikasi)
#             if len(str_tolist_kode[y][oo]) == 0 :
#                 if pengaktifan_AI == True:
#                     layer_sama("kode_Prasaratan "+str(oo), layer2, "", 1, True)
#                     layer_sama("kode_Prasaratan "+str(4), layer2, "", 1, True)
#             elif len(str_tolist_kode[y][oo]) >= 28 :
#                 if pengaktifan_AI == True:
#                     layer_sama("kode_Prasaratan "+str(4), layer2, str_tolist_kode[y][oo], 20, False)
#             else:
#                 if pengaktifan_AI == True:
#                     layer_sama("kode_Prasaratan "+str(oo), layer2, str_tolist_kode[y][oo], 32, False)
            
#             # kualifikasi (kualifikasi)
#             if len(kualifikasis[y][oo]) == 0 :
#                 if pengaktifan_AI == True:
#                     layer_sama("Prasaratnya "+str(oo), layer2, "", 1, True)
#             else:
#                 skalar = True
#                 ukuran_fontt = 20
#                 ukuran_str = 50
#                 if len(kualifikasis[y]) == 1:
#                     skalar = False
#                     ukuran_fontt = 30
#                     ukuran_str = 55
#                 elif len(kualifikasis[y]) == 2:
#                     skalar = True
#                     ukuran_fontt = 25
#                     ukuran_str = 37
#                 else:
#                     skalar = True
#                     ukuran_fontt = 20
#                     ukuran_str = 50
#                     print ("|||||||||||| Melebihi ||||||||||||||")
#                 data = kualifikasis[y][oo]
#                 info = listToString(data,skalar,str_tolist_kode[y][oo],ukuran_str)
#                 # print (len(kualifikasis[i][j]))
#                 if len(info[0]) >= 700:
#                     ukuran_fontt = 20
#                 if pengaktifan_AI == True:
#                     layer_sama("Prasaratnya "+str(oo), layer2, info[0], ukuran_fontt, False)
#                 tampung = info[1]

#             tampung_semua.update(tampung)

#         print ("============== kelebihan =============")
#         print ("tampungan-> ",tampung_semua)
#         no += 1
#         no_d -= 1
#         nomer_nama.append(no_d)
#         if pengaktifan_AI == True:
#             layer_sama("tgl", layer2, str(tgl), 22, False)
#             layer_sama("no", layer2, "0"+str(no), 147, False)
#             save_pic(row["Nama"],str(no_d))

# if pengaktifan_AI == True:      
#     layer2.visible = False    

