import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f
from scipy.optimize import curve_fit


def main():
    filename = input("Input file : ")
    x,y,e = f.readCSV(filename,(True,True,True))


    line = lambda x,a,b : a*x + b
    popt,pcov = curve_fit(line,x,y,sigma=e)
    perr = np.sqrt(np.diag(pcov))
    print("a is : {0:10.5e} +/- {1:10.5e}".format(popt[0],perr[0]))
    print("b is : {0:10.5e} +/- {1:10.5e}".format(popt[1],perr[1]))
    
    plt.errorbar(x,y,xerr=0.0,yerr=e,fmt="bx")
    plt.plot([x[0],x[-1]],[line(x[0],popt[0],popt[1]),line(x[-1],popt[0],popt[1])],"r")
    plt.show()

main()
