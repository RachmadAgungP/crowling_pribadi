import cv2 
import os,argparse 
import pytesseract 
from PIL import Image 
pytesseract.pytesseract.tesseract_cmd = r"E:/Aplication/tesseract.exe"
#We then Construct an Argument Parser 
img_cv = cv2.imread(r'instagram\2020-12-22_00-14-57_UTC.jpg')

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))
# OR
img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))