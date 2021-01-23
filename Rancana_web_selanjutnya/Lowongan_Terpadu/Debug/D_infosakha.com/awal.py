from bs4 import BeautifulSoup, NavigableString, Tag # BeautifulSoup is in bs4 package
import requests
import re 
import string
import time
import pandas as pd
import datetime
import urllib.request
import os
import time
import sys

now = datetime.datetime.now()
tgl = now.strftime("%B %d, %Y")
# "November 19, 2020"
tgl = "December 23, 2020"
tgl_post = tgl.split()
tgl = "24/12/2020"
URL = "https://infosakha.com/"

def prasyaratan(objek):

print ("URL 1 ->",URL)
time.sleep(1)
content = requests.get(URL)
time.sleep(1)
soup = BeautifulSoup(content.text, 'html.parser')
objek = soup.find("div",{"class":'content-area'})

tglan = [artikel.get_text() for artikel in objek.find_all("span",{"class":"post-date"}) if artikel.get_text() == tgl]
link = [artikel.get("href") for artikel in objek.find_all(True) if artikel.name == "a" and artikel.next_element.next_element.name == "h2"][:len(tglan)]
judul = [artikel.get_text() for artikel in objek.find_all("h2",{"class":"post-title"})][:len(tglan)]
print ("link ="+ str(link))
print ("judul ="+ str(judul))
# for i in link:
URL1 = "https://infosakha.com/lowongan-kerja-pt-pp-properti-tbk/"
content = requests.get(URL1)
time.sleep(4)
soup = BeautifulSoup(content.text, 'html.parser')

prasyaratan(objek)
