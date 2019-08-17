"""
Simple python program to read in CSV file with two or three col and do a Guassian fit.
The first two cols are the x/y data and the third (if given) is the error on y.
"""


import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f                 # Local CSV reader
from scipy.optimize import curve_fit


def gauss(x,a,b,c,d):
    """
    Define function to fit, (linear)
    """
    return a*np.exp(-((x - b)/(2*c**2))**2) + d

def main():
    filename = str(input("Input file : "))    # Get filename
    data = f.readCSV(filename)                # Read in data to array

    x = data[0]                               # set x/y to first cols
    y = data[1]

    if data.shape[0] > 2:               # If three cols use errors
        yErr = data[2]                  # set yErr to column 2 
    else:
        yErr = None                      # Set to None


    #      Estimate of peak location and height
    peakheight = np.amax(y)                   # Peak value
    peakloc = x[np.argmax(y)]            # Peak locaion
    

    # Do a fit using curve_fit, note retuns two lists. 
    popt,pcov = curve_fit(gauss,x,y,p0=[peakheight,peakloc,1.0,0.0],sigma=yErr)

    perr = np.sqrt(np.diag(pcov))        # Errors

    #    Print out the results, popt contains fitted vales and perr the errors
    print("a is : {0:10.5e} +/- {1:10.5e}".format(popt[0],perr[0]))
    print("b is : {0:10.5e} +/- {1:10.5e}".format(popt[1],perr[1]))
    print("c is : {0:10.5e} +/- {1:10.5e}".format(popt[2],perr[2]))
    print("d is : {0:10.5e} +/- {1:10.5e}".format(popt[3],perr[3]))

    plt.subplot(2,1,1)
    plt.errorbar(x,y,xerr=0.0,yerr=yErr,fmt="bx")     # Plot the data
    #      Plot the 
    plt.plot(x,gauss(x,*popt),"r")

    #       Label the graph
    plt.title("Guassian Fit pk: {0:8.4g} loc: {1:8.4g} w: {2:8.4g}".format(popt[0],popt[1],popt[2]))
    plt.xlabel("x value")
    plt.ylabel("y value")

    #    Add residuals
    plt.subplot(2,1,2)
    plt.errorbar(x,gauss(x,*popt) - y,xerr = 0.0, yerr = yErr,fmt = "rx")
    plt.xlabel("x value")
    plt.ylabel("y residual")
    plt.show()

main()
