import parser

from Tools.scripts.treesync import raw_input
from math import*
from Equation import*
a = int(raw_input("Enter value of a: "))
b = int(raw_input("Enter value of b: "))
tol = float(raw_input("Enter value of tolerance: "))
equ = str(raw_input("Enter equation: "))
i=0

def f(x):
    return (eval(equ))


def bisection_method(a, b, tol, i):
    if f(a) * f(b) > 0:
        # end function, no root.
        print("No root found.")
    else:
        while (b - a) / 2.0 > tol :
            midpoint = (a + b) / 2.0
            i+=1
            if f(midpoint) == 0:
                return (midpoint)

            elif f(a) * f(midpoint) < 0:  # Increasing but below 0 case
                b = midpoint

            else:
                a = midpoint
            print("i=" + str(i), "a=", round(a,4), "b=", round(b,4), "c=",round(midpoint,4),"f(a)=",round(f(a),4),"f(b)=",  round(f(b),4),"f(c)=",round(f(midpoint),4))

        print("No. of iterations = ",i);
        return (midpoint)



answer = bisection_method(a, b, tol,i)

print("Root of the given equation =",
      round(answer, 4));






