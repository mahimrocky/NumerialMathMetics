n=int(input("Enter the order of matrix :"))
mat={}
z={}
x={}
b=0
ne=0
p=0
flag=0
print("Enter matrix element row wise\n")

for i in range(0,n):
    for j in range(0,n):
        a=float(input());
        mat[i,j]=a;

print("Enter column vector\n")
for i in range(0,n):
    a=float(input())
    x[i,0]=a

for m in range(0,30):
    for i in range(0,n):
        z[i,0]=0
        for j in range(0,n):
            z[i,0]=z[i,0]+mat[i,j]*x[j,0]

    zmax=z[0,0]
    for i in range(1,n):
        if(z[i,0]>zmax):
            zmax=z[i,0]
    for i in range(0,n):
        z[i,0]=z[i,0]/zmax

    if(m==0):
        p=zmax
    if(m!=0):
        ne=zmax
        if(round(ne,3)==round(p,3)):
            flag==1
        p=ne
    if(flag==1):
        break
    
    for i in range(0,n):
        x[i,0]=z[i,0]

print("Eigen value is :%.3f"%zmax)
for i in range(0,n):
    print("%.3f"%z[i,0])
    print(" ")
    



        
