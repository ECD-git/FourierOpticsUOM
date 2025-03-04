import numpy as np
import scipy as sp
from PIL import Image
import matplotlib.pyplot as plt
import random

def unflatten(array, linelength):
    '''
    '''
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
    '''
    '''
    print("Normalising to max value " + str(array.max()))
    return array / array.max()

def sample(data, samplesize):
    '''
    '''
    return random.sample(range(0,data.shape[1]), samplesize), random.sample(range(0,data.shape[0]), samplesize)

def abs2(x):
    '''
    '''
    return x.real**2 + x.imag**2

def openimage(name: str):
    '''
    '''
    im = Image.open(name, 'r')
    pix_vals = list(im.getdata(band=1))
    return unflatten(pix_vals,im.width)

def displayhorizontalline(data: list, row: int, norm: bool):
    '''
    '''
    fig = plt.figure(figsize=(15,5))
    if(row > data.shape[1]):
        print("ERROR: line out of image range")
    else:
        if(norm):
            plt.plot(normalise(data[row,:]))
        else:
            plt.plot(data[row,:])
        plt.show()

def displayverticalline(data: list, colm: int, norm: bool):
    '''
    '''
    fig = plt.figure(figsize=(15,5))
    if(colm > data.shape[0]):
        print("ERROR: line out of image range")
    else:
        if(norm):
            plt.plot(normalise(data[:,colm])-np.mean(normalise(data[:,colm])))
        else:
            plt.plot(data[:,colm])
        plt.show()
    
def get_period(inpdata: list, full: bool):
    '''
    Warning, untested on not strictly horizontal or vertical data
    '''
    indexes = sp.signal.find_peaks(inpdata, height=(inpdata.max() - (inpdata.max()-inpdata.min())*0.5, inpdata.max()))
    peaks = inpdata[indexes[0]]
    period = (indexes[0][-1]-indexes[0][0])/len(indexes[0])
    if(full):
        return period, indexes[0], peaks;
    else:
        return period;

def stderrormean(oneDdata):
    temp = np.sum(np.pow(np.mean(oneDdata) - oneDdata, 2))
    temp = np.pow(len(oneDdata)-1, -1, dtype=float)*temp
    return np.pow(temp, 0.5) / np.pow(len(oneDdata), 0.5)
