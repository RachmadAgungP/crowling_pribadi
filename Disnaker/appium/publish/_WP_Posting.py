
import requests
import json
import unidecode
def post_media(url,nama_image,headers):
    image_urls = 'images/%s'%nama_image
    urls = '%smedia'%url
    media = {'file': open(image_urls, 'rb'), 'caption': 'HappyFace'}
    image = requests.post(urls, headers=headers, files=media)
    # print('Your image is published on ' + json.loads(image.content)['source_url'])
    # print(json.loads(image.content)['id'])
    return json.loads(image.content)['id']

def post_artikel(url,user,password,title,artikel,token,id_image,id_category,tgl,index,headers,id_tags):
    post = {
    'title'    : title,
    'status'   : 'publish', 
    'content'  : '''%s'''%artikel,
    'categories': id_category, 
    'date'   : tgl+'T06:00:00',
    'tags'   : id_tags,
    'featured_media': id_image,
    }
    r = requests.post(url + 'posts', headers=headers, json=post)
    # print("ini ID POST ",json.loads(r.content)["id"])
    return r

def search_img(title,nama_image,url,jss,headers):
    list_id = [] 
    id_img = ''
    title = unidecode.unidecode(title)
    for i in range(len(json.loads(jss.content))):
        # for key in json.loads(jss.content)[i]:
        title_db = json.loads(jss.content)[i]["title"]['rendered']
        if title_db[-1].isnumeric():
            title_db = title_db.replace("-%s"%title_db[-1],"") 
        if title == title_db:
            id_img = json.loads(jss.content)[i]["id"]
        list_id.append(title_db)
    if title in list_id:
        print ("ada")
        id_image = id_img
    else:
        print ("tidak ada")
        print (title)
        print (list_id)
        id_image = post_media(url,nama_image,headers)
    return (id_image)   


# import _WP_Seleksi_category
# import pandas as pd
# import _tgl_
# import string
# import base64
# import re
# from datetime import date

# def debuging_Posting(tgl,index):
#     tgl_a = re.sub(r"\D", " ", tgl)
#     tgl_b = tgl_a.split()
#     tgl_c = int(tgl_b[0])
#     month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
#     bulan = month.index(tgl.split()[0])+1
#     tahun = tgl.split()[-1]
#     tgll = date(int(tahun), bulan,tgl_c).isoformat()

#     data_loker = pd.read_csv("E:/Belajar/www.disnakerja.com/hasil/%s/data_namapekerjaan1.csv"%tgl)
#     nama_perusahaan = data_loker['Nama']
#     Path_Gambar = data_loker["Path_Gambar"]
#     website = 'https://foloker.com/'
#     url = "%s/wp-json/wp/v2/"%website
#     yul = '%s/wp-json/wp/v2/media/'%website
#     jss = requests.get(yul) 

#     website = 'https://foloker.com/'
#     url = "%s/wp-json/wp/v2/"%website
#     user = "admin"
#     password = "NDkd g1ZD bIVo ylzE qL6v hyHl"
#     credentials = user + ':' + password
#     token = base64.b64encode(credentials.encode()) 
#     headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

#     category_jurusan = pd.read_csv("Data\data_jurusan.csv")
#     category_lokasi  = pd.read_csv("Data\lokasi.csv")
#     category_lulusan = ['SMA','SMK','MA','D3','Diploma','S1','Bachelor','S2','Master']

#     title = nama_perusahaan[index]
#     title_img = title.translate(str.maketrans("","",string.punctuation)).replace("  "," ").replace(" ","-")
#     # print ("judul Img ",title_img)
#     with open('hasil\%s\html\%s.html'%(tgl,nama_perusahaan[index]), 'r', encoding='utf-8-sig') as f:
#         html_string = f.read()
#     artikela = html_string
#     # artikela = artikel[index] 

#     nama_image = Path_Gambar[index].split("/")[-1]
#     id_image = search_img(title,nama_image,url,jss,headers)
#     # print ("id_image ", id_image)
#     Category = _WP_Seleksi_category.text_categorys(index,tgl,category_jurusan,category_lulusan,category_lokasi,nama_perusahaan)
#     id_category = _WP_Seleksi_category.id_categorys(Category)[0]
#     id_tags = _WP_Seleksi_category.id_categorys(Category)[1]
#     idpost = post_artikel(url,user,password,"Lowongan Kerja "+title,artikela,token,id_image,id_category,tgll,index,headers,id_tags)
#     id_post = json.loads(idpost.content)['id']
#     print ("Posting sukses",id_post)

#     return (id_post)

# tgl = _tgl_.baca_file()
# # tgl = "January 29, 2021"
# index = 9
# debuging_Posting(tgl,9)