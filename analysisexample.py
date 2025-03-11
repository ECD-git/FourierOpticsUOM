from LatticeAnalysis import imageanalysis as IA
import numpy as np
import matplotlib.pyplot as plt

imagename = "F8 grid no masking.png"
imagedata = IA.openimage(imagename)
# An example slice to show the functionality
IA.displayverticalline(imagedata, 700, norm=True)
latticeconst = IA.getlatticeconst(imagedata, samplesize=5, nohori=True)
