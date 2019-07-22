"""
      Simple programms  plot slits using tio input library
"""
from slits import TwoSlits
import numpy as np
import matplotlib.pyplot as plt
import tio as t

wave = 0.65
distance = 450.0

def main():
    
    #      get the paramters
    width = t.getFloat("Slit width",0.1)
    separ = t.getFloat("Slit seperation",0.4)
    peak = t.getFloat("Peak",5.0)
    
    #       Form the data
    slits = TwoSlits(separ,width,distance,peak,wave)
    x_array = np.linspace(0.0,10.0,500)
    y_array = slits.getArrayValues(x_array)

    #      Plot the output
    plt.plot(x_array,y_array)
    plt.ylim(0.0,1.0)
    plt.title("Two Slits")
    plt.xlabel("X positition")
    plt.ylabel("Intensity")
    plt.show()

main()
    
    

    
    
        
