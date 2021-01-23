import pyautogui
import time

# groups = ['122338368492875']
pyautogui.hotkey('win', '5')
# find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
time.sleep(1)
pyautogui.typewrite("paraphrasing-tool.com")
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
time.sleep(5)
# pyautogui.keyDown('ctrl')
# for i in range(3):
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyDown('enter')
pyautogui.keyUp('enter')
time.sleep(5)
for i in range(3):
    pyautogui.keyDown('tab')
    pyautogui.keyUp('tab')
pyautogui.keyDown('enter')  
pyautogui.keyUp('enter')
time.sleep(5)   
pyautogui.typewrite("aku adalah anak yang baik")
time.sleep(5)
pyautogui.keyDown('tab')
pyautogui.keyUp('tab')
pyautogui.keyDown('enter')  
pyautogui.keyUp('enter')
time.sleep(5)
# pyautogui.keyUp('aku adalah anak yang baikt')          
# pyautogui.keyUp('ctrl')
# "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div[1]/div[1]/div/div/div/div[1]/div"

# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys

# USERNAME = 'lowongankerja171@gmail.com'
# PASSWORD = 'AGUNG19541'

# driver = webdriver.Chrome('chromedriver.exe')
# driver.get('https://paraphrasing-tool.com/')
# driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]').click()
# for i in range(len(groups)):
#     link = 'https://facebook.com/groups/'+groups[i]
#     pyautogui.typewrite(link)
#     pyautogui.typewrite('\n')

#     print("Waiting for 45 seconds\n")
#     time.sleep(45)

#     pyautogui.typewrite('p')
#     time.sleep(2)
#     print("Writing post\n")
#     pyautogui.typewrite("Hello there, it's a testing post from messy programmers")
#     time.sleep(4)

#     # pyautogui.keyDown('ctrl')
#     # pyautogui.keyDown('enter')
#     # pyautogui.keyUp('enter')
#     # pyautogui.keyUp('ctrl')

#     # time.sleep(3)

#     # pyautogui.write(['f6'])
#     # time.sleep(1)