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

def MyCreative(M): #Now go mad here. Do any creative editing
    #In this function, I will pick pixels of value greater than some threshold
    #And then I will change pixels in its neighborhood by randomly picking them
    S = M.shape
    ind = np.where(M > 240) #Obtain all coordinates of pixels greater than this threshold value 
    N = 10 #Neighborhood size
    rows = ind[0] #First argument of ind containing all height coordinates corresponding to this threshold
    cols = ind[1] #Second argument of ind with all width coordinates corresponding to this threshold
    print('How many? ',len(rows))
    NewM = M
    for i in range(len(rows)):
        r = rows[i] #Pick a row
        c = cols[i] #Pick a column
        if (r < S[0] - N) & (r > N) & (c < S[1] - N) & (c > N): #Do the following only if the pixel is at least N distance within the boundary of the image
            Rpicks = (r + np.random.randint(-N,N,size=N)) #Generate a vector of N random integers around the chosen point
            Cpicks = (c + np.random.randint(-N,N,size=N))
            NewM[Rpicks,Cpicks] = 20 #Then I modify the pixels in the choen neighborhood to this value
    return NewM

img = cv2.imread('IMG_1562.jpg') #imread is a method in cv2 module to load an image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert to a gray image
S = img_gray.shape #The image is then a Python object. Objects have attributes. Shape is one such attribute
print('The image is of', S,' shape.')
#print('The image is of', img.shape ,'shape and has', S[2] ,'layers.') #S[0] is the height in pixels, S[1] is that for width, and S[2] is the number of layers
#Now let's use a for loop to simplify what we do with layers
if len(S) == 3: #Check if it is a color image
    L = S[2] #Assign it to another variable for convenience
else:
    L = 0
    print('The image has less than 3 layers, possibly gray scale')

if L == 3:
    plt.figure()
    for i in range(L):
        layer = img[:,:,i]
        modifiedLayer = MyCreative(layer)
        plt.subplot(2,2,i+1) #This is because i starts with 0.
        plt.imshow(modifiedLayer,None)
        plt.title(['Layer-',i])
else:
    plt.figure()
    layer = img[:,:]
    plt.subplot(2,2,1) #This is because i starts with 0.
    plt.imshow(layer,None)
    plt.title(['Unedited'])

    modifiedLayer = MyCreative(layer)
    plt.subplot(2,2,2) #This is because i starts with 0.
    plt.imshow(modifiedLayer,None)
    plt.title(['Edited'])
    plt.show()


