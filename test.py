import numpy
import matplotlib.pyplot as plt
import cv2
import os

DIR=r"G:\Proj\Data"
CATEGORIES = ["Nut", "NotNut"]

for category in CATEGORIES:
    path = os.path.join(DIR, category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        #plt.imshow(img_array, cmap='gray')
        #plt.show()
        #print(os.path.join(path,img))
        #print(img_array.shape)
        IMG_SIZE=100
        #new_array=cv2.resize(img_array, (IMG_SIZE,IMG_SIZE))
        #plt.imshow(new_array, cmap='gray')
        #plt.show()
        #print(new_array.shape)

training_data=[]

def create_training_data():
    for category in CATEGORIES:
        path=os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)

    for img in tqdm(os.listdir(path))):
        try:
            img_array=cv2.imread(os.path,join(path,img), cv2.IMREAD_GRAYSCALE)
             new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
