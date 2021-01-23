import pandas as pd
import ast
import win32com.client as win32
import os
import textwrap
import datetime
# df = pd.read_csv("data_namapekerjaan1.csv")
import shutil
import _AI_Size_otomatis

def yuy(posss,koddk,kualll):
    posisiss = []
    str_tolist_kodes = []
    kualifikasiss = []
    posisiss.append(posss)
    str_tolist_kodes.append(koddk)
    kualifikasiss.append(kualll)
    for y in range (len(posisiss)):
        o = 0
        for u in range (len(str_tolist_kodes[y])):
            if "General Requirements" in str_tolist_kodes[y][o] or "Persyaratan Umum" in str_tolist_kodes[y][o] or "Ketentuan" in str_tolist_kodes[y][o] or "Berkas Lamaran" in str_tolist_kodes[y][o]: 
                posisiss[0].append('*Tambahan Info')
                str_tolist_kodes[0].append(str_tolist_kodes[y][o])
                kualifikasiss[0].append(kualifikasiss[y][o])
                str_tolist_kodes[y][o] = [[]]
                kualifikasiss[y][o] = [[]]
                o -= 1
            o += 1
    print ("->",posisiss)
    print ("->",str_tolist_kodes)
    return posisiss, str_tolist_kodes, kualifikasiss
def Sorting(lst): 
    lst.sort(key=len, reverse=True) 
    return lst 
def sort_dict_by_value_len(dict_):
    return sorted(dict_.items(), key=lambda kv: (len(kv[1]), kv[0]),reverse=True)

def hitung_char_in_layer3(data,str_tolist_kode,if_3):
    list_banyak_char_layer3_kode = []
    list_banyak_char_layer3_value = []
    for y in range(len(data)):
        p = []
        valuee = {}
        for oo in range (len(data[y])):
            datas = data[y][oo]
            info = listToString(datas,False,str_tolist_kode[y][oo])
            p.append(len(info[0]))
            valuee.update(info[4])
        # p.sort(reverse=True)
        kode =  sort_dict_by_value_len(valuee)
        # kual = sorted(valuee.values(), key=lambda s: len(valuee.get(s)), reverse=True)
        list_banyak_char_layer3_kode.append(kode)
        # list_banyak_char_layer3_value.append(kual)
    # print ("sdadasdad",list_banyak_char_layer3)
    # print ("->",list_banyak_char_layer3_kode)
    # for ion in range(len(list_banyak_char_layer3)):
    #     for ui in range(len(list_banyak_char_layer3[ion])):
    #         if ion == 0:
    #             _AI_Size_otomatis.contentnya("Prasaratnya "+str(ui), if_3, list_banyak_char_layer3[ion][ui], 24, False,True)
    #         else:
    #             break
    return (list_banyak_char_layer3_kode)
                                    

def listToString(s,skalar,kod):  
    str1 = ""
    tnpa_tnd_bca = ""
    str1_over = ""
    kod = kod
    if kod == []:
        kod = "Pilihan"
        print (kod)
   
    print (kod)
    tampungan = {kod:[]} 
    tampung_semua= {kod:[]} 
    items = {kod:[]}
    w = 1
    hitung_baris = 0
    for ele in s: 
        if ele == "":
            pass
        else:
            str1 += "\n"+"-\t"+ ele
            tnpa_tnd_bca += "\n"+ ele
            tampungan[kod].append("\n"+"-\t"+ ele)
            tampung_semua[kod].append("\n"+"-\t"+ ele)
            hitung_baris += 1
        w += 1
    # tampungan[kod].append(str1)
    if len(tampungan[kod]) >=10:
        if skalar == True:
            items[kod] = tampungan[kod][10:len(tampungan[kod])]
            tampungan[kod] = tampungan[kod][:10]
            tampungan[kod].append(os.linesep+"- penjelasan ada di web Foloker.com ...")
            print (items)
            for i in tampungan[kod]:
                str1_over += i
        else:
            for i in tampungan[kod]:
                str1_over += i 
    else:
        for i in tampungan[kod]:
            str1_over += i    
    # print ("kualifikasi-> ",str1_over)
    # print ("->tampung",sort_dict_by_value_len(tampung_semua))
    return str1_over,items,str1,tnpa_tnd_bca,tampung_semua


def urai(df,pengaktifan_AI,tipe_gambar,layer1,layer2,if_1,if_2,if_3,if_4,layer3,adobe_document):
    r = 0
    info_keterangan = []
    tambahan_feed = {}
    nomer = []  #berapa banyak foto yang dihasilkan
    nama_file = []
    index_error = 0
    for index,row in df.iterrows():
        # Nama (feed 1)
        
        nomer_nama = []
        tampung_semua = {}
        tt = 0
        no = 1
        list_edit = yuy(ast.literal_eval(row['Posisi']),ast.literal_eval(row["kode_kual"]),ast.literal_eval(row['Kualifikasi']))
        posisis = list_edit[0][0]
        no_d = 1 + len(posisis) + 1

        if '*Tambahan Info' in posisis:
            posisis = list_edit[0][0][:-1]
        else:
            posisis = list_edit[0][0]
        pos = listToString(posisis,True,"Posisi")

        no_d -= 1
        nomer_nama.append(no_d)

        print ("============ " + str(row["Nama"])+ " ================")
        if len(posisis) == 0 :
            print ("opp",str(row["Nama"]))
            info_keterangan.append("")
            no -= 1
            nomer.append(no)
            no_d += 1
            nama_file.append(0)
            continue
        else:
        #     if pengaktifan_AI == True: 
        #         layer1.visible = True
        #         if tipe_gambar == "story":
        #             uk_nama_p = 31
        #             uk_p = 35
        #         else:
        #             uk_nama_p = 28
        #             uk_p = 40
        #         # ============ posisi (feed 1) =============
        #         _AI_Size_otomatis.contentnya("Nama_Perusahaan", layer1, str(row["Nama"]), uk_nama_p, False,False)
        #         # ====> Gambar <====
        #         gam = layer1.placedItems("Gambar")
        #         gam.file = row['Path_Gambar']
            
        #             # ====> Daftar Posisi <====
        #         _AI_Size_otomatis.contentnya("Posisi", layer1, pos[2], uk_p, False,True)
        #             # ====> Atribut lain <====
        #         if tipe_gambar == "story":
        #             pass
        #         else:
        #             # _AI_Size_otomatis.contentnya("tgl", layer1, str(tgl), 22, False)
        #             _AI_Size_otomatis.contentnya("no", layer1, "0"+str(no), 147, False,False)
        #             # ========> SAVE <=======
        #         if tipe_gambar == "story":
        #             # save_pic(index,"story",str(no_d),adobe_document)
        #         else:
        #             # save_pic(index,row["Nama"],str(no_d),adobe_document)
        #         # ==========================================
        #         layer1.visible = False
        # ============ posisi (feed 2) =============
            if tipe_gambar == "story":
                continue
            else:
                for y in range (len(posisis)):
                    
                    print ("posisi ->",posisis[y])
                    str_tolist_kode = list_edit[1][0]
                    kualifikasis = list_edit[2][0]

                    if pengaktifan_AI == True:
                        layer2.visible = True
                        
                        _AI_Size_otomatis.contentnya("Nama_Posisi", layer2, posisis[y], 35, False,True)
                    
                    if len(str_tolist_kode[y]) >= 5:
                        print ("============ skip ==================")
                        pass
                    else:
                        if "Lowongan Kerja" in posisis[y] and len(str_tolist_kode[0][0]) == 0 and len(kualifikasis[0]) == 0:
                            print ("asadas")
                            pass
                        elif len(str_tolist_kode[y][0]) == 0 and len(kualifikasis[y][0]) == 0:
                            print ("asadas",str_tolist_kode[y][0],kualifikasis[y][0])
                            pass
                        else:
                            for oo in range (len(str_tolist_kode[y])):
                                tampung = []
                                
                                # subjudul kualifikasi (kode_kualifikasi)
                                if len(str_tolist_kode[y][oo]) == 0 :
                                    if pengaktifan_AI == True:
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), layer2, "", 1, True,False)
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(4), layer2, "", 1, True,False)
                                elif len(str_tolist_kode[y][oo]) >= 28 :
                                    if pengaktifan_AI == True:
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(4), layer2, str_tolist_kode[y][oo], 20, False, True)
                                # else:
                                #     if pengaktifan_AI == True:
                                #         _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), layer2, str_tolist_kode[y][oo], 32, False, True)
                                
                                # kualifikasi (kualifikasi)
                                # if len(kualifikasis[y][oo]) == 0 :
                                #     if pengaktifan_AI == True:
                                #         _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), layer2, "", 1, True,False)
                                # else:
                                skalar = True
                                ukuran_fontt = 30
                                # if pengaktifan_AI == True:
                                if len(kualifikasis[y]) == 1:
                                    if_1.visible = True
                                    if len(str_tolist_kode[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_1, "\n", 1, True,False)
                                    else:
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_1, str_tolist_kode[y][oo], 32, False, True)
                                    skalar = False
                                    data = kualifikasis[y][oo]
                                    info = listToString(data,skalar,str_tolist_kode[y][oo])
                                    if len(kualifikasis[y][oo]) == 0:
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_1, "\n", ukuran_fontt, False,True)
                                    else:
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_1, info[0], ukuran_fontt, False,True)
                                elif len(kualifikasis[y]) == 2:
                                    if_2.visible = True
                                    if len(str_tolist_kode[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_2, "\n", 1, True,False)
                                    else:
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_2, str_tolist_kode[y][oo], 32, False, True)
                                    skalar = False
                                    data = kualifikasis[y][oo]
                                    info = listToString(data,skalar,str_tolist_kode[y][oo])
                                    if len(kualifikasis[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_2, "\n", ukuran_fontt, False,True)
                                    else:
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_2, info[0], ukuran_fontt, False,True)
                                elif len(kualifikasis[y]) == 3:
                                    if_3.visible = True
                                    info = hitung_char_in_layer3(kualifikasis,str_tolist_kode,if_3)[y][oo]
                                    if len(str_tolist_kode[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_3, "\n", 1, True,False)
                                    else:
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_3, info[0], 32, False, True)
                                    skalar = False
                                    if len(kualifikasis[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_3, "\n", ukuran_fontt, False,True)
                                    else:
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_3, info[1], ukuran_fontt, False,True)
                                elif len(kualifikasis[y]) == 4:
                                    if_4.visible = True
                                    # info = hitung_char_in_layer3(kualifikasis,str_tolist_kode,if_3)[y][oo]
                                    if len(str_tolist_kode[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_4, "\n", 1, True,False)
                                    else:
                                        _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), if_4, str_tolist_kode[y][oo], 32, False, True)
                                    skalar = False
                                    data = kualifikasis[y][oo]
                                    info = listToString(data,skalar,str_tolist_kode[y][oo])
                                    if len(kualifikasis[y][oo]) == 0 :
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_4, "\n", ukuran_fontt, False,True)
                                    else:
                                        _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), if_4, info[0], ukuran_fontt, False,True)

                                else:
                                    skalar = True
                                    ukuran_fontt = 20
                                    print ("|||||||||||| Melebihi ||||||||||||||")
                                
                                    # tampung = info[1]

                                # tampung_semua.update(tampung)

                            print ("============== kelebihan =============")
                            print ("tampungan-> ",tampung_semua)
                            no += 1
                            no_d -= 1
                            nomer_nama.append(no_d)
                            if pengaktifan_AI == True:
                                # _AI_Size_otomatis.contentnya("tgl", layer2, str(tgl), 22, False)
                                _AI_Size_otomatis.contentnya("no", layer2, "0"+str(no), 147, False,False)
                                save_pic(index,row["Nama"],str(no_d),adobe_document)
                    
                    if pengaktifan_AI == True:      
                        layer2.visible = False    
                    # ==========================================
                    
            

def main(tgl,tipe_gambar):
    df = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl)
    print (df.columns)

    adobe_app = win32.GetActiveObject("Illustrator.Application")
    adobe_document = adobe_app.ActiveDocument

    if tipe_gambar == "story":
        layer1 = adobe_document.Layers("Layer1")
        layer1.visible = False
        rrun = urai(df,True,tipe_gambar,layer1,layer1,layer1,adobe_document)
    else:
        layer1 = adobe_document.Layers("Layer1")
        layer2 = adobe_document.Layers("Layer2")
        if_1 = adobe_document.Layers("if_1")
        if_2 = adobe_document.Layers("if_2")
        if_3 = adobe_document.Layers("if_3")
        if_4 = adobe_document.Layers("if_4")
        layer3 = adobe_document.Layers("Layer3")
        layer1.visible = False
        layer2.visible = False
        if_1.visible = False
        if_2.visible = False
        if_3.visible = False
        if_4.visible = False
        layer3.visible = False
        rrun = urai(df,True,tipe_gambar,layer1,layer2,if_1,if_2,if_3,if_4,layer3,adobe_document)

def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r")
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

tgl = baca_file()
tipe_gambar = "feed"
main(tgl,tipe_gambar)