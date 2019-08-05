"""
Simple python program to read in CSV file with two or three col and do a liner fit.
The first two cols are the x/y data and the third (if given) is the error on y.
"""


import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f                 # Local CSV reader
from scipy.optimize import curve_fit


def linear(x,a,b):
    """
    Define function to fit, (linear)
    """
    return a*x + b

def main():
    filename = str(input("Input file : "))    # Get filename
    data = f.readCSV(filename)                # Read in data to array

    x = data[0]                               # set x/y to first cols
    y = data[1]

    if data.shape[0] > 2:               # If three cols use errors
        yErr = data[2]                  # set yErr to column 2 
    else:
        yErr = 0.0                      # Set to zero



    # Do a fit using curve_fit, note retuns two lists.
    popt,pcov = curve_fit(linear,x,y,sigma=yErr)

    perr = np.sqrt(np.diag(pcov))        # Errors

    #    Print out the results, popt contains fitted vales and perr the errors
    print("a is : {0:10.5e} +/- {1:10.5e}".format(popt[0],perr[0]))
    print("b is : {0:10.5e} +/- {1:10.5e}".format(popt[1],perr[1]))
    
    plt.errorbar(x,y,xerr=0.0,yerr=yErr,fmt="bx")     # Plot the data
    #      Plot the 
    plt.plot([x[0],x[-1]],[linear(x[0],popt[0],popt[1]),linear(x[-1],popt[0],popt[1])],"r")

    #       Label the graph
    plt.title("Linear Fit")
    plt.xlabel("x value")
    plt.ylabel("y value")
    plt.show()

main()
