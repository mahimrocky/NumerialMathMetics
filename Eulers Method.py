print('Enter the value of x0,y0,h,x')
x0=float(input())
y0=float(input())
h=float(input())
x=float(input())
x1=x0
y1=y0
for i in range(0,10):
 if(x1>x):
  break
  y1+=h*(x1+y1)
x1+=h
print("X1 y1",x1,y1)
