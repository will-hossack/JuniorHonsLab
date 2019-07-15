"""
      Porgram to plot slits
"""
from slits import TwoSlits
import numpy as np
import matplotlib.pyplot as plt
import tio as t


def main():

    width = t.getFloat("Slit width",0.1)
    separ = t.getFloat("Slit seperation",0.4)
    distance = t.getFloat("Distance",400)
    
    slits = TwoSlits(separ,width,distance,0.68)
    x = np.linspace(-5,5,500)
    y = slits.getArrayValue(x)

    plt.plot(x,y)
    plt.show()

main()
    
    

    
    
        
