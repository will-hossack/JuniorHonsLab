import math
import matplotlib.pyplot as plt     # Import the plot package as plt
import numpy as np
import csvfile as f


def main():

    td, = f.readCSV(input("Input file : "))
    print("Length is " + str(td.size))
    mean = np.mean(td)
    std = np.std(td)
    em = std/math.sqrt(td.size)
    print("Mean is : " + str(mean) + " and STD is " + str(std))
    print("Error on mean is : " + str(em))
    plt.hist(td,50)
    plt.plot([mean,mean],[0,50],"r")
    plt.plot([mean - std,mean - std],[0,50],"g")
    plt.plot([mean + std,mean + std],[0,50],"g")
    plt.plot([mean - 2*std,mean - 2*std],[0,20],"b")
    plt.plot([mean + 2*std,mean + 2*std],[0,20],"b")
    plt.plot([mean - 3*std,mean - 3*std],[0,10],"b")
    plt.plot([mean + 3*std,mean + 3*std],[0,10],"b")
    plt.title("Mean : {0:6.4f} sd: {1:6.4f} em: {2:6.4f}".format(mean,std,em))
    plt.show()

main()
