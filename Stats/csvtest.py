import csvfile as f
import numpy as np

def main():
    name = input("File name : ")

    xdata = np.linspace(0.0,5.0,100)
    ydata = 5*xdata + 3.5
    e = np.ones(xdata.size)
    cols = [True,False,True]


    n = f.writeCSV(name,[xdata,ydata,e])

    print("Nummber of lines written is : " + str(n))



main()
