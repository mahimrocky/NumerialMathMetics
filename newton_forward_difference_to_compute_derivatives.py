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
"""print(z) """   
h=x[1]-x[0]
c=0.0
d=0.0

"""For first derivatives"""
for i in range(1,n):
    if(i%2==0):
       c+=float((z[i-1][0])/i)
    else:
        d+=float((z[i-1][0])/i)
ans=float((d-c)*(1/h))
print("The first order is: ",ans)
