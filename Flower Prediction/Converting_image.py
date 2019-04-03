import numpy as np
import pandas as pd
import zipfile
import random
import os
import cv2
from glob import glob
from PIL import Image
import matplotlib.pyplot as plt

#MAKING THE VARIABLES FOR DATASET

labels = []
flowers = []
total = 0

#TAKING OUT THE PATH OF FILE

PATH = os.path.abspath(os.path.join('flowers'))

#IMPORTING DAISIES

print("Importing images of Daisies")
source = os.path.join(PATH,"daisy")
daisy = glob(os.path.join(source,"*.jpg"))
count = 0
for i in range(len(daisy)):
    labels.append(1)
    flowers.append(daisy[i])
    count = count+1
    total+=1

print("No of daisy images are",count)

#IMPORTING DANDELIONS

print("Importing images from Dandelions")
source = os.path.join(PATH,"dandelion")
dandelion = glob(os.path.join(source,"*.jpg"))
count =  0
for i in range(len(dandelion)):
    labels.append(2)
    flowers.append(dandelion[i])
    count+=1
    total+=1
    
print("No of daisy images are",count)    
    
#IMPORTING ROSES

print("Importing images from Roses")
source = os.path.join(PATH,"rose")
rose = glob(os.path.join(source,"*.jpg"))
count =  0
for i in range(len(rose)):
    labels.append(3)
    flowers.append(rose[i])
    count+=1
    total+=1
    
print("No of daisy images are",count)

#IMPORTING SUNFLOWERS

print("Importing images from Sunflowers")
source = os.path.join(PATH,"sunflower")
sunflower = glob(os.path.join(source,"*.jpg"))
count =  0
for i in range(len(sunflower)):
    labels.append(4)
    flowers.append(sunflower[i])
    count+=1
    total+=1
    
print("No of sunflower images are",count)    
        
#IMPORTING TUPILS

print("Importing images from Sunflowers")
source = os.path.join(PATH,"tulip")
tulip = glob(os.path.join(source,"*.jpg"))
count =  0
for i in range(len(tulip)):
    labels.append(5)
    flowers.append(tulip[i])
    count+=1
    total+=1
    
print("No of tulip images are",count)
print("Total number of images are:",total)
               
#NOW CONVERTING IMAGE INTO ARRAY
def proc_img():
    x = [] #images as array
    y = [] #labels of images

    w = 128
    h = 128
    n=0

    for img in flowers:
        base  = os.path.basename(img)

        full_size_image = Image.open(img)
        full_size_image = full_size_image.convert("L")
        reduce_size_image = full_size_image.resize((128,128))
        x.append(np.asarray(reduce_size_image))
        y.append(labels[n])
        n+=1

    return x,y

x,y = proc_img()

print("Saving flower datasets as a NPZ files...")

np.savez("labels", y)    
np.savez("flowers",x)        
























    
