import pandas as pd
import ast
import win32com.client as win32
import os
import textwrap
import datetime
# df = pd.read_csv("data_namapekerjaan1.csv")
import shutil
import _AI_Size_otomatis

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

def layer_sama(nama_layer, layer_ke, isi, ukuran_font, visible):
    var = layer_ke.TextFrames(nama_layer)
    var.TextRange.Contents = str(isi)
    tR = var.textRange
    tR.characterAttributes.size = ukuran_font
    var.hidden = visible
    return (var)

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


def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r")
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

df = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl)
print (df.columns)
adobe_app = win32.GetActiveObject("Illustrator.Application")
adobe_document = adobe_app.ActiveDocument

def urai(index,row,pengaktifan_AI,tipe_gambar,layer1,layer2,layer3,adobe_document):
    info_keterangan = []
    kumpulan_penamaan_foto_decrement = []
    tampung_semua = {}
    nomer = []  #berapa banyak foto yang dihasilkan
    index_error = 0

    # nomer_nama = kumpulan_penamaan_foto_decrement
    no = 1
    list_edit = yuy(ast.literal_eval(row['Posisi']),ast.literal_eval(row["kode_kual"]),ast.literal_eval(row['Kualifikasi']))
    posisis = list_edit[0][0]

    # no_d = penamaan_decrement
    penamaan_foto_decrement = 1 + len(posisis) + 1
    if '*Tambahan Info' in posisis:
        posisis = list_edit[0][0][:-1]
    else:
        posisis = list_edit[0][0]
    
    print ("============ " + str(row["Nama"])+ " ================")
    pos = listToString(posisis,True,"Posisi")
    penamaan_foto_decrement -= 1
    kumpulan_penamaan_foto_decrement.append(penamaan_foto_decrement)
    if len(posisis) == 0 :
        print ("opp",str(row["Nama"]))
        info_keterangan.append("")
        no -= 1
        nomer.append(no)
        penamaan_foto_decrement += 1
        nama_file.append(0)
        pass
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
            _AI_Size_otomatis.contentnya("Nama_Perusahaan", layer1, str(row["Nama"]), uk_nama_p, False, False)
            # ====> Gambar <====
            logo_prusahaan = layer1.placedItems("Gambar")
            logo_prusahaan.file = row['Path_Gambar']
            # ====> Daftar Posisi <====
            _AI_Size_otomatis.contentnya("Posisi", layer1, pos[2], uk_p, False, True)
            # ====> Atribut lain <====
            if tipe_gambar == "story":
                pass
            else:
                # layer_sama("tgl", layer1, str(tgl), 22, False)
                layer_sama("no", layer1, "0"+str(no), 147, False)
            # ========> SAVE <=======
            if tipe_gambar == "story":
                save_pic(index,"story",str(penamaan_foto_decrement),adobe_document)
            else:
                save_pic(index,row["Nama"],str(penamaan_foto_decrement),adobe_document)
            # ==========================================
            layer1.visible = False
            
    return (kete[3],kumpulan_penamaan_foto_decrement,nomer)

def maine(df,tgl,tipe_gambar):
    try:
        if tipe_gambar == "story":
            layer1 = adobe_document.Layers("Layer1")
            layer1.visible = False
            r = 0
            info_keterangan = []
            tambahan_feed = {}
            nomer = []  #berapa banyak foto yang dihasilkan
            nama_file = []
            index_error = 0
            for index,row in df.iterrows():
                rrun = urai(index,row,True,tipe_gambar,layer1,layer1,layer1,adobe_document)
        else:
            layer1 = adobe_document.Layers("Layer1")
            layer2 = adobe_document.Layers("Layer2")
            layer3 = adobe_document.Layers("Layer3")
            layer1.visible = False
            layer2.visible = False
            layer3.visible = False
            r = 0
            info_keterangan = []
            tambahan_feed = {}
            nomer = []  #berapa banyak foto yang dihasilkan
            nama_file = []
            index_error = 0
            for index,row in df.iterrows():
                rrun = urai(index,row,True,tipe_gambar,layer1,layer2,layer3,adobe_document)
    
    except Exception as e:
        if tipe_gambar == "story":
            print ("ini",e)
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

tgl = baca_file()
tipe_gambar = "feed"
# tipe_gambar = "story"

