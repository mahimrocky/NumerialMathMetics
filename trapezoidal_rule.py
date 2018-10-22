from math import log,exp,sin,cos

import parser

print ("Enter the lower range : \n")

l=float (input())
print ("Enter the higher range : \n")
h=float (input())
print("Enter the value of h:\n")
h1=float(input())

def frange(c, d, e):
  while round(c,3) <= round(d,3):
    yield c
    c += e
x1=list(frange(l,h,h1))
formula=str(input("Enter your whole equation:\n"))
code = parser.expr(formula).compile()
def f(x):
    return eval(code)

y=list()
for i in range(0,len(x1)):
    b=f(x1[i])
    y.append(b)

  
result = 0
p=y[0]+y[len(x1)-1]
q=0

for i in range(1,len(x1)-1):
    a=y[i]
    q=q+a
result = (h1/2)*(p+2*q)
print ("The answer is: ",result)

