from math import exp,cos,sin,tan,log
import parser
print("Equation format will be x**a+b*x+9 where a is the power of x")
print("b is the constant like 1,2...9 etc\n")
print("When need to input exp or cos or sin use exp() or sin()")
formula=str(input("Enter your whole equation:\n"))
code = parser.expr(formula).compile()

def f(x):
    return eval(code)

def bisection(x1,low,up):
    f(x1)
    if(f(x1)*f(low)<0):
        l1=float((x1+low)/2)
        c=low
    else:
        l1=float((x1+up)/2)
        c=up
        
    if(x1==l1 or c==l1):
       print(l1)
       return 
    bisection(l1,x1,c)
    

for i in range(-10,20):
    f(i)
    f(i+1)
    if(f(i)*f(i+1)<0):
        n1=i
        n2=i+1
        a=float((i+i+1)/2)

bisection(a,n1,n2)

