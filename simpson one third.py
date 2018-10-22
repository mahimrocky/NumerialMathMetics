n=int(input("give the no. of records"))  
x=[]
y=[]
sum=0
k=0
print("value of x :")
for i in range(0,n):
    a=float(input())
    x.append(a)


print("value of y :")
for i in range(0,n):
    b=float(input())
    y.append(b)


h=x[1]-x[0]
n=n-1
sum = sum + y[0]
for i in range(1,n):
    if(k==0):
        sum=sum+4*y[i]
        k=1
    else:
        sum=sum+2*y[i]
        k=0
        
sum=sum+y[n]
sum=sum*(h/3)
print("\n\n I = ",sum)
