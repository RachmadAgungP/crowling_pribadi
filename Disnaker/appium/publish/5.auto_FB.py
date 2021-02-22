import pyautogui
import time

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import _tgl_
import pyautogui
USERNAME = 'lowongankerja171@gmail.com'
PASSWORD = 'AGUNG19541'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://facebook.com/')

user_input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input')
user_input.send_keys(USERNAME)
password_input = driver.find_element_by_xpath('//*[@id="pass"]')
password_input.send_keys(PASSWORD)
LOGIN = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
LOGIN.click()
group = ["366680916822092","lowongankerjaterbarusurabaya","1406139939706044","250024915122114"]
# "122338368492875",
for p in range(len(group)):
    time.sleep(2)
    driver.get('https://facebook.com/groups/%s'%group[p])
    time.sleep(4)
    if p == 0:
        print ("0")
        pyautogui.hotkey('tab')
        time.sleep(2)
        pyautogui.hotkey('tab')
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(2)
    tgl = _tgl_.baca_file()
    nama_folder_foto = _tgl_.data_proses_foto(tgl)[0]
    nama_foto = _tgl_.data_proses_foto(tgl)[1]
    nama_text = _tgl_.data_proses_text(tgl)[1]
    # folder = []
    # for yo in range(len(nama_foto)):
    #     nama = []
    #     for yi in nama_foto[yo]:
    #         nama.append("E:/Belajar/www.disnakerja.com/hasil/%s/%s/%s"%(tgl,nama_folder_foto[yo],yi))
    #     folder.append(nama)
    folder = []
    for yo in range(len(nama_text)):
        nama = []
        # for yi in nama_foto[yo]:
        folder.append(open("E:/Belajar/www.disnakerja.com/hasil/%s/text/%s"%(tgl,nama_text[yo]), "r", encoding='utf-8-sig').read())
        # folder.append(nama)

    files = folder
    for pos in files:
        klik_foto = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/span').click()
        time.sleep(5)
        pyautogui.typewrite(pos)
        # klik_foto.execute_script("document.getElementsByXpath('//*[@id='mount_0_0']/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div/div/div/span/span').value='%s'"%pos)
        # tt = len(pos)-1
        # for t in range(len(pos)):
        #     if t == 0:
        #         klik_foto.send_keys(pos[tt-t])
        #         time.sleep(3)
        #     else:
        #         klik_foto2 = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]/div[1]/input')
        #         klik_foto2.send_keys(pos[tt-t])
        #         time.sleep(2)
        posting = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/form/div/div[1]/div/div/div[1]/div[3]/div[2]/div/div')
        posting.click()
        # time.sleep(6)
        time.sleep(30)
