from bs4 import BeautifulSoup
from mistletoe import markdown
# from html2text import HTML2Text
import _tgl_
import re
tgl = _tgl_.baca_file()

htmls = open("E:/Belajar/www.disnakerja.com/hasil/%s/html/DBC (Djabesmen Co).html"%tgl, "r", encoding='utf-8-sig')
html_ = htmls.read()
htmls.close()
