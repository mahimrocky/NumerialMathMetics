from math import exp,cos,sin,tan,log,log10
import parser
print("Equation format will be x**a+b*x+9 where a is the power of x")
print("b is the constant like 1,2...9 etc\n")
print("When need to input exp or cos or sin use exp() or sin() or log10()")
formula=str(input("Enter your whole equation:\n"))
code = parser.expr(formula).compile()

def f(x):
    return eval(code)

for i in range(1,40):
    f(i)
    f(i+1)
    if(f(i)*f(i+1)<0):
        a=i
        b=i+1
        if(a<b):
            d=float((a*f(b)-b*f(a))/(f(b)-f(a)))
        else:
            d=float((b*f(a)-a*f(b))/(f(a)-f(b)))
            
def falsePosition(x1,low,up):
    f(x1)
    if(f(x1)*f(low)<0):
        c=low
        if(x1<low):
            l1=float((x1*f(low)-low*f(x1))/(f(low)-f(x1)))
        else:
           l1=float((low*f(x1)-x1*f(low))/(f(x1)-f(low))) 
    else:
        c=up
        if(x1<up):
            l1=float((x1*f(up)-up*f(x1))/(f(up)-f(x1)))
        else:
           l1=float((up*f(x1)-x1*f(up))/(f(x1)-f(up))) 
    if(x1==l1 or c==l1):
       print("The desire root is: ",l1)
       return 
    falsePosition(l1,x1,c)
    
falsePosition(d,a,b)                
            


