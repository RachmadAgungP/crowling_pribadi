import requests
import json
import base64
import re
import string
import pandas as pd 
import numpy as np
from datetime import date
from bs4 import BeautifulSoup, NavigableString, Tag
import unidecode
import random
import _WP_Seleksi_category
import _WP_Posting
# import _buat_content

def maine(tgl,uppy):
    data_loker = pd.read_csv("E:\Belajar\www.disnakerja.com\hasil\%s\data_namapekerjaan1.csv"%tgl)
    # datetime.now().isoformat(timespec='minutes')   
    nama_perusahaan = data_loker['Nama']
    # for ind in uppy:
    #     _buat_content.htmll(tgl,ind,data_loker)

    # datai = uppy
    datai = random.sample(uppy,len(uppy))
    print(datai)
    tgl_a = re.sub(r"\D", " ", tgl)
    tgl_b = tgl_a.split()
    tgl_c = int(tgl_b[0])
    print (tgl_c)
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    bulan = month.index(tgl.split()[0])+1
    tahun = tgl.split()[-1]
    
    tgll = date(int(tahun), bulan,tgl_c).isoformat()
    tglan = "%s/%s/%s"%(str(tahun),str(bulan),str(tgl_c+1))
    
    # artikel = html_string

    category_jurusan = pd.read_csv("Data\data_jurusan.csv")
    category_lokasi  = pd.read_csv("Data\lokasi.csv")
    category_lulusan = ['SMA','SMK','MA','D3','Diploma','S1','Bachelor','S2','Master']

    website = 'https://foloker.com/'
    url = "%s/wp-json/wp/v2/"%website
    user = "admin"
    password = "NDkd g1ZD bIVo ylzE qL6v hyHl"
    credentials = user + ':' + password
    token = base64.b64encode(credentials.encode()) 
    headers = {'Authorization': 'Basic ' + token.decode('utf-8')}

    yul = '%s/wp-json/wp/v2/media/'%website
    jss = requests.get(yul)         

    data_loker = pd.read_csv("E:/Belajar/www.disnakerja.com/hasil/%s/data_namapekerjaan1.csv"%tgl)
    nama_perusahaan = data_loker['Nama']
    # artikel = data_loker['artikel']

    from selenium import webdriver
    import time
    from selenium.webdriver.common.keys import Keys

    USERNAME = 'admin'
    PASSWORD = 'AGUNG19541'

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://foloker.com/wp-admin')

    user_input = driver.find_element_by_id('user_login')
    user_input.send_keys(USERNAME)

    password_input = driver.find_element_by_id('user_pass')
    password_input.send_keys(PASSWORD)

    login_button = driver.find_element_by_id('wp-submit')
    login_button.click()
    
    for index in datai:
        # ======= Posing Artikel 
        index = index
        title = nama_perusahaan[index]
        title_img = title.translate(str.maketrans("","",string.punctuation)).replace("  "," ").replace(" ","-")
        # print ("judul Img ",title_img)
        with open('hasil\%s\html\%s.html'%(tgl,nama_perusahaan[index]), 'r') as f:
            html_string = f.read()
        artikela = html_string
        # artikela = artikel[index] 

        nama_image = '%s.jpg'%title
        id_image = _WP_Posting.search_img(title,nama_image,url,jss,headers)
        # print ("id_image ", id_image)
        Category = _WP_Seleksi_category.text_categorys(index,tgl,category_jurusan,category_lulusan,category_lokasi,nama_perusahaan)
        id_category = _WP_Seleksi_category.id_categorys(Category)
        # print ("----> ", cat(Category))
        # 2020-12-05
        idpost = _WP_Posting.post_artikel(url,user,password,"Lowongan Kerja "+title,artikela,token,id_image,id_category,tgll,index,headers)
        id_post = json.loads(idpost.content)['id']

        # proses SEO
        ar = artikela
        soup = BeautifulSoup(ar, 'html.parser')
        objek = soup.find('p').get_text()
        deskrip = objek.split('.')
        if len(deskrip[0]) <= 2:
            deskripsi = deskrip[:5]
        else:
            deskripsi = deskrip[0]

        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        time.sleep(2)
        edit = driver.get('https://foloker.com/wp-admin/post.php?post=%s&action=edit'%id_post)
        time.sleep(2)
        if index == 0:
            closee = driver.find_element_by_xpath('/html/body')
            closee.click()
            
        frasa_kunci_utama = driver.find_element_by_xpath('//*[@id="focus-keyword-input-metabox"]')
        frasa_kunci_utama.send_keys("Lowongan Kerja "+title)
        insert_var =  driver.find_element_by_xpath('//*[@id="yoast-google-preview-description-metabox"]')
        insert_var.click()
        insert_var.send_keys(deskripsi)
        perbarui = driver.find_element_by_xpath('//*[@id="editor"]/div/div/div[1]/div/div[1]/div/div[2]/button[2]')
        aw = perbarui.click()
    closing = driver.find_element_by_xpath('/html/body')
    return closing

def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r")
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

tgl = baca_file()
# tgl = "January 6, 2021"
datai = [0,2,3,4,5,6,7,8,9,10,11,12,14]
# for y in list_data:
#     htmll(tgl,y,dataw)
wess = maine(tgl,datai)
wess.click()

# from bs4 import BeautifulSoup, NavigableString, Tag
# URL = 'https://foloker.com/wp-admin'
# # URL = 'https://%s/page/%s/'%(web2,i)
# print ("URL 1 ->",URL)
# time.sleep(1)
# content = requests.get(URL)
# time.sleep(4)
# soup = BeautifulSoup(content.text, 'html.parser')
# objek = soup.find('div')
