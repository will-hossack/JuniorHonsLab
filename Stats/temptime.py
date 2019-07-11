import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f

def main():
    temp,time = f.readCSV(input("File : "))

    plt.errorbar(temp,time,2.0,1.0,fmt = "o")
    plt.show()

main()
