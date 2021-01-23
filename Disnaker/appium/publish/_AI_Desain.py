import pandas as pd
import ast
import win32com.client as win32
import os
import textwrap
import datetime
# df = pd.read_csv("data_namapekerjaan1.csv")
import shutil
import _AI_Size_otomatis

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
        if ele == "":
            pass
        else:
            str1 += os.linesep+"- "+" "+ ele
            tnpa_tnd_bca += os.linesep+ ele
            tampungan[kod].append(os.linesep+"- "+" "+ ele)
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
    print ("kualifikasi-> ",str1_over)

    return str1_over,items,str1,tnpa_tnd_bca


def  _AI_Size_otomatis.contentnya(nama_layer, layer_ke, isi, ukuran_font, visible):
    var = layer_ke.TextFrames(nama_layer)
    var.TextRange.Contents = str(isi)
    tR = var.textRange
    tR.characterAttributes.size = ukuran_font
    var.hidden = visible
    return (var)

def save_pic(urut,nama,tt,adobe_document):
    # Define the Export JPEG Options.
    jpeg_export_options = win32.Dispatch("Illustrator.ExportOptionsJPEG")

    # Export the document.
    if nama == "story":
        newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/{}'.format(tgl,"story")
    else:
        newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/{}'.format(tgl,str(urut)+". "+nama)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if nama == "story":
        adobe_document.Export(
        ExportFile=r"E:/Belajar/www.disnakerja.com/hasil/{}/{}/{}".format(
            str(tgl),"story",str(urut)
        ),
        ExportFormat=1,
        Options=jpeg_export_options
        )
    else:
        adobe_document.Export(
            ExportFile=r"E:/Belajar/www.disnakerja.com/hasil/{}/{}/{}".format(
                str(tgl),str(urut)+". "+nama,str(tt)
            ),
            ExportFormat=1,
            Options=jpeg_export_options
        )

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

    
def urai(df,pengaktifan_AI,tipe_gambar,layer1,layer2,layer3,adobe_document):
    r = 0
    info_keterangan = []
    tambahan_feed = {}
    nomer = []  #berapa banyak foto yang dihasilkan
    nama_file = []
    index_error = 0
    for index,row in df.iterrows():
        # Nama (feed 1)
        try:
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
            pos = listToString(posisis,True,"Posisi",55)

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
                if pengaktifan_AI == True: 
                    layer1.visible = True
                    if tipe_gambar == "story":
                        uk_nama_p = 31
                        uk_p = 35
                    else:
                        uk_nama_p = 28
                        uk_p = 31
                    # ============ posisi (feed 1) =============
                    _AI_Size_otomatis.contentnya("Nama_Perusahaan", layer1, str(row["Nama"]), uk_nama_p, False,False)
                    # ====> Gambar <====
                    gam = layer1.placedItems("Gambar")
                    gam.file = row['Path_Gambar']
                
                        # ====> Daftar Posisi <====
                    _AI_Size_otomatis.contentnya("Posisi", layer1, pos[2], uk_p, False, True)
                        # ====> Atribut lain <====
                    if tipe_gambar == "story":
                        pass
                    else:
                        #  _AI_Size_otomatis.contentnya("tgl", layer1, str(tgl), 22, False)
                         _AI_Size_otomatis.contentnya("no", layer1, "0"+str(no), 147, False, False)
                        # ========> SAVE <=======
                    if tipe_gambar == "story":
                        save_pic(index,"story",str(no_d),adobe_document)
                    else:
                        save_pic(index,row["Nama"],str(no_d),adobe_document)
                    # ==========================================
                    layer1.visible = False
                print ("aaaaa",ast.literal_eval(row['Keterangan']))
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
                            # hidden layer
                            for i in range(5):
                                 _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(i), layer2, " ", 32, True,False)
                                 _AI_Size_otomatis.contentnya("Prasaratnya "+str(i), layer2, " ", 32, True,True)

                             _AI_Size_otomatis.contentnya("Nama_Posisi", layer2, posisis[y], 35, False,False)
                        
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
                                             _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(4), layer2, str_tolist_kode[y][oo], 20, False,False)
                                    else:
                                        if pengaktifan_AI == True:
                                             _AI_Size_otomatis.contentnya("kode_Prasaratan "+str(oo), layer2, str_tolist_kode[y][oo], 32, False,False)
                                    
                                    # kualifikasi (kualifikasi)
                                    if len(kualifikasis[y][oo]) == 0 :
                                        if pengaktifan_AI == True:
                                             _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), layer2, "", 1, True,False)
                                    else:
                                        skalar = True
                                        ukuran_fontt = 20
                                        if len(kualifikasis[y]) == 1:
                                            skalar = False
                                            ukuran_fontt = 30
                                        elif len(kualifikasis[y]) == 2:
                                            skalar = True
                                            ukuran_fontt = 25
                                        else:
                                            skalar = True
                                            ukuran_fontt = 20
                                            print ("|||||||||||| Melebihi ||||||||||||||")
                                        data = kualifikasis[y][oo]
                                        info = listToString(data,skalar,str_tolist_kode[y][oo],ukuran_str)
                                        # print (len(kualifikasis[i][j]))
                                        if len(info[0]) >= 700:
                                            ukuran_fontt = 20
                                        if pengaktifan_AI == True:
                                             _AI_Size_otomatis.contentnya("Prasaratnya "+str(oo), layer2, info[0], ukuran_fontt, False,True)
                                        tampung = info[1]

                                    tampung_semua.update(tampung)

                                print ("============== kelebihan =============")
                                print ("tampungan-> ",tampung_semua)
                                no += 1
                                no_d -= 1
                                nomer_nama.append(no_d)
                                if pengaktifan_AI == True:
                                    #  _AI_Size_otomatis.contentnya("tgl", layer2, str(tgl), 22, False)
                                     _AI_Size_otomatis.contentnya("no", layer2, "0"+str(no), 147, False,False)
                                    save_pic(index,row["Nama"],str(no_d),adobe_document)
                        
                        if pengaktifan_AI == True:      
                            layer2.visible = False    
                        # ==========================================
                        
                    # (feed 3)
                    keter = ast.literal_eval(row['Keterangan'])
                    print ("iniloh----",keter)
                    
                    keteran = listToString(keter,False,'w',50)
                    
                    kete = listToString(keter,False,'w',50000)
                    
                    # if type(row["Posisi"]) == float :
                    #     print ("pass")
                    #     continue
                    # else:
                    # info_keterangan.append("")
                    info_keterangan.append(kete[3])
                    no += 1
                    no_d -= 1
                    nomer_nama.append(no_d)
                    
                    if pengaktifan_AI == True:
                        layer3.visible = True
                        
                         _AI_Size_otomatis.contentnya("Keterangan", layer3, keteran[3] + "\n Informasi Lebih lanjut Kunjungi Foloker.com", 33, False,False)
                        #  _AI_Size_otomatis.contentnya("tgl", layer3, str(tgl), 22, False)
                         _AI_Size_otomatis.contentnya("no", layer3, "0"+str(no), 147, False,False)
                        save_pic(index,row["Nama"],str(no_d),adobe_document)
                        layer3.visible = False

        except Exception as e:
            if tipe_gambar == "story":
                print ("ini",e)
                continue
            else:
                if pengaktifan_AI == True:      
                    layer2.visible = False
                # newpath = r'E:/Belajar/www.disnakerja.com/hasil/{}/{}'.format(tgl,str(index)+". "+row["Nama"])  
                # shutil.rmtree(newpath)
                index_error = index
                df_er = df.loc[[index]]
                df = df.drop(index = index)
                print ("opo",df['Alamat'])
                newpath = r'Disnaker/appium/Debug/Data_debug/{}'.format(tgl) 
                if not os.path.exists(newpath):
                    os.makedirs(newpath)
                df_er.to_csv('Disnaker/appium/Debug/Data_debug/%s/data_saat_Debug.csv'%tgl)
                no = no + 1
                no_d = no_d + 1
                info_keterangan.append("")
        
        nomer.append(no)
            # ==========================================
        r+=1
        nama_file.append(nomer_nama)
        

    return info_keterangan,nomer,nama_file,index_error


def maine(tgl,tipe_gambar):
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
        layer3 = adobe_document.Layers("Layer3")
        layer1.visible = False
        layer2.visible = False
        layer3.visible = False
        rrun = urai(df,True,tipe_gambar,layer1,layer2,layer3,adobe_document)

    dfe = pd.Series(rrun[0])
    nom = pd.Series(rrun[1])
    nomer_nam = pd.Series(rrun[2])
    DF_fix = df
    DF_fix['info'] =  dfe
    DF_fix['byk_hasil'] = nom
    DF_fix['nama_nomer'] = nomer_nam
    print (rrun[3])
    # DF_EDIT = DF_fix.drop(index=rrun[3])
    if tipe_gambar == "story":
        pass
    else:
        DF_fix.to_csv('hasil\%s\data_Fix.csv'%tgl)

def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r")
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

tgl = baca_file()
# kode_kual dan kualifikasi harus sama
            # now = datetime.datetime.now()
            # # tgl = str(now.strftime("%B %d, %Y"))
            # # tgl = "January 6, 2021"
tipe_gambar = "feed"
# tipe_gambar = "story"

maine(tgl,tipe_gambar)


