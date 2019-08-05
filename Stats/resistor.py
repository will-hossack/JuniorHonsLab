import math
import numpy as np
import matplotlib.pyplot as plt
import csvfile as f
import tio as t



"""
     Resistor
"""

class Resistor(object):
    """
    Class to represent a temperature dependence resistor
    
    param r the static resitsance
    param alpha the temperature dependant term, (Default = 0.0)
    """
    def __init__(self,r,alpha = 0.0):
        """ Constrcutor    """
        self.r = r
        self.alpha = alpha
        

    def getResistance(self,v):
        """ Get the resistance for specified voltage
        param v the voltage, eirher float or nparray
        return the resistance, float or ndarray
        """
        return (self.r + np.sqrt(self.r**2 + 4*self.alpha*v**2))/2.0

    def getResistanceApprox(self,v):
        return self.r + self.alpha*v**2/self.r



    def getCurrent(self,v):
        """ Get the current
        param v the voltage, float of ndarray
        return the current, float of ndarray
        """
        return v/self.getResistance(v)        

    def getCurrentApprox(self,v):
        return v/self.getResistanceApprox(v)
        #return v/self.r - self.alpha*v**3/self.r**3

def main():


    res = t.getFloat("Static resistance",100.0)
    alpha = t.getFloat("Alpha",2.0)
    maxv = t.getFloat("Maximum voltage",50.0)
    offset = t.getFloat("Current offset",0.0)
    sd = t.getFloat("SD of noise as percentage",0.1)


    
    resistor = Resistor(res,alpha)

    
    v_array = np.linspace(0,maxv,50)
    i_array = resistor.getCurrent(v_array) + offset
    imax = i_array[-1]
    sd *= imax
    e_array = np.full(v_array.size,sd)
    n_array = np.random.normal(i_array,sd)
    n_array = np.maximum(n_array,0.0)     # Force to be positive

    f.writeCSV(t.getFilename("File : ","txt"),[v_array,n_array,e_array])
    
    
    plt.plot(v_array,i_array,"r")
    #    plt.plot(v_array,resistor.getCurrentApprox(v_array),"g")
    #plt.plot(v_array,resistor.getResistance(v_array),"r")
    #plt.plot(v_array,resistor.getResistanceApprox(v_array),"g")
    
    plt.plot(v_array,n_array,"+")
    plt.show()
    
main()
