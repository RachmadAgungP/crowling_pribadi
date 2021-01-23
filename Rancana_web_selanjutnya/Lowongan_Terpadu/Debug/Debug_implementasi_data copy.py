import pandas as pd
import ast
import win32com.client as win32
import os
import textwrap
import datetime
# df = pd.read_csv("data_namapekerjaan1.csv")
df = pd.read_csv("Debug_data_namapekerjaan1.csv")
print (df.columns)

# kode_kual dan kualifikasi harus sama
now = datetime.datetime.now()
# tgl = str(now.strftime("%B %d, %Y"))
tgl = "December 11, 2020"
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

adobe_app = win32.GetActiveObject("Illustrator.Application")
adobe_document = adobe_app.ActiveDocument
layer1 = adobe_document.Layers("Layer1")
layer2 = adobe_document.Layers("Layer2")
layer3 = adobe_document.Layers("Layer3")
layer1.visible = False
layer2.visible = False
layer3.visible = False

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

    
def urai(df,pengaktifan_AI):
    r = 0
    info_keterangan = []
    tambahan_feed = {}
    nomer = []  #berapa banyak foto yang dihasilkan
    nama_file = []
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
        pos = listToString(posisis,True,"Posisi",55)

        no_d -= 1
        nomer_nama.append(no_d)

        print ("============ " + str(row["Nama"])+ " ================")

        if pengaktifan_AI == True: 
            layer1.visible = True
            # ============ posisi (feed 1) =============
            layer_sama("Nama_Perusahaan", layer1, str(row["Nama"]), 28, False)
            # ====> Gambar <====
            gam = layer1.placedItems("Gambar")
            gam.file = row['Path_Gambar']

                # ====> Daftar Posisi <====
            layer_sama("Posisi", layer1, pos[2], 31, False)
                # ====> Atribut lain <====
            layer_sama("tgl", layer1, str(tgl), 22, False)
            layer_sama("no", layer1, "0"+str(no), 147, False)
                # ========> SAVE <=======
            save_pic(row["Nama"],str(no_d))
            # ==========================================
            layer1.visible = False

        # ============ posisi (feed 2) =============
        for y in range (len(posisis)):
            
            print ("posisi ->",posisis[y])
            str_tolist_kode = list_edit[1][0]
            kualifikasis = list_edit[2][0]

            if pengaktifan_AI == True:
                layer2.visible = True
                for i in range(5):
                    layer_sama("kode_Prasaratan "+str(i), layer2, " ", 32, True)
                    layer_sama("Prasaratnya "+str(i), layer2, " ", 32, True)

                layer_sama("Nama_Posisi", layer2, posisis[y], 35, False)
            
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
                        if pengaktifan_AI == True:
                            # subjudul kualifikasi (kode_kualifikasi)
                            if len(str_tolist_kode[y][oo]) == 0 :
                                layer_sama("kode_Prasaratan "+str(oo), layer2, "", 1, True)
                                layer_sama("kode_Prasaratan "+str(4), layer2, "", 1, True)
                            elif len(str_tolist_kode[y][oo]) >= 28 :
                                layer_sama("kode_Prasaratan "+str(4), layer2, str_tolist_kode[y][oo], 20, False)
                            else:
                                layer_sama("kode_Prasaratan "+str(oo), layer2, str_tolist_kode[y][oo], 32, False)
                            
                        # kualifikasi (kualifikasi)
                        if len(kualifikasis[y][oo]) == 0 :
                            if pengaktifan_AI == True:
                                layer_sama("Prasaratnya "+str(oo), layer2, "", 1, True)
                        else:
                            skalar = True
                            ukuran_fontt = 20
                            ukuran_str = 50
                            if len(kualifikasis[y]) == 1:
                                skalar = False
                                ukuran_fontt = 30
                                ukuran_str = 55
                            elif len(kualifikasis[y]) == 2:
                                skalar = True
                                ukuran_fontt = 25
                                ukuran_str = 37
                            else:
                                skalar = True
                                ukuran_fontt = 20
                                ukuran_str = 50
                                print ("|||||||||||| Melebihi ||||||||||||||")
                            data = kualifikasis[y][oo]
                            info = listToString(data,skalar,str_tolist_kode[y][oo],ukuran_str)
                            # print (len(kualifikasis[i][j]))
                            if len(info[0]) >= 700:
                                ukuran_fontt = 20
                            if pengaktifan_AI == True:
                                layer_sama("Prasaratnya "+str(oo), layer2, info[0], ukuran_fontt, False)
                            tampung = info[1]

                        tampung_semua.update(tampung)

                    print ("============== kelebihan =============")
                    print ("tampungan-> ",tampung_semua)
                    no += 1
                    no_d -= 1
                    nomer_nama.append(no_d)
                    if pengaktifan_AI == True:
                        layer_sama("tgl", layer2, str(tgl), 22, False)
                        layer_sama("no", layer2, "0"+str(no), 147, False)
                        save_pic(row["Nama"],str(no_d))
            if pengaktifan_AI == True:      
                layer2.visible = False    
            # ==========================================
        
        # (feed 3)
        
        keter = ast.literal_eval(row['Keterangan'])
        keter.extend(ast.literal_eval(row['Apply']))
        i = 0
        n = len(keter)
        while i < n:
            element = keter[i]
            if element == 'Apply ' or element == 'Apply\xa0' or element == ', , , ':
            # if check(element):
                del keter[i]
                n = n - 1
            else:
                i = i + 1
        keteran = listToString(keter,False,'w',50)
        kete = listToString(keter,False,'w',50000)
        
        info_keterangan.append(kete[3])
        no += 1
        no_d -= 1
        nomer_nama.append(no_d)

        if pengaktifan_AI == True:
            layer3.visible = True
            layer_sama("Keterangan", layer3, keteran[3], 33, False)
            layer_sama("tgl", layer3, str(tgl), 22, False)
            layer_sama("no", layer3, "0"+str(no), 147, False)
            save_pic(row["Nama"],str(no_d))
            layer3.visible = False

        nomer.append(no)
        # ==========================================

        r+=1
        nama_file.append(nomer_nama)
      
    return info_keterangan,nomer,nama_file

rrun = urai(df,True)

dfe = pd.Series(rrun[0])
nom = pd.Series(rrun[1])
nomer_nam = pd.Series(rrun[2])
DF_fix = df
DF_fix['info'] =  dfe
DF_fix['byk_hasil'] = nom
DF_fix['nama_nomer'] = nomer_nam
DF_fix.to_csv('data_Fix.csv')

# print (df['kode_kual'][0])
# keter =[]
# info_keterangan = []
# for index,row in df.iterrows():
#     keter = ast.literal_eval(row['Keterangan'])
#     keter.extend(ast.literal_eval(row['Apply']))

#     i = 0
#     n = len(keter)
#     while i < n:
#         element = keter[i]
#         if element == 'Apply ' or element == 'Apply\xa0' or element == ', , , ':
#         # if check(element):
#             del keter[i]
#             n = n - 1
#         else:
#             i = i + 1

#     keteran = listToString(keter,False,'w',10000)
#     info_keterangan.append(keteran[3])
# print("ini info ",info_keterangan)
# dfe = pd.Series(info_keterangan)
# Ex = {'info':dfe}
# ccsv = pd.DataFrame(Ex)
# ccsv.to_csv('data_info.csv')

