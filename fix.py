
from Tools.scripts.treesync import raw_input
from math import*

from Equation import *

x0 = int(raw_input("Enter value of x0: "))
max_itr= int(raw_input("Enter max number of iteration: "))
fx_equ= str(raw_input("f(x): "))
gx_equ = str(raw_input("g(x): "))
cnt=1

def f(x):
    return (eval(fx_equ))

def g(x):
    return (eval(gx_equ))
print()
print('i','x(i)','g(x)','f(x)')
print(1,x0,round(g(x0),4),round(f(x0),4))
x=g(x0)
condition=True
while cnt<max_itr or condition:
    cnt=cnt+1
    print(cnt,round(x,4),round(g(x),4),round(f(x),4))
    x=g(x)
    condition = abs(g(x)) < 0.01







