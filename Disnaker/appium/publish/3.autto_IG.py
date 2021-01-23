from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from ppadb.client import Client as AdbClient
import time
import pandas as pd 
import datetime
import base64
import ast
import pyautogui
import random
# # buka android 
# pyautogui.hotkey('win', '2')
# time.sleep(2)
# pyautogui.typewrite("D:")
# time.sleep(2)
# pyautogui.hotkey('enter')
# time.sleep(2)
# pyautogui.typewrite("cd D:/android/emulator ")
# time.sleep(2)
# pyautogui.hotkey('enter')
# time.sleep(2)
# pyautogui.typewrite("emulator -avd test_avd_29")
# time.sleep(2)
# pyautogui.hotkey('enter')
# time.sleep(10)
# # buka apium 
# pyautogui.hotkey('win', '1')
# time.sleep(10)
# pyautogui.click(967, 706)
# time.sleep(2)
# pyautogui.click(967, 706)
# time.sleep(2)
# pyautogui.click(506, 130 )
# time.sleep(2)
# pyautogui.click(638, 292 )
# time.sleep(2)
# pyautogui.click(513, 567 )
# time.sleep(12)
# pyautogui.click(322, 749 )
# time.sleep(2)
# pyautogui.click(1670, 897 )
# time.sleep(10)

# Default is "127.0.0.1" and 5037

def proses_file(i,z,pilihan_menu,nama_foto,device):
    print (nama_foto[i])
    numbers = nama_foto[i].strip('][').split(', ')
    numbers.sort() 

    for j in numbers:
        time.sleep(3)
        nama_file_from_pc = "E:\Belajar\www.disnakerja.com\hasil\%s\%s\%s.jpg"%(tgl,z,j)
        nama_file_from_emulator =  "/mnt/sdcard/DCIM/100ANDRO/%s.jpg"%j
        if pilihan_menu == "tambah":
            tambah_file = device.push(nama_file_from_pc, nama_file_from_emulator)
            device.shell("am broadcast \
                        -a android.intent.action.MEDIA_SCANNER_SCAN_FILE \
                        -d file:/mnt/sdcard/DCIM/100ANDRO/")
        else:
            hapus_file = device.shell("rm -f %s"%nama_file_from_emulator)

def feed(i,r,nama_foto,nama_perusahaan,device,driver,banyak_foto,info):
    print ("--> data %s <--"%nama_perusahaan[i])
    print ("-->> tambah file ... ")
    proses_file(i,str(i)+". "+str(nama_perusahaan[i]),"tambah",nama_foto,device)
    print ("-->> Open IG ... ")

    open_IG = driver.start_activity("com.instagram.android", "com.instagram.mainactivity.MainActivity")
    time.sleep(2)
    open_IG.implicitly_wait(30)
    print ("-->> + upload file 1 ... ")
    open_IG.find_element_by_xpath('//android.widget.Button[@content-desc="Camera"]').click()
    open_IG.implicitly_wait(30)
    print ("-->> checklist slideout ... ")
    open_IG.find_element_by_id('com.instagram.android:id/slideout_iconview_icon').click()
    print ("-->> checklist photo ... ")
    x=41
    y=441+40
    for j in range(1,int(banyak_foto[i])+1):
        if j >= 10:
            pass
        elif j == 10 or j == 11 or j == 12:
            pass
        else:
            print (banyak_foto[i])
            if j%4 == 0:
                y += 42
                x = 41
                print("---->> y",j)
            else:
                print("---->> x",j)
                x += 82
                print ("----- ",x,y)
        time.sleep(3)
        open_IG.implicitly_wait(30)
        TouchAction(open_IG).tap(x=x, y=y).perform()
    print("-->> Next.. ")
    open_IG.find_element_by_id('com.instagram.android:id/next_button_imageview').click()
    time.sleep(3)
    print("-->> Next... ")
    open_IG.find_element_by_id('com.instagram.android:id/next_button_imageview').click()
    print("-->> Caption Click.. ")
    captions = open_IG.find_element_by_id('com.instagram.android:id/caption_text_view')
    print("-->> Caption Write.. ")
    captions.send_keys(str(info[i])+" \n \n #lowongankerja #lowongan #loker #lokerja #lowonganbumn #lowongancpns #lowonganpekerjaan #kerja #lokerjawatimur #lokersumatra #lokerjawa #lokermadura #lokerbali #lokerkalimantan #lokersulawesi #lokermaluku #lokerpapua #Karir #jobstreet #disnaker #jobs #klob #lokersurabaya #lokerjakarta #lokerjogja")
    time.sleep(5)
    print("-->> Next... ")
    open_IG.find_element_by_id('com.instagram.android:id/next_button_imageview').click()
    print("-->> Close App IG ... ")
    open_IG.close_app()
    print("-->> Hapus File ... ")
    time.sleep(5)
    proses_file(i,str(i)+". "+nama_perusahaan[i],"hapus",nama_foto,device)
    time.sleep(2)

def ad_story(v,pilihan_menu,device):
    nama_file_from_pc = "E:\Belajar\www.disnakerja.com\hasil\%s\%s\%s.jpg"%(tgl,"story",v)
    nama_file_from_emulator =  "/mnt/sdcard/DCIM/100ANDRO/%s.jpg"%v
    if pilihan_menu == "tambah":
        tambah_file = device.push(nama_file_from_pc, nama_file_from_emulator)
        device.shell("am broadcast \
                    -a android.intent.action.MEDIA_SCANNER_SCAN_FILE \
                    -d file:/mnt/sdcard/DCIM/100ANDRO/")
    else:
        hapus_file = device.shell("rm -f %s"%nama_file_from_emulator)

def story(upp,device,driver):
    for v in upp:
        ad_story(v,"tambah",device)
    open_IG = driver.start_activity("com.instagram.android", "com.instagram.mainactivity.MainActivity")
    time.sleep(4)
    open_IG.implicitly_wait(30)
    print ("-->> + upload file 1 ... ")
    open_IG.find_element_by_xpath('//android.widget.Button[@content-desc="Camera"]').click()
    open_IG.implicitly_wait(30)
    print ("-->> checklist slideout ... ")
    TouchAction(open_IG).tap(x=223, y=607).perform()
    # open_IG.find_element_by_id('com.instagram.android:id/dial_ar_effect_picker_right_side_button_container').click()
    open_IG.find_element_by_id('com.instagram.android:id/gallery_preview_button').click()
    open_IG.find_element_by_id('com.instagram.android:id/gallery_multi_select_button').click()
    time.sleep(2)
    x=52
    y=181
    for j in range(1,len(upp)+1):
        if j >= 9:
            pass
        elif j == 10 or j == 11 or j == 12:
            pass
        else:
            if j == 1:
                x = 52
            elif j%4 == 0:
                y += 181
                x = 52
                print("---->> y",j)
            else:
                print("---->> x",j)
                x += 104
                print ("----- ",x,y)
        time.sleep(3)
        open_IG.implicitly_wait(30)
        TouchAction(open_IG).tap(x=x, y=y).perform()
    time.sleep(3)
    open_IG.find_element_by_id('com.instagram.android:id/media_thumbnail_tray_button_text').click()
    time.sleep(1)
    open_IG.find_element_by_id('com.instagram.android:id/media_thumbnail_tray_button_text').click()
    time.sleep(1)
    open_IG.find_element_by_xpath('//android.widget.Button[@content-desc="Share to Your Story"]/android.widget.FrameLayout').click()
    time.sleep(5)
    for v in upp:
        ad_story(v,"hapus",device)

def mainee(tgl,uppy,tipe_upload):
    upp = random.sample(uppy,len(uppy))
    client = AdbClient(host="127.0.0.1", port=5037)
    device = client.device("emulator-5554")

    data_loker = pd.read_csv("hasil\%s\data_fix.csv"%tgl)
    nama_perusahaan = data_loker['Nama']
    nama_foto = data_loker['nama_nomer']
    print(nama_foto)
    banyak_foto = data_loker['byk_hasil']
    info = data_loker['info']

    desired_cap ={
        "deviceName":"Android Emulator",
        "platformName":"Android",
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
    r = 0
    if tipe_upload == "feed":
        for i in upp:
            feed(i,r,nama_foto,nama_perusahaan,device,driver,banyak_foto,info)
            r+=1
    else:
        story(upp,device,driver)

# now = datetime.datetime.now()
# tgl = str(now.strftime("%B %d, %Y"))

def baca_file():
    tgl_r = open("E:/Belajar/www.disnakerja.com/Data/tanggal.txt", "r")
    tgl = tgl_r.read()
    tgl_r.close()
    return tgl

tgl = baca_file()

upp = [1,2,3,4,5]
tipe_upload = "story"
mainee(tgl,upp,tipe_upload)