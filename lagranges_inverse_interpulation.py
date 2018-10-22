import math
print("Enter the range:\n")
n=int(input());
x=list()
y=list()
ans=0
print("Enter the value of x:\n")
for i in range(1,n+1):
    x.append(int(input()))
print("Enter the value of y:\n")
for i in range(1,n+1):
    y.append(float(input()))

n1=float(input("Enter the value you want to calculation:\n"))

for j in range(0,n):
    x2=1
    x4=1
    for k in range(0,n):
        if(k!=j):
            x1=(n1-y[k])
            x2=x2*x1
            x3=(y[j]-y[k])
            x4=x4*x3
    ans1=(x2/x4)*x[j]
    ans=ans+ans1
print("The desire answer is: ",ans)
    
            
