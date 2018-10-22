m=int(input("Enter the number of t values. "))
y=[]
T=[]
H=float(0)
k1=float(0)
k2=float(0)
k3=float(0)
de=float(0)

def fnc(n1,n2):
    return ((n1-n2)/2.0)

print("Enter the values of t0,t1,t2......\n")
for i in range(0,m):
    a=float(input())
    T.append(a)
    
print("Enter the values of y[0]\n")
for i in range(0,m):
    y.append(0)

for j in range(0,m-1):
    H=T[j+1]-T[j]
    print("H=%f\n"%H)
    k1=H*fnc(T[j],y[j])
    k2=H*fnc(T[j]+H/2.0,y[j]+.5*k1)
    k3=H*fnc(T[j]+H,y[j]+2*k2-k1)
    de=(k1+4*k2+k3)/6.0
    y[j+1]=y[j]+de

for j in range(0,m):
    print("J=%f\n"%j)
    print("Y[j]=%f"%y[j])
