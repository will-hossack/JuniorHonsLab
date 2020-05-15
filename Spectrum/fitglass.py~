""" 
Program to read in wavelength , index values from CSV file and 
fit first order Sellmier function 
"""

import numpy as np
import csvfile as csv
import optics.wavelength as w
import tio
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit




def main():

    file = tio.getFilename("File","txt")   # Open File
    wave,ref = csv.readCSV(file)           # Read to np arrays

    #        Define the fite function with two parameters
    fit = lambda wave,a,b: w.Sellmeier(a,b).getArrayValues(wave)
    

    #        Do the fit
    popt,pcov = curve_fit(fit,wave,ref,p0=[1.25,0.1])
    tio.tprint(popt)
    tio.tprint("Alpha is : ",popt[0]," and lambda_0 is : ",popt[1])
                          
    
                          
    index = w.Sellmeier(*popt)
    

    print("Nd : " + str(index.getNd()) + " Vd : " + str(index.getVd()))
    dn = index.getDerivative(w.Sodium_D)
    print("Derivative is : " + str(dn))
    
    plt.plot(wave,ref,"x")
    
    index.draw()
    plt.show()

    

    

    

    
main()

