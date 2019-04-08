#In this code, we will learn how to load and display the layers of an image
import cv2 #This module is needed to process images
import numpy as np #This numerical module is needed to compute with arrays
import matplotlib.pyplot as plt #This module is needed to plot data
from utils import plot_image_matplotlib

class PlayWithImage:
    def __init__ (self,img):
        self.img = img
        self.count = 1

    def ReplacePixels(self):
        layer = self.layer
        ind = np.where(layer > 200) #Obtain all coordinates of pixels greater than this threshold value 
        rows = ind[0] #First argument of ind containing all height coordinates corresponding to this threshold
        cols = ind[1] #Second argument of ind with all width coordinates corresponding to this threshold
        print('How many for simple? ',len(rows))
        layer[rows,cols] = 0
        return layer
    
    def CreativePixels(self): #Now go mad here. Do any creative editing
        #In this function, I will pick pixels of value greater than some threshold
        #And then I will change pixels in its neighborhood by randomly picking them
        layer = self.layer
        S = layer.shape
        ind = np.where(layer > 200) #Obtain all coordinates of pixels greater than this threshold value 
        N = 10 #Neighborhood size
        rows = ind[0] #First argument of ind containing all height coordinates corresponding to this threshold
        cols = ind[1] #Second argument of ind with all width coordinates corresponding to this threshold
        print('How many for creative? ',len(rows))
        
        for i in range(len(rows)):
            r = rows[i]
            c = cols[i]
            if (r < S[0] - N) & (r > N) & (c < S[1] - N) & (c > N): #Do the following only if the pixel is at least N distance within the boundary of the image
                Rpicks = (r + np.random.randint(-N,N,size=N)) #Generate a vector of N random integers around the chosen point
                Cpicks = (c + np.random.randint(-N,N,size=N))
                layer[Rpicks,Cpicks] = 20 #Then I modify the pixels in the choen neighborhood to this value
            
        return layer

    def ModifyImage(self): #Self contains M
        NM = self.img #I assign self.M to M to make things easier for the next steps
        S = NM.shape
        if S[2] == 3:
            for i in range(3):
                self.layer = NM[:,:,i]
                NM[:,:,i] = self.ReplacePixels()
        else:
            self.layer = NM
            NM = self.ReplacePixels()
        self.NM = NM

    def MyCreative(self): #Now go mad here. Do any creative editing
        #In this method, I will pick pixels of value greater than some threshold
        #And then I will change pixels in its neighborhood by randomly picking them
        CM = self.img #I assign self.M to M to make things easier for the next steps
        S = CM.shape
        if S[2] == 3:
            for i in range(3):
                self.layer = CM[:,:,i]
                CM[:,:,i] = self.CreativePixels()
        else:
            self.layer = CM
            CM = self.CreativePixels()
        self.CM = CM

    def plotoriginal(self):
        plot_image_matplotlib(self.img,'Original')

    def plotsimplemodify(self):
        self.ModifyImage()
        plot_image_matplotlib(self.NM,'Simple')
        
    def plotcreativemodify(self):
        self.MyCreative()
        plot_image_matplotlib(self.CM,'Creative')
            
img = cv2.imread('IMG_1562.jpg') #imread is a method in cv2 module to load an image

simple = PlayWithImage(img)
simple.plotoriginal()
simple.plotcreativemodify()
simple.plotsimplemodify()
simple.plotoriginal()



