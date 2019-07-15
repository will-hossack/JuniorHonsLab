"""
      Porgram simulated imaging slit width.
"""
from slits import TwoSlits
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import tio as t

wave = 0.65     # Global wavelength

def main():
    #     Get the input paramters
    
    width = t.getFloat("Slit width",0.1)
    separ = t.getFloat("Slit seperation",0.4)
    distance = t.getFloat("Distance",450)
    samples = t.getInt("Samples",50)
    imageSlit = t.getFloat("Image Slit width",0.1)

    #     Make the slit object
    slits = TwoSlits(separ,width,distance,wave)
    
    # sampl;e spacing bete=ween +/- 3 mm
    xpos = np.linspace(-3,3,samples)
    yvals = np.empty(xpos.size)

    #      get intensity through slit for each x
    for i,x in enumerate(xpos):
        a = x - 0.5*imageSlit    # left side of slit
        b = x + 0.5*imageSlit    # righ side of slit
        y,err = quad(slits.getValue,a,b)   # integrate across slit
        yvals[i] = y/imageSlit         # scale output
 
    plt.plot(xpos,yvals,'o')
    xfine = np.linspace(-3,3,500)    # do a fine plot as comparison
    plt.plot(xfine,slits.getArrayValues(xfine))
    plt.ylim(0.0,1.0)
    
    plt.show()
        
main()   
    
