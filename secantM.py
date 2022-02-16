import parser

from Tools.scripts.treesync import raw_input
from math import*
from Equation import *
a = int(raw_input("Enter value of a: "))
b= int(raw_input("Enter value of b: "))
tol = float(raw_input("Enter value of tolerance: "))
equ = str(raw_input("Enter equation: "))


def f(x):
    return (eval(equ))


def secant(a, b, tol):
    i = 0;
    xm = 0;
    x0 = 0;
    c = 0;
    if (f(a) * f(b) < 0) and i<= abs((log((b - a)/tol)/log(2))):
        while True:

            # calculate the intermediate value
            x0 = ((a * f(b) - b * f(a)) /
                  (f(b) - f(a)));

            # check if x0 is root of
            # equation or not
            c = f(a) * f(x0);

            # update the value of interval
            a = b;
            b = x0;

            # update number of iteration
            i += 1;

            # if x0 is the root of equation
            # then break the loop
            if (c == 0):
                break;
            xm = ((a * f(b) - b * f(a)) /
                  (f(b) - f(a)));

            if (abs(xm - x0) < tol):
                break;

        print("Root of the given equation =",
              round(x0, 4));


    else:
        print("Can not find a root in ",
              "the given inteval");

    # Driver code


# initializing the values


answer = secant(a, b, tol);







