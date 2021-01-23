import requests
import json
import base64
import re
import string
import pandas as pd

website = 'https://foloker.com/'
url = "%s/wp-json/wp/v2/"%website
user = "admin"
password = "NDkd g1ZD bIVo ylzE qL6v hyHl"
# b61p 3J0k BzoB 1oRb IUV8 G64a
credentials = user + ':' + password
token = base64.b64encode(credentials.encode()) 
headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

tgl = "December 21, 2020"
def category():
    # 60 = pendidikan
    # 61 = Jurusan
    yul = '%s/wp-json/wp/v2/categories/'%website
    jss = requests.get(yul)
    for i in range(len(json.loads(jss.content))):
        parsed= json.loads(jss.content)[i]['id']
        # print(json.dumps(parsed, indent=4, sort_keys=True))
    list_name = ["Kesehatan","Matematika & IPA (MIPA)","Sosial dan Humaniora","Ekonomi dan Bisnis","Sastra dan Budaya","Komputer dan Teknologi","Pendidikan","Pertanian","Profesi dan Ilmu Terapan","Seni","Teknik","Semua Jurusan"]
    list_pend = ["SMA/SMK/MA", "S1","S2","Diploma"]
    list_name_p = ["Pendidikan","Jurusan"]
    for y in list_name:
        posty = {"description" : y,
                "name": y,
                "slug": y,
                "parent": 61,
                "meta": []
            }
    print (len(list_name))
        # r = requests.post(url + 'categories', headers=headers, json=posty)
# category()

def tags():
    # 60 = pendidikan
    # 61 = Jurusan
    yul = '%s/wp-json/wp/v2/tags/'%website
    jss = requests.get(yul)
    for i in range(len(json.loads(jss.content))):
        parsed= json.loads(jss.content)[i]['name']
        print(json.dumps(parsed, indent=4, sort_keys=True))
    list_name_p = ["Aceh","Sumatera Utara (Sumut)","Sumatera Barat (Sumbar)","Riau","Jambi","Bengkulu","Sumatera Selatan (Sumsel)","Kepulauan Bangka Belitung","Lampung","Banten","Jawa Barat (Jabar)","DKI Jakarta","Jabodetabek","Jawa Tengah (Jateng)","Yogyakarta","Jawa Timur (Jatim)","Bali","Nusa Tenggara Barat (NTB)",
"Nusa Tenggara Timur (NTT)","Kalimantan Utara (Kaltara)","Kalimantan Barat (Kalbar)","Kalimantan Tengah (Kalteng)","Kalimantan Selatan (Kalsel)","Kalimantan Timur (Kaltim)","Gorontalo","Sulawesi Utara (Sulut)","Sulawesi Barat (Sulbar)","Sulawesi Tengah (Sulteng)","Sulawesi Selatan (Sulsel)","Sulawesi Tenggara (Sultra)",
"Maluku Utara","Maluku","Papua","Papua Barat", "Kepulauan Riau"]
    for y in list_name_p:
        posty = {"description" : y,
                "name": y,
                "slug": y,
                "meta": []
            }
        r = requests.post(url + 'tags', headers=headers, json=posty)
# tags()

data_loker = pd.read_csv("hasil\%s\data_namapekerjaan1.csv"%tgl)
# nama_perusahaan = data_loker['Nama']
artikel = data_loker['artikel']


    # caty = cat(Category)
    # print ("----> ", cat(Category))

yul = '%s/wp-json/wp/v2/tags/'%website
# jss = requests.get(yul)
# for i in range(len(json.loads(jss.content))):
#     parsed= json.loads(jss.content)[i]['id']
#     print(json.dumps(parsed, indent=4, sort_keys=True))
# for yu in range(90,124):
#     list_index_tag.append(str(yu))



# tag input tags 
dff_data_lokasi = pd.read_csv("Data\lokasi.csv")
list_name_tag = ["Aceh","Sumatera Utara","Sumatera Barat","Riau","Jambi","Bengkulu","Sumatera Selatan","Kepulauan Bangka Belitung","Lampung","Banten","Jawa Barat","DKI Jakarta","Jabodetabek","Jawa Tengah","Yogyakarta","Jawa Timur","Bali","Nusa Tenggara Barat",
"Nusa Tenggara Timur","Kalimantan Utara","Kalimantan Barat","Kalimantan Tengah","Kalimantan Selatan","Kalimantan Timur","Gorontalo","Sulawesi Utara","Sulawesi Barat","Sulawesi Tengah","Sulawesi Selatan","Sulawesi Tenggara",
"Maluku Utara","Maluku","Papua","Papua Barat", "Kepulauan Riau"]

list_index_tag = ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '100', '101', '102', '103', '104', '105', '106', '107', '108', '109', '110', '111', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123']

def tagss(index):
    lokasi = []
    for tu in dff_data_lokasi.columns:
        for u in dff_data_lokasi[tu]:
            if type(u) == float:
                continue
            else:
                if u in artikel[index]:
                    lokasi.append(tu.title())
    # print (lokasi)
    return lokasi

def tagsss(tagg):
    tu = 0
    tampungi = []
    for ttii in tagg:
        for yu in list_name_tag:
            if ttii in yu:
                tampungi.append(list_index_tag[tu])
        tu+=1
    return tampung
# imm = []
# for im in range(90,125):
#     imm.append(im)
# print (imm)
# for index in range (len(data_loker)):
#     lokasi = tagss(index)
#     print (lokasi)
#     indexx = tagsss(lokasi)
#     print (indexx)
ur = "https://foloker.com/wp-json/wp/v2/posts/"
jss = requests.get(ur)
for i in range(len(json.loads(jss.content))):
    parsed= json.loads(jss.content)['jetpack_featured_media_url']
    print(parsed)
# print (jss)