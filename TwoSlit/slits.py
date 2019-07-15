"""
      Class for two slits
"""
import math
import numpy as np


class TwoSlits(object):
    """
    Function to give difration of two slits, sized in mm.

    :param separ: seperation of centre
    :param width: width of slit
    :param distance: distance to image plane
    :param wave: the wavelength (Default = 0.65 microns)
    :praam intensity: Intesity at ceebtral peak (Default = 1.0)
    """

    def __init__(self,separ,width,distance,wave = 0.65, intensity = 1.0):

        self.separ = float(separ)
        self.width = float(width)
        self.distance = float(distance)
        self.wavelength = wave/1000.0
        self.intensity = intensity

    def getValue(self,x):
        """
        Get the value at x
        
        :param x: the distance from optical axis
        :return: the intensity
        """
        alpha = math.pi*self.width*x/(self.wavelength*self.distance)
        beta = math.pi*self.separ*x/(self.wavelength*self.distance)
        if alpha == 0.0:
            return self.intensity
        else:
            a = math.sin(alpha)/alpha * math.cos(beta)
            return self.intensity*a*a

            
    def getArrayValues(self,x_array):
        """
        Get numpy array of values
        
        :param x_array: np.array of x values
        :return: np.array of y values.
        """
        
        y_array = np.empty(x_array.size)
        for i,x in enumerate(x_array):
            y_array[i] = self.getValue(x)

        return y_array

    



    

def line(x,separ,width,offset):
    s = TwoSlits(separ,width,400.0,0.68)
    return s.getValue(x) + offset
    
    

    
    
        
