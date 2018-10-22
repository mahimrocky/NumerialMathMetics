import math
print("Enter the range:\n")
n=int(input())
x=list()
y=list()

print("Enter the value of x:\n")
for i in range(0,n):
    x.append(int(input()))
    
print("Enter the value of y:\n")
for i in range(0,n):
    y.append(float(input()))    

x1=math.log(float(input("Enter the value for calculation:\n")))

z=list()
z.append(list())
for i in range(0,n):
    z[0].append(y[i])
    

for i in range(1,n):
    m=list()
    for j in range(0,n-i):
        a=float(z[i-1][j+1]-z[i-1][j])
        b=float(x[j+i]-x[j])
        c=float(a/b)
        m.append(c)
    z.append(m)    

for i in range (0,n):
    for j in range (0,n-i):
        print (z[i][j])

ans=y[0]
ans1=1
for i in range(1,n):
    d=x1-x[i-1]
    ans1=ans1*d
    ans=ans+(ans1*z[i][0])
print("The answer is: ",ans)    

