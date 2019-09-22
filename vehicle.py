import pytesseract
import urllib
import cv2
import json
import numpy as np
import pandas as pd
from PIL import Image
from pytesseract import image_to_string


List = pd.read_json('Indian_Number_plates.json', lines=True)
pd.set_option('display.max_colwidth', -1)
del List['extras']
List['points'] = List.apply(lambda Row: Row['annotation'][0]['points'], axis=1)
del List['annotation']
#ExtractNumbers(List)
Images =[]
Plates =[] 
Numbers=[] 
#def ExtractNumbers(List):
for index,Row in List.iterrows():
    ResponAse = urllib.request.urlopen(Row[0])
    Img = np.array(Image.open(Response))
    Images.append(Img)
    xt = Row[1][0]['x']*Img.shape[1]
    yt = Row[1][0]['y']*Img.shape[0]
    xb = Row[1][1]['x']*Img.shape[1]
    yb = Row[1][1]['y']*Img.shape[0]
    fullImage = Image.fromarray(Img)
    plateImage = fullImage.crop((xt, yt, xb, yb))
    Plates.append(np.array(plateImage))
    plateImage.save('image.png')
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    img = cv2.imread('image.png')
    img = cv2.resize(img, (int(img.shape[1]*4), int(img.shape[0]*4)))
    Num = pytesseract.image_to_string(img)
    print(Num)
    Numbers.append(Num)
    
    f = open('num.txt','a')
    f.write('\n'+Num)
    f.close()
    #img = Image.open('image.png')
    #txt=pytesseract.image_to_string(img, lang='eng')
    #print(txt)
