#In this code, we will learn how to load and display the layers of an image
import cv2 #This module is needed to process images
import numpy as np #This numerical module is needed to compute with arrays
import matplotlib.pyplot as plt #This module is needed to plot data


img = cv2.imread('IMG_1562.jpg') #imread is a method in cv2 module to load an image
S = img.shape #The image is then a Python object. Objects have methods. Shape is one such method
img_copy = img.copy() #You can also use the copy method to make a copy of this image.
print('The original image starts at memory location ',id(img))
print('The copy of img starts at memory location ',id(img_copy)) 
print('The image is of', img.shape ,'shape and has', S[2] ,'layers.') #S[0] is the height in pixels, S[1] is that for width, and S[2] is the number of layers
if S[2] == 3: #If this is a color image
    layer1 = img[:,:,0]
    layer2 = img[:,:,1]
    layer3 = img[:,:,2]
    print('Layer1 is of shape: ',len(layer1.shape))
    plt.figure()
    plt.subplot(2,2,1)
    plt.imshow(layer1,None)# plt.imshow needs two attributes: 1. The pixel array, 2. The color code, in this case "None"
    plt.title('Layer-1')
    plt.subplot(2,2,2)
    plt.imshow(layer2,None)
    plt.title('Layer-2')
    plt.subplot(2,2,3)
    plt.imshow(layer3,None)
    plt.title('Layer-3')
    plt.show()
else:
    plt.figure()
    plt.imshow(img,'gray')# plt.imshow needs two attributes: 1. The pixel array, 2. The color code, in this case "None"
    plt.title('Gray image')

ind = np.where(layer1 > 50) #Now you can use the "where" numpy module method in numpy module to find where pixel values
#greater than 50 are located
print('The x coordinates of the selected pixels: ',ind[0])
print('The y coordinates of the selected pixels: ',ind[1])




