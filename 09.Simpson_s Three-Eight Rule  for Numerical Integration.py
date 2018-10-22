print ("Enter the pair of x and y :")
n = int (input())

x = []
print ("Enter the value of x : \n")
for i in range(0,n):
    x1 = float(input())
    x.append(x1)

y=[]
print ("Enter the value of y : \n")
for i in range(0,n):
    y1 = float(input())
    y.append(y1)

result = 0.0
h = x[1]-x[0]
p = y[0]+y[n-1]
q = 0.0
r = 0.0

for i in range(1,n-1):
    if(i!=3):
        q = q+y[i]

for j in range (1,n-1):
    if(j%3 == 0):
        r = r + y[j]        
result = (3/8)*h*(p+(3*q)+(2*r))
print(result)
