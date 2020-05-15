""" 
Program to read in wavelength , index values from CSV file and 
fit first order Sellmier function 
"""

import numpy as np
import csvfile as csv
from optics.wavelength import Sellmeier,Sodium_D
import tio
import matplotlib.pyplot as plt

def main():

    file = tio.getFilename("File","txt")   # Open File
    wave,ref = csv.readCSV(file)           # Read to np arrays

    index = Sellmeier(1.25,0.1).fitIndex(wave,ref)
                          
    print("Index : " + repr(index))

    print("Nd : " + str(index.getNd()) + " Vd : " + str(index.getVd()))
    dn = index.getDerivative(Sodium_D)
    print("Derivative is : " + str(dn))
    
    plt.plot(wave,ref,"x")
    
    index.draw()
    plt.show()

    

    

    

    
main()

