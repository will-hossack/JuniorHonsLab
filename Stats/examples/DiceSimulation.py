"""
Dice simulation program written for Physics 1B lab but adapted to JH to show fitting of a neg expotential with
weighted errors.
"""

import random
import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
from scipy.optimize import curve_fit
import csvfile as f


class Dice(object):
    """
    Dice object for simulations
    """
    def __init__(self,sides = 6):
        """
        Constructor for Dice with specified number of sides
        """
        self.sides = sides

    def roll(self):
        """
        One roll of fair dice.
        """
        return random.randint(1,self.sides)
        #return int(round(self.sides*random.random() + 1.0))

    def throw(self,number = 1000):
        """
        Throw a number of dice, it will return list,
        but also hold the list internally.
        """
        self.sample = []
        while number >= 0:
            self.sample.append(self.roll())
            number -= 1

        return self.sample

    def count(self,value = 1):
        """
        Count the number of dice with a specific value, 
        Defaults to 1
        """
        n = 0
        for s in self.sample:
            if s == value:
                n += 1
        return n

    
def line(x, a, b, c):
    """
    Line to bve fitted, note use of np.exp() to allow np.ndarray() to be automatically returned.
    """
    return a*np.exp(-b*x) + c

def main():
    """
    Main program start
    """
    
    sides = int(input("Number of sides on each dice : "))
    startsample = int(input("Starting Sample : "))

                
    dice = Dice(sides)        # Make dice of right number of sides

    xData = []                # List to hold results of simulation
    yData = []
    run = 0
    sample = startsample
    while sample > 10:
        #      Store generation and sample size in lists.
        xData.append(run)
        yData.append(sample)
        dice.throw(sample)

        #       Get number of dice with value 1
        n = dice.count()
        sample -= n   # Reduce sample size by that number
        run += 1

    #            Do data fitting
    x = np.array(xData)     # convert x/y data to np arrays.
    y = np.array(yData)
    sig = np.sqrt(y)        # sd of error on y-data
    
    f.writeCSV(str(input("File : ")),[x,y,sig])     # Write data to CSV file
    
    #                Do the fitefit
    popt,pcov = curve_fit(line,x,y,sigma=sig)
    perr = np.sqrt(np.diag(pcov))        # Errors
    print("Optimal fit values " + str(popt))
    print("Error on values " + str(perr))


    #                Plot data
    plt.subplot(2,1,1)
    plt.errorbar(x,y,xerr=0.0,yerr=sig,fmt="bx")
    #                plot the optimal line
    plt.plot(x,line(x,*popt),"r",label="Decay: {0:8.4f} +\- {1:8.4f}".format(popt[1],perr[1]))
    plt.title("Decay plot for {0:d} dice with {1:d} sides".format(startsample,sides))
    plt.xlabel("Generation")
    plt.ylabel("Dice Number")
    plt.legend(loc="upper right",fontsize="small")

    plt.subplot(2,1,2)
    plt.errorbar(x,line(x,*popt) - y,xerr = 0.0, yerr = sig,fmt = "rx")
    plt.xlabel("Generation")
    plt.ylabel("Residual")
    
    plt.show()
    

main()    
