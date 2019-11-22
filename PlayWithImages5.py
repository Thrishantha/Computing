#In this code, we will learn how to load and display the layers of an image
import cv2 #This module is needed to process images
import numpy as np #This numerical module is needed to compute with arrays
import matplotlib.pyplot as plt #This module is needed to plot data
from utils import plot_image_matplotlib

class PlayWithImage:
    def __init__ (self,img):
        self.img = img
        self.count = 1

    def ReplacePixels(layer):
        ind = np.where(layer > 200) #Obtain all coordinates of pixels greater than this threshold value 
        rows = ind[0] #First argument of ind containing all height coordinates corresponding to this threshold
        cols = ind[1] #Second argument of ind with all width coordinates corresponding to this threshold
        print('How many pixels? ',len(rows))
        layer[rows,cols] = 0
        return layer
    
    def CreativePixels(layer): #Now go mad here. Do any creative editing
        #In this function, I will pick pixels of value greater than some threshold
        #And then I will change pixels in its neighborhood by randomly picking them
        S = layer.shape
        ind = np.where(layer > 200) #Obtain all coordinates of pixels greater than this threshold value 
        N = 10 #Neighborhood size
        rows = ind[0] #First argument of ind containing all height coordinates corresponding to this threshold
        cols = ind[1] #Second argument of ind with all width coordinates corresponding to this threshold
        print('How many pixels for creative? ',len(rows))
        
        for i in range(len(rows)):
            r = rows[i]
            c = cols[i]
            if (r < S[0] - N) & (r > N) & (c < S[1] - N) & (c > N): #Do the following only if the pixel is at least N distance within the boundary of the image
                Rpicks = (r + np.random.randint(-N,N,size=N)) #Generate a vector of N random integers around the chosen point
                Cpicks = (c + np.random.randint(-N,N,size=N))
                layer[Rpicks,Cpicks] = 20 #Then I modify the pixels in the choen neighborhood to this value
            
        return layer

    def ModifyImage(self,M): #Self contains M
        #NM = self.img #I assign self.M to M to make things easier for the next steps
        NM = M.copy()
        S = NM.shape
        if S[2] == 3:
            for i in range(3):
                layer = NM[:,:,i]
                NM[:,:,i] = PlayWithImage.ReplacePixels(layer)
        else:
            layer = NM
            NM = PlayWithImage.ReplacePixels(layer)
        self.NM = NM

    def MyCreative(self,M): #Now go mad here. Do any creative editing
        #In this method, I will pick pixels of value greater than some threshold
        #And then I will change pixels in its neighborhood by randomly picking them
        #CM = self.img #I assign self.M to M to make things easier for the next steps
        CM = M.copy()
        S = CM.shape
        if S[2] == 3:
            for i in range(3):
                layer = CM[:,:,i]
                CM[:,:,i] = PlayWithImage.CreativePixels(layer)
        else:
            layer = CM
            CM = PlayWithImage.CreativePixels(layer)
        self.CM = CM

    def plotoriginal(self,img):
        plot_image_matplotlib(img,'Original')

    def plotsimplemodify(self,img):
        self.ModifyImage(img)
        plot_image_matplotlib(self.NM,'Simple')
        
    def plotcreativemodify(self,img):
        self.MyCreative(img)
        plot_image_matplotlib(self.CM,'Creative')
            
photo = cv2.imread('amma.jpg') #imread is a method in cv2 module to load an image

simple = PlayWithImage(photo)

simple.plotoriginal(photo)
simple.plotcreativemodify(photo)
simple.plotsimplemodify(photo)
simple.plotoriginal(photo)
plt.show()


