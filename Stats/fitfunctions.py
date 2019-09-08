"""
     Set of function to fit via curve_fit
"""
import numpuy as np

def perror(pcov):
    return np.sqrt(np.diag(pcov))

"""     Linear function
"""
def linear(x,a,b):
    return a*x + b

"""     Quadratic
"""
def quadratic(x,a,b,c):
    return a*x**2 + b*x + c

"""      Neg Exp
"""
def negexp(x,a,b,c):
    return a*np.exp(-b*x) + c

