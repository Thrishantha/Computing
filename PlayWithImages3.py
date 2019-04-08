#In this code, we will learn how to load and display the layers of an image
import cv2 #This module is needed to process images
import numpy as np #This numerical module is needed to compute with arrays
import matplotlib.pyplot as plt #This module is needed to plot data

def ModifyImage(M):
    ind = np.where(M > 200) #Obtain all coordinates of pixels greater than this threshold value 
    rows = ind[0] #First argument of ind containing all height coordinates corresponding to this threshold
    cols = ind[1] #Second argument of ind with all width coordinates corresponding to this threshold
    print('How many? ',len(rows))
    NewM = M
    NewM[rows,cols] = 0
    return NewM


img = cv2.imread('IMG_1562.jpg') #imread is a method in cv2 module to load an image
S = img.shape #The image is then a Python object. Objects have attributes. Shape is one such attribute
print('The image is of', img.shape ,'shape and has', S[2] ,'layers.') #S[0] is the height in pixels, S[1] is that for width, and S[2] is the number of layers
#Now let's use a for loop to simplify what we do with layers
L = S[2] #Assign it to another variable for convenience
if L == 3:
    plt.figure()
    for i in range(L):
        layer = img[:,:,i]
        modifiedLayer = ModifyImage(layer)
        plt.subplot(2,2,i+1) #This is because i starts with 0.
        plt.imshow(modifiedLayer,None)
        plt.title(['Layer-',i])

    plt.show()


