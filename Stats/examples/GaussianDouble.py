"""
Formgaussian data with optional noise
"""
import numpy as np
import csvfile as f

def gauss(x,a,b,c,d):
    """
    Define function to fit, (linear)
    """
    return a*np.exp(-((x - b)/(2*c**2))**2) + d

def main():

    
    w0One = float(input("w0 One : "))
    w0Two = float(input("w0 Two : "))
    peakOne = 10
    peakTwo = 6
    width = float(input("width :"))
    sd = float(input("SD of noise as fraction of max : "))
    sd *= (peakOne + peakTwo)/2
               
    x = np.linspace(0.0,w0One + w0Two,100)
    y = gauss(x,peakOne,w0One,width,0.0) + gauss(x,peakTwo,w0Two,width,0.0) 
    y = np.random.normal(y,sd)         # add noise
    y = np.maximum(y,0.0)             # force positice (will add a DC)
    f.writeCSV(str(input("File : ")),[x,y,np.full(x.size,sd)])

main()
