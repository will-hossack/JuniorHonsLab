"""
      Porgram simulated imaging slit width.
"""
from slits import TwoSlits
from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import tio as t
import csvfile as csv


class FitSlits(TwoSlits):
    """
    Class to fit the slits, same as TwoSlits but with extra method sto specify line
    """
    def __init__(self,separ,width,distance,peak = 0.0, wave = 0.65, intensity = 1.0,offset = 0.0):
        """
        Just call the underlying class
        """
        TwoSlits.__init__(self,separ,width,distance,peak,wave)

    def line(self,x_array,a,b,c,d,e):
        """
        Define the line method aith 5 fitted paramers being
        separ, width, peak, intensity and offset
        """
        # Update the slit values with the parameters
        self.separ = a
        self.width = b
        self.peak = c
        self.intensity = d
        self.offset = e
        #   Return the line values as a np array with the updated parameters.
        return self.getArrayValues(x_array)



wave = 0.65        # Global wavelength
distance = 450.0   # Global distance


def main():

    # read in csv file and plot
    file = t.openFile("Data","r","txt")
    xpos,intensity = csv.readCSV(file)
    peak = (xpos[0] + xpos[-1])/2

    width = t.getFloat("Slit width",0.1)
    separ = t.getFloat("Slit seperation",0.4)
    peak = t.getFloat("Peak",peak)
    pintensity = t.getFloat("Peak Intensity",1.0)


    # Make a guess od the slits
    slits = FitSlits(separ,width,distance,peak,wave,pintensity,0.0)

    #     Do a curve fit wit p0 v=being the initial giess
    popt,pcov = curve_fit(slits.line,xpos,intensity,\
                          p0=[slits.separ,slits.width,slits.peak,slits.intensity,slits.offset])
    perr = np.sqrt(np.diag(pcov))
    # print(popt)
    # print(perr)

    #      Print out the results
    t.tprint("Separation: {0:7.5f} +/- {1:7.5}".format(popt[0],perr[0]))
    t.tprint("Slit width: {0:7.5f} +/- {1:7.5}".format(popt[1],perr[1]))
    t.tprint("Peak centre: {0:7.5f} +/- {1:7.5}".format(popt[2],perr[2]))
    t.tprint("Peak intensity: {0:7.5f} +/- {1:7.5}".format(popt[3],perr[3]))
    t.tprint("Offset: {0:7.5f} +/- {1:7.5}".format(popt[4],perr[4]))

    #    Plot outputs
    plt.plot(xpos,intensity,'o')
    xfine = np.linspace(xpos[0],xpos[-1],500)    # do a fine plot as comparison
    plt.plot(xfine,slits.getArrayValues(xfine))
    plt.ylim(0.0,slits.intensity)
    plt.title("Fit of Slit Data")
    plt.xlabel("X position")
    plt.ylabel("Intensity")
    
    plt.show()
        
main()   
    
