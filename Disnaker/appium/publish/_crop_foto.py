from PIL import Image 
import cv2
import numpy as np
def save_foto(path_foto):
    img = Image.open(r"%s"%path_foto) 
    img = img.resize((600,300))
    width, height = img.size
    print (width, height)
    img_left_area = (50, 50, width-10, height-10)
    img_left = img.crop(img_left_area)
    img_left.show()
    img_left.save(str(path_foto))
    
