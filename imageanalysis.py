import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

def unflatten(array, linelength):
    height = int(len(array)/linelength)
    if(len(array)%linelength != 0):
        print("ERROR, array is not divisible by line length")
    else:
        result = np.zeros(shape=(height,linelength)) 
        for i in range(height):
            temp = array[linelength*i:linelength*(i+1)]
            #print(temp)
            result[i] = temp
        print("Converted to 2D array of " + str(linelength) + " x " + str(height))
        return result
        
def normalise(array):
    print("Normalising to max value " + str(array.max()))
    return array / array.max()

def sample(data, samplesize):
    return random.sample(range(0,data.shape[0]), samplesize), random.sample(range(0,data.shape[1]), samplesize)

def abs2(x):
    return x.real**2 + x.imag**2

def openimage(name):
    im = Image.open(name, 'r')
    pix_vals = list(im.getdata(band=1))
    return unflatten(pix_vals,im.width)

def displayhorizontalline(data, row, norm):
    fig = plt.figure(figsize=(10,5))
    if(row > data.shape[1]):
        print("ERROR: line out of image range")
    else:
        if(norm):
            plt.plot(normalise(data[row,:]))
        else:
            plt.plot(data[row,:])
        plt.show()

def displayverticalline(data, colm, norm):
    fig = plt.figure(figsize=(10,5))
    if(colm > data.shape[0]):
        print("ERROR: line out of image range")
    else:
        if(norm):
            plt.plot(normalise(data[:,colm]))
        else:
            plt.plot(data[:,colm])
        plt.show()
    
# iamge name
#imgName = "5.3.2.3[144].png"
# convert to intensity data
#data = openimage(imgName)

# plot - TEST
#displayhorizontalline(data, 0, True)
#displayverticalline(data, 20, True)

# choose random sample set of columns + rows
#rows, colms = sample(data, 5)

# fourier transform and observe
#yf = np.fft.rfft(data[0]-np.mean(data[0]), norm="ortho")
#selfconvol = np.fft.irfft(abs2(yf), norm="ortho")
#mask = abs(selfconvol) > 0.5*selfconvol.max()

#fig = plt.figure(figsize=(10,5))
#plt.plot(abs(selfconvol))
#plt.show()
# average lattice consts in pixels
