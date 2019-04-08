#In this code, we will learn how to load and display the layers of an image
import cv2 #This module is needed to process images
import numpy as np #This numerical module is needed to compute with arrays
import matplotlib.pyplot as plt #This module is needed to plot data


img = cv2.imread('IMG_1562.jpg') #imread is a method in cv2 module to load an image
S = img.shape #The image is then a Python object. Objects have attributes. Shape is one such attribute
print('The image is of', img.shape ,'shape and has', S[2] ,'layers.') #S[0] is the height in pixels, S[1] is that for width, and S[2] is the number of layers
if S[2] == 3:
    layer1 = img[:,:,0]
    layer2 = img[:,:,1]
    layer3 = img[:,:,2]
    print(len(layer1.shape))
    ind = np.where(layer1 > 50)
    plt.figure()
    plt.subplot(2,2,1)
    plt.imshow(layer1,None)
    plt.title('Layer-1')
    plt.subplot(2,2,2)
    plt.imshow(layer2,None)
    plt.title('Layer-2')
    plt.subplot(2,2,3)
    plt.imshow(layer3,None)
    plt.title('Layer-3')
    plt.show()

