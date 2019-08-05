""" 
Example program to read the data from the BigG experiment. It read in data, display it, then calcates
spectun which is also displays.
"""



import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import scipy.signal as sig
import csvfile as f


def main():

    #       Get filenamme
    filename = str(input("Input file : "))
    # Read to t,x numpy arrays using tab seperator and skipping the
    #  header of five lines.
    t,x = f.readCSV(filename,(True,True,False),separ="\t",headerskip=5)

    #      Plot raw data in upper pannel
    dt = t[1] - t[0]
    plt.subplot(2,1,1)
    plt.plot(t,x)
    plt.title("Input Data")
    plt.xlabel("Sample is : " + str(dt))

    #      Filter input signal by a Hamming window to reduce ailiasing
    hamming = sig.hamming(t.size)
    y = x*hamming

    #       Take fft, shift to centre and take modulus
    cft = np.fft.fft(y)
    cft = np.fft.fftshift(cft)
    mod = abs(cft)

    #         Build linear space for display
    dw = 1.0/(t.size*dt)
    w = np.linspace(-0.5/dt,0.5/dt,t.size)

    #         Plot mof of FT in lower window.
    plt.subplot(2,1,2)
    plt.plot(w,mod)
    plt.xlabel("Sample is : " + " {0:7.3e}".format(dw))

    
    plt.show()

    

    
main()
