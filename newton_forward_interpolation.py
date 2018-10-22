import math
print("Enter the range:\n")
n=int(input())
x=list()
y=list()

print("Enter the value of x:\n")
for i in range(0,n):
    x.append(float(input()))
    
print("Enter the value of y:\n")
for i in range(0,n):
    y.append(float(input()))    

x1=float(input("Enter the value for calculation:\n"))
p=float((x1-x[0])/(x[1]-x[0]))

z=list()
z.append(list())

for i in range(0,n-1):
    a=float(y[i+1]-y[i])
    z[0].append(a)

for i in range(1,n):
    m=list()
    for j in range(0,n-1-i):
        b=float(z[i-1][j+1]-z[i-1][j])
        m.append(b)
    z.append(m)
    
ans=y[0]
p1=1
p2=1
for i in range(1,n):
    p1=p1*(p-i+1)
    p2=p2*i
    ans=ans+(p1/p2)*z[i-1][0]
print(ans)    
       
  
    
