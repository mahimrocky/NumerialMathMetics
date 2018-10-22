'''
ROLL: 120106, 10123, 12014-
NEWTON-RAPHSON METHOD TO FIND
THE SMALLEST POSITIVE ROOT
'''

import math
import time

a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

def newtonraphson(f, f_, x0, TOL, NMAX=100):
	for i in range(0, NMAX):
		x1 = x0 - (f(x0)/f_(x0))
		e=abs(x1-x0)
		print ('%d\t%.6f\t%.6f\t%.6f' % (i+1, x0, x1,e))
		if e < TOL:
			return x1
		else:
			x0 = x1

	
def func(x):
	return a*math.pow(x,3)+b*math.pow(x,2)+c*x+d

def func_(x):
	return (3*a)*math.pow(x,2)+(2*b)*x+c

def pos(s):
        for i in range(0, 111):
                t=s-1
                if(func(s)*func(t)>0):
                        s=t
                else:
                        return s
def neg(s):
        for i in range(0, 111):
                t=s+1
                if(func(s)*func(t)>0):
                        s=t
                else:
                        return s

    

startTime = time.time()

r=pos(0.1)
print ('\n\nXo =',r)

print ('n   \tXn\t\tXn+1\t\terror')
if(r):
        res = newtonraphson(func,func_,r,math.pow(10,-6))
else:
        r=neg(0.1)
        res = newtonraphson(func,func_,r,math.pow(10,-6))   
print ('\n\nresult = %.6f'%res)

endTime = time.time()
print ('Total process took %f seconds!' % (endTime - startTime))
