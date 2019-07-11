import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f


def main():

    td, = f.readCSV(input("Input file : "))
    print("Length is " + str(td.size))
    print(td)
    print("Mean is : " + str(np.mean(td)) + " and STD is " + str(np.std(td)))
    print("Error on mean is : " + str(np.std(td/math.sqrt(td.size))))
    plt.hist(td,20)
    plt.show()

main()
