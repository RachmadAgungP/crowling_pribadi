from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from ppadb.client import Client as AdbClient
import time
import pandas as pd 
import datetime
import base64
import ast
import pyautogui
import time

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
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554")

now = datetime.datetime.now()
tgl = str(now.strftime("%B %d, %Y"))
tgl = "December 31, 2020"

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

def proses_file(z,pilihan_menu):
    numbers = nama_foto[i].strip('][').split(', ')
    numbers.sort() 
    j = numbers[-1]
    # for j in numbers:
    time.sleep(5)
    nama_file_from_pc = "E:\Belajar\www.disnakerja.com\hasil\%s\%s\%s.jpg"%(tgl,z,j)
    nama_file_from_emulator =  "/mnt/sdcard/DCIM/100ANDRO/%s.jpg"%j
    if pilihan_menu == "tambah":
        tambah_file = device.push(nama_file_from_pc, nama_file_from_emulator)
        device.shell("am broadcast \
                    -a android.intent.action.MEDIA_SCANNER_SCAN_FILE \
                    -d file:/mnt/sdcard/DCIM/100ANDRO/")
    else:
        hapus_file = device.shell("rm -f %s"%nama_file_from_emulator)

driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
r = 0

# for i in nama_perusahaan:
i = 2

# proses_file(str(i)+". "+nama_perusahaan[i],"hapus")
time.sleep(2)
print ("--> data %s <--"%nama_perusahaan[i])
print ("-->> tambah file ... ")
# proses_file(str(i+" "+nama_perusahaan[i]),"tambah")
proses_file(str(i)+". "+str(nama_perusahaan[i]),"tambah")
print ("-->> Open IG ... ")

open_IG = driver.start_activity("com.instagram.android", "com.instagram.mainactivity.MainActivity");
time.sleep(2)
print ("-->> + upload file 1 ... ")
open_IG.find_element_by_xpath('//android.widget.Button[@content-desc="Camera"]').click()

print ("-->> checklist slideout ... ")
open_IG.find_element_by_id('com.instagram.android:id/slideout_iconview_icon').click()
print ("-->> checklist photo ... ")
# x=41
# y=441
# x += 82
# print ("----- ",x,y)
# time.sleep(3)
# open_IG.implicitly_wait(30)
# TouchAction(open_IG).tap(x=x, y=y).perform()
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
proses_file(i,str(i)+". "+nama_perusahaan[i],"hapus")
# proses_file(str(i+" "+nama_perusahaan[i]),"hapus")
time.sleep(2)
r+=1


