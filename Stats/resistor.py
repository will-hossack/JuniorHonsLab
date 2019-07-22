import math
import numpy as np
import matplotlib.pyplot as plt



"""
     Resistor
"""

class Resistor(object):

    def __init__(self,r,alpha):

        self.r = r
        self.alpha = alpha
        

    def getResistance(self,v):

        return self.r*(1 + self.alpha*v*v/self.r)


    def getCurrent(self,v):

        return v/self.getResistance(v)

    def getCurrentArrayValues(self,v_array):
        i_array = np.empty(v_array.size)
        for i,v in enumerate(v_array):
            i_array[i] = self.getCurrent(v)

        return i_array
        


def main():

    resistor = Resistor(100,0.02)

    v_array = np.linspace(0,100,500)
    i_array = resistor.getCurrentArrayValues(v_array)

    plt.plot(v_array,i_array)
    plt.show()
    
main()
