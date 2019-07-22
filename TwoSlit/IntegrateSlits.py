"""
      Porgram simulated imaging slit width. The data is plotted to
      a CSV file and shown as a plot.
"""
from slits import TwoSlits
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import tio as t
import csvfile as csv

wave = 0.65         # Global wavelength
distance = 450.0    # Global distance

def main():
    #     Get the input paramters
    width = t.getFloat("Slit width",0.1)
    separ = t.getFloat("Slit seperation",0.4)
    peak = t.getFloat("Peak",5.0)

    samplestart = t.getFloat("Sample start",2.5)
    sampleend = t.getFloat("Sample end",7.5)
    samples = t.getInt("Samples",50)
    imageSlit = t.getFloat("Image Slit width",0.1)

    #     Make the slit object
    slits = TwoSlits(separ,width,distance,peak,wave)
    
    # sample spacing beteween sample start / end
    xpos = np.linspace(samplestart,sampleend,samples)
    intensity = np.empty(xpos.size)

    #      get intensity through slit for each x
    for i,x in enumerate(xpos):
        a = x - 0.5*imageSlit    # left side of slit
        b = x + 0.5*imageSlit    # righ side of slit
        y,err = quad(slits.getValue,a,b)   # integrate across slit
        intensity[i] = y/imageSlit         # scale output

    out = t.openFile("Output file","w","txt")
    csv.writeCSV(out,[xpos,intensity])

    #    Plot outputs
    plt.plot(xpos,intensity,'o')
    xfine = np.linspace(samplestart,sampleend,500)    # do a fine plot as comparison
    plt.plot(xfine,slits.getArrayValues(xfine))
    plt.ylim(0.0,1.0)

    plt.title("Sample simulation")
    plt.xlabel("X position")
    plt.ylabel("Intensity")
    plt.show()
        
main()   
    
