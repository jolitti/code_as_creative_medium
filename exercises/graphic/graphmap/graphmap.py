import numpy as np
from PIL import Image, ImageOps
import sys
from matplotlib import pyplot as plt

import cv2

# USAGE: python3.10 graphmap.py [name of folder with "input.jpg"]

#---------------------------------



#---------------------------------

def main():
    THRESHOLD = 200
    #folder = sys.argv[1]
    #input_path = folder + "/input.jpg"
    #img = Image.open(input_path)
    #img = ImageOps.grayscale(img)
    #imgarray = np.asarray(img)
    #pixels =  (imgarray < THRESHOLD) * np.ones(imgarray.shape)
    #print(pixels)

    input_path = sys.argv[1] + "/input.jpg"
    img = cv2.imread(input_path,0)
    # print(img)
    newthresh,img = cv2.threshold(img,THRESHOLD,255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)
    # print(newthresh)
    # print(img)

    area_lower_bound = 2
    contours = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    for c in contours[0]:
        c = c[:,0,:]
        print(c.shape)
        print(c)
        
        x,y = zip(*c)
        plt.plot(x,y)
        print("---")
    plt.show()
#---------------------------------

if __name__ == "__main__": main()
