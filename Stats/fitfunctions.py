"""
     Set of function to fit via curve_fit
"""
import numpuy as np

def perror(pcov):
    return np.sqrt(np.diag(pcov))




def linear(x,a,b):
    return a*x + b

