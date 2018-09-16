import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from tqdm import tqdm
import random
import pickle

DIR=r"G:\Proj\DataCoC"                                      #set the directory
CATEGORIES = ["Nut", "NotNut"]                          #define the categories
IMG_SIZE=ArithmeticError                #define final image sizze
training_data=[]

def create_training_data(training_data):                    #create our image set function
    IMG_SIZE=100
    for category in CATEGORIES:
        path=os.path.join(DIR, category)
        class_num = CATEGORIES.index(category)

        for img in tqdm(os.listdir(path)):
            try:
                img_array=cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)      #convert to grayscale
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))                 #resize to 100x100
                training_data.append([new_array, class_num])                #add to list, both image data and the feature_labels
            except Exception as e:
                print(e)
    return training_data

training_data=create_training_data(training_data)

#print(len(training_data))

random.shuffle(training_data)                       #shuffle the data

#for sample in training_data[:10]:
    #print(sample[1])

X = []
y = []

for features,label in training_data:       #create the feature and outputs     
    X.append(features)
    y.append(label)

print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)              #reshape to flat


pickle_out = open("X.pickle","wb")          #create dataset
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()



'''
#Load the dataset!

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle","rb")
y = pickle.load(pickle_in)


''''''
