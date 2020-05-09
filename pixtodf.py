import cv2
import os
import numpy as np
import pandas as pd

os.system("cls")

def flattenTheImage(img):
	M = img.shape[0]
	N = img.shape[1]
	imgL = []
	for i in range(M):
		for j in range(N):
			imgL.append(img[i,j])
	return imgL


dim = (5,5)
rootPath = "C:\\Users\\INKOM06\\Pictures\\fontdata\\6\\"
img = cv2.imread(rootPath+"20190509_190049.jpg")
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lst3 = flattenTheImage(img)
lst3.append(0)

img = cv2.imread(rootPath+"20190509_190050.jpg")
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

lst4 = flattenTheImage(img)
lst4.append(0) 

print(lst3)
print(lst4)

lst = []
lst.append(lst3)
lst.append(lst4)

totPix = dim[0]*dim[1]
colLabel = []
for i in range(totPix):
	colLabel.append(str(i))
colLabel.append("Class")
print(colLabel)

df = pd.DataFrame(lst,  columns =colLabel, dtype = int) 
print(df.head()) 
