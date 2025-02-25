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
    
# iamge name
imgName = "5.3.2.3[144].png"
# convert to intensity data
im = Image.open(imgName, 'r')
pix_vals = list(im.getdata(band=1))
data = normalise(unflatten(pix_vals,1440))
# plot
fig = plt.figure(figsize=(10,5))
plt.plot(np.linspace(0,1440,1440), data[0])
plt.show()


# choose random sample set of columns + rows
rows, colms = sample(data, 5)

# fourier transform and observe
yf = np.fft.rfft(data[0]-np.mean(data[0]), norm="ortho")
selfconvol = np.fft.irfft(abs2(yf), norm="ortho")
mask = abs(selfconvol) > 0.5*selfconvol.max()

fig = plt.figure(figsize=(10,5))
plt.plot(abs(selfconvol))
plt.show()
# average lattice consts in pixels
