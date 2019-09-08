"""
Simple program to make linear data
"""
import numpy as np
import csvfile as f
import tio as t

def linear(x,a,b):
    return a*x + b


def main():
    xstart = t.getFloat("x start",1.0)
    xend = t.getFloat("x end",10.0)
    n = t.getInt("number",100)

    a = t.getFloat("gradient",0.5)
    b = t.getFloat("intercept",1.5)
    sd = t.getFloat("sd",0.0)
    
    x = np.linspace(xstart,xend,n)
    y = linear(x,a,b)
    y = np.random.normal(y,sd)
    e = np.full(x.size,sd)


    
    f.writeCSV(t.getFilename("File","txt"),[x,y,e])

main()
    
