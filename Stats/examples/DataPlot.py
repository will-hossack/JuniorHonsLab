""" 
Simple Python programme to read in a multi collumn CSV fine and plot
the first two colums as a x/y graph. If there is a third colulm it
will be used for the y error bars.

"""

import numpy as np
import sys
import matplotlib.pyplot as plt
import csvfile as f     # Local CVS reader


def main():

    filename = str(input("File : "))    # Read file name as str
    data = f.readCSV(filename)          # Default csv read to array on np.array

    
    if data.shape[0] > 2:               # If three cols use errors
        yErr = data[2]                  # set yErr to column 2 
    else:
        yErr = None                     # Set to None

    #        Plot out data with errors bars and sensible titles.
    plt.errorbar(data[0],data[1],xerr=0.0,yerr=yErr,fmt="bx")
    plt.title("Data Plot: {0:s}".format(filename))
    plt.xlabel("x value")
    plt.ylabel("y value")
    plt.show()

main()
