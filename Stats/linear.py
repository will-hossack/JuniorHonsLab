"""   Linear outpur test data
"""
import math
import random



def main():

    a = float(input("A : "))
    b = float(input("B : "))

    file = open(input("File : "),"w")

    for i in range(0,30):
        x = i
        y = a*x + b + random.uniform(-a,a)
        e = a
        file.write("{0:12.5e} , {1:12.5e} , {2:12.5e}\n".format(x,y,e))



main()
