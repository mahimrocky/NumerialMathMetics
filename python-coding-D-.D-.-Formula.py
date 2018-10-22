#Newton Divided difference Formula: Python Coding from below
diff1,diff2,diff3,diff4,diff5,x,y = [ ] , [ ] , [ ] , [ ] , [ ]  , [ ] , [ ]
v,w,k=0,0,0
result=0
n=int (input("How many pairs of x and y:\t"))
print ("Enter the value of x:\n")
for i in range(0,n):
    a=float(input())
    x.append(a)
print ("Enter the value of y:\n")
for i in range(0,n):
    b=float(input())
    y.append(b)
print ("Enter the value of x: ")
m=float(input())

for i in range(0,n-1):
    v=(y[i+1]-y[i])
    w=(x[i+1]-x[i])
    k= float (v/w)
    diff1.append(k)
v,w,k=0,0,0
for i in range (0,n-2):
    v=(diff1[i+1]-diff1[i])
    w=(x[i+2]-x[i])
    k= float (v/w)
    diff2.append(k)
v,w,k=0,0,0
for i in range (0,n-3):
    v=(diff2[i+1]-diff2[i])
    w=(x[i+3]-x[i])
    k= float (v/w)
    diff3.append(k)
v,w,k=0,0,0
for i in range (0,n-4):
    v=(diff3[i+1]-diff3[i])
    w=(x[i+4]-x[i])
    k= float (v/w)
    diff4.append(k)
v,w,k=0,0,0
for i in range (0,n-5):
    v=(diff4[i+1]-diff4[i])
    w=(x[i+5]-x[i])
    k= float (v/w)
    diff5.append(k)
if(n==6):
    result=float (y[0]+(m-x[0])*diff1[0]+
                  (m-x[0])*(m-x[1])*diff2[0]+(m-x[0])*(m-x[1])*(m-x[2])*diff3[0]+(m-x[0])*(m-x[1])
              *(m-x[2])*(m-x[3])*diff4[0]+
                  (m-x[0])*(m-x[1])*(mx[2])*(m-x[3])*(m-x[4])*diff5[0])
elif(n==5):
    result=float (y[0]+(m-x[0])*diff1[0]+(m-x[0])*(m-x[1])*diff2[0]+(m-x[0])*(m-x[1])*(m-x[2])*diff3[0]+(m-x[0])
              *(m-x[1])*(m-x[2])*(m-x[3])*diff4[0])
elif(n==4):
    result=float (y[0]+(m-x[0])*diff1[0]+(m-x[0])*(m-x[1])*diff2[0]+(m-x[0])*(m-x[1])*(m-x[2])*diff3[0])
print ("the result is : ",result)  
