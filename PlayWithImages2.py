#In this code, we will learn how to load and display the layers of an image
import cv2 #This module is needed to process images
import numpy as np #This numerical module is needed to compute with arrays
import matplotlib.pyplot as plt #This module is needed to plot data


img = cv2.imread('IMG_1562.jpg') #imread is a method in cv2 module to load an image
S = img.shape #The image is then a Python object. Objects have attributes. Shape is one such attribute
print('The image is of', img.shape ,'shape and has', S[2] ,'layers.') #S[0] is the height in pixels, S[1] is that for width, and S[2] is the number of layers
#Now let's use a for loop to simplify what we do with layers
L = S[2] #Assign it to another variable for convenience
if L == 3:
    plt.figure()
    for i in range(L):
        layer = img[:,:,i]
        plt.subplot(2,2,i+1) #This is because i starts with 0.
        plt.imshow(layer,None)
        plt.title(['Layer-',i])

    plt.show()
