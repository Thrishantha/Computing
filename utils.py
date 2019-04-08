# Original source: https://github.com/miguelgfierro/codebase
# Modified by Thrish
import cv2
import matplotlib.pyplot as plt
import numpy as np


def plot_image_matplotlib(img, label):
    """Plot an opencv image using matplotlib.
    Args:
        img (numpy array): An image.
        figsize (tuple): Size of the figure in inches (w,h).
    Examples:
        >>> img = cv2.imread('../../share/Lenna.png')
        >>> plot_image_matplotlib(img)
    """
    shape_len = len(img.shape)
    if shape_len == 3:#color image
        image = img.copy()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        cmap = None
    elif shape_len == 2: #gray image
        image = img
        cmap = 'gray'
    else:
        raise Exception("Wrong image")
    fig, ax = plt.subplots() #Figure handle and the axis handle
    ax.imshow(image, cmap=cmap)
    ax.axis('off')
    if label:
        ax.set_title(label)
    
    plt.show()
    fig.clf()
    ax.cla()
    plt.close()
    
def auto_canny(image, sigma=0.33):
    # compute the median of the single channel pixel intensities
    v = np.median(image)
 
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
 
    # return the edged image
    return edged


