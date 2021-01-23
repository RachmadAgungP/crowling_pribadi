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
time.sleep(10)
pos = driver.find_element_by_xpath('//*[@id="menu-posts"]/a/div[3]')
pos.click()
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
edit = driver.get('https://foloker.com/wp-admin/post.php?post=354&action=edit')
closee = driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div/div/div/div/div[1]/button')
closee.click()
frasa_kunci_utama = driver.find_element_by_xpath('//*[@id="focus-keyword-input-metabox"]')
frasa_kunci_utama.send_keys("Lowongan Kerja PT Nestlé Indonesia")
insert_var =  driver.find_element_by_xpath('//*[@id="yoast-google-preview-description-metabox"]')
insert_var.click()
insert_var.send_keys('Nestlé adalah sebuah perusahaan multinternasional di Vevey, Swiss yang bergerak dalam bidang makanan minuman.')
perbarui = driver.find_element_by_xpath('//*[@id="editor"]/div/div/div[1]/div/div[1]/div/div[2]/button[2]')
perbarui.click()

# driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 