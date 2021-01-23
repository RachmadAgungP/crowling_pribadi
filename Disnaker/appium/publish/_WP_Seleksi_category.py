
# ss = category_lulusan
# rr = text category
def data_artikel_html(tgl,nama_perusahaan,index):
    with open('hasil\%s\html\%s.html'%(tgl,nama_perusahaan[index]), 'r') as f:
        html_string = f.read()
    return html_string

def text_categorys(index,tgl,category_jurusan,category_lulusan,category_lokasi,nama_perusahaan):
    jurusan = []
    lulusan = []
    lokasi = []
    nama = []
    tampung_index = []
    for tu in category_jurusan.columns:
        for u in category_jurusan[tu]:
            if type(u) == float:
                continue
            else:
                
                if u in data_artikel_html(tgl,nama_perusahaan,index):
                    tampung_index.append(index)
                    jurusan.append(tu)
    for u in category_lulusan:
        if type(u) == float:
            continue
        else:
            if u in data_artikel_html(tgl,nama_perusahaan,index):
                lulusan.append(u)   
    # ll = category_lokasi.columns
    # print (list(ll))
    # for yu in list(ll):
    # print (";",category_lokasi)
    for tu in category_lokasi.columns:
        for u in category_lokasi[tu]:
            # print ("=",type(u))
            if type(u) == float:
                continue
            else:
                if u in data_artikel_html(tgl,nama_perusahaan,index):
                    lokasi.append(tu.title())
                    
    print (data_artikel_html(tgl,nama_perusahaan,index))
                    

    print (nama_perusahaan[index])
    print ("category jurusan : ",jurusan)
    print ("category lulusan : ",lulusan)
    print ("category lokasi : ",lokasi)
    return jurusan,lulusan,lokasi

list_name = ["Kesehatan","Matematika & IPA (MIPA)","Sosial dan Humaniora","Ekonomi dan Bisnis","Sastra dan Budaya","Komputer dan Teknologi","Pendidikan","Pertanian","Profesi dan Ilmu Terapan","Seni","Teknik","Semua Jurusan"]
list_pend   = ["SMA/SMK/MA","S1","S2","Diploma"]
list_name_p = ["Pendidikan","Jurusan"]
list_name_tag = ["Aceh","Sumatera Utara","Sumatera Barat","Riau","Jambi","Bengkulu","Sumatera Selatan","Kepulauan Bangka Belitung","Lampung","Banten","Jawa Barat","Jakarta","Jabodetabek","Jawa Tengah","Yogyakarta","Jawa Timur","Bali","Nusa Tenggara Barat",
"Nusa Tenggara Timur","Kalimantan Utara","Kalimantan Barat","Kalimantan Tengah","Kalimantan Selatan","Kalimantan Timur","Gorontalo","Sulawesi Utara","Sulawesi Barat","Sulawesi Tengah","Sulawesi Selatan","Sulawesi Tenggara",
"Maluku Utara","Maluku","Papua","Papua Barat", "Kepulauan Riau"]

index_cate = [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
index_pend = [62,63,64,65]
list_index_tag = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]

# cat = id_category
def id_categorys(Category):
    t = 0
    tampung = []
    id_jurusan = []
    id_lulusan = []
    id_lokasi = []
    for tti in Category[0]:
        if tti in list_name:
            tampung.append(index_cate[list_name.index(tti)])
            id_jurusan.append(index_cate[list_name.index(tti)])
        t+=1

    ti =0
    for tii in Category[1]:
        if tii == 'SMA' or tii == 'SMK' or tii == 'MA':
            tii = 'SMA/SMK/MA'
            tampung.append(index_pend[list_pend.index(tii)])
            id_lulusan.append(index_pend[list_pend.index(tii)])
        elif tii == 'D3' or tii == 'Diploma' or tii == 'D1' or tii == 'D2':
            tii = 'Diploma'
            tampung.append(index_pend[list_pend.index(tii)])
            id_lulusan.append(index_pend[list_pend.index(tii)])
        elif tii == 'S1' or tii == 'Bachelor' :
            tii = 'S1'
            tampung.append(index_pend[list_pend.index(tii)])
            id_lulusan.append(index_pend[list_pend.index(tii)])
        elif tii == 'S2' or tii == 'Magister' or tii == 'Master':
            tii = 'S2'
            tampung.append(index_pend[list_pend.index(tii)])
            id_lulusan.append(index_pend[list_pend.index(tii)])
        ti+=1
    
    tu = 0
    for ttii in Category[2]:
        print ("io")
        for yu in list_name_tag:
            print ("oi",yu)
            if ttii in yu:
                tampung.append(list_index_tag[list_name_tag.index(ttii)])
                id_lokasi.append(list_index_tag[list_name_tag.index(ttii)])
        tu+=1
    print ("id_semua :",list(set(tampung)))
    print ("id_jurusan :",list(set(id_jurusan)))
    print ("id_lulusan :",list(set(id_lulusan)))
    print ("id_lokasi :",list(set(id_lokasi)))
    print ("=====================")
    return list(set(tampung))

import pandas as pd
import _tgl_
tgl = _tgl_.baca_file()
category_jurusan = pd.read_csv("Data\data_jurusan.csv")
category_lokasi  = pd.read_csv("Data\lokasi.csv")
category_lulusan = ['SMA','SMK','MA','D3','Diploma','S1','Bachelor','S2','Master']
data_loker = pd.read_csv("E:\Belajar\www.disnakerja.com\hasil\%s\data_namapekerjaan1.csv"%tgl) 
nama_perusahaan = data_loker['Nama']

Category = text_categorys(9,tgl,category_jurusan,category_lulusan,category_lokasi,nama_perusahaan)
id_category = id_categorys(Category)