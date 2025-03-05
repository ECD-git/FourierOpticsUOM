import numpy as np
import scipy as sp
from PIL import Image
import matplotlib.pyplot as plt
import random

def unflatten(array: list, linelength: int):
    '''
    Unflattens a 1D array into a 2d array of width linelength.
    Array length must be some multiple of the line length.
    '''
    height = int(len(array)/linelength)
    if(len(array)%linelength != 0):
        print("ERROR: array is not divisible by line length")
    else:
        result = np.zeros(shape=(height,linelength)) 
        for i in range(height):
            temp = array[linelength*i:linelength*(i+1)]
            #print(temp)
            result[i] = temp
        print("Converted to 2D array of " + str(linelength) + " x " + str(height))
        return result
        
def normalise(array: list):
    '''
    Normalises an array height to have max value at 1.
    '''
    print("Normalising to max value " + str(array.max()))
    return array / array.max()

def sample(data: list, samplesize: int):
    '''
    Returns an array of random x and y values within the bounds of the input array.
    '''
    return random.sample(range(0,data.shape[1]), samplesize), random.sample(range(0,data.shape[0]), samplesize)

def abs2(x):
    return x.real**2 + x.imag**2

def openimage(name: str):
    '''
    Opens an image file, returns a 2D array of pixel intensity data.
    '''
    im = Image.open(name, 'r')
    pix_vals = list(im.getdata(band=1))
    return unflatten(pix_vals,im.width)

def displayhorizontalline(data: list, row: int, norm: bool):
    '''
    Plots a horizontal line segment of the inputted image's intensity.
    Plot can be normalised if norm is set to true.
    '''
    plt.figure(figsize=(15,5))
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
    Plots a vertical line segment of the inputted image's intensity.
    Plot can be normalised if norm is set to true.
    '''
    plt.figure(figsize=(15,5))
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
    Uses the scipi get_peaks function to get the average distance between 2 peaks,
    for periodic input data.
    Indexes and heights of peaks can be returned in full is set to true.
    Warning, untested on not strictly horizontal or vertical data.
    '''
    indexes = sp.signal.find_peaks(inpdata, height=(inpdata.max() - (inpdata.max()-inpdata.min())*0.5, inpdata.max()))
    peaks = inpdata[indexes[0]]
    period = (indexes[0][-1]-indexes[0][0])/len(indexes[0])
    if(full):
        return period, indexes[0], peaks;
    else:
        return period;

def stderrormean(oneDdata: list):
    '''
    Gets the statistical standard error on the mean for an array of floats.
    '''
    temp = np.sum(np.pow(np.mean(oneDdata) - oneDdata, 2))
    temp = np.pow(len(oneDdata)-1, -1, dtype=float)*temp
    return np.pow(temp, 0.5) / np.pow(len(oneDdata), 0.5)
