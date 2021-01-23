import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"E:/Aplication/tesseract.exe"
image = cv2.imread('instagram\2020-12-22_02-29-08_UTC_1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 255 - cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Blur and perform text extraction
thresh = cv2.GaussianBlur(thresh, (3,3), 0)
data = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')
t = data.split('\n')
angka = []

print (angka)
print (t)


# cv2.imshow('thresh', thresh)
# cv2.waitKey()