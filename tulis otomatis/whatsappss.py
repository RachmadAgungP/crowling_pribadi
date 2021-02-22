from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from ppadb.client import Client as AdbClient
import time
import pandas as pd 
import datetime
import base64
import ast
import pyautogui
import pydirectinput
import random
pyautogui.hotkey('alt', 'tab')
# time.sleep(0.2)
# pyautogui.hotkey('win', 'up')
striny = open("Rancana_web_selanjutnya/Lowongan_Terpadu/Debug/insta/coba_insta.txt", "r")
strin = list(striny.read())
time.sleep(0.1)
# pyautogui.hotkey('ctrl', 'tab')
def writee(strin):
    for y in strin:
        time.sleep(0.02)
        if y == "\n":
            time.sleep(0.01)
            # print (y)from datetime import datetimefrom itertools import dropwhile, takewhile
            # pyautogui.typewrite(y)
            pydirectinput.press("enter")
            time.sleep(0.02)
        else:
            pyautogui.typewrite(y)
            time.sleep(0.01)
            print (y)
    # pyautogui.hotkey('enter')
print (strin)
writee(strin)



# time.sleep(1)
# for y in range(9):
#     print (y)
#     time.sleep(0.1)
#     pyautogui.hotkey('tab')
#     time.sleep(0.1)
# pyautogui.hotkey('enter')

# time.sleep(0.5)
# for y in range(4):
#     print (y)
#     time.sleep(0.1)
#     pyautogui.hotkey('tab')
#     time.sleep(0.1)
# pyautogui.hotkey('enter')
# time.sleep(0.001)
# pyautogui.hotkey('enter')
# writee("highlight")
# pyautogui.hotkey('tab')
# writee("channel")
# pyautogui.hotkey('tab')
# pyautogui.hotkey('tab')
# pyautogui.hotkey('enter')
# writee("highlightchannel171")
# pyautogui.hotkey('tab')
# pyautogui.hotkey('tab')
# writee("agung171")
# pyautogui.hotkey('tab')
# writee("agung171")
# pyautogui.hotkey('tab')
# pyautogui.hotkey('tab')
# pyautogui.hotkey('enter')
# time.sleep(0.5)
# writee("085806677020")
# pyautogui.hotkey('tab')
# pyautogui.hotkey('enter')                               
                
# pyautogui.keyDown('shift') 
# for y in strin:
#      # hold down the shift key
#     pyautogui.press('right') 
#     time.sleep(0.001)    # press the left arrow key    # press the left arrow key
# pyautogui.keyUp('shift') 


    
