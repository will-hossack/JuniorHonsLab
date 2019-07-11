import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f

def main():
    m,t = f.readCSV(input("File : "))
    k = 4.0*math.pi**2 * m/t**2
    print(k)

    kmean = np.mean(k)
    kerr = np.std(k)/math.sqrt(k.size)

    print("Value of k is : {0:5.2f}  +/-  {1:4.2f}".format(kmean,kerr))
    
main()
