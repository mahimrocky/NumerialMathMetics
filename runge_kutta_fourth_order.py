import math
import parser

formula = str(input("Enter the equation:\n"))
code = parser.expr(formula).compile()
def f(x,y):
    return eval(code)

print("Enter the value of x0:\n")
x0=float(input())

print("Enter the value of yo:\n")
y0=float(input())

print("Enter the value of h:\n")
h=float(input())

k1=round(float(h*(f(x0,y0))),5)
k2=round(float(h*(f(x0+h/2,y0+k1/2))),5)
k3=round(float(h*(f(x0+h/2,y0+k2/2))),5)
k4=round(float(h*(f(x0+h,y0+k3))),5)

del_y=(k1+(2*k2)+(2*k3)+k4)/6

y=round(y0+del_y,5)
print(y)
