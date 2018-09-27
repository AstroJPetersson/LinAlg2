import numpy as np
from scipy import *

class TwoVector:
	
	def __init__(self, x, y):
		self.x=x
		self.y=y
		
	def angle(self):
		e1=np.array([1, 0]) #creates an unitvector along x
		z=np.array([self.x, self.y]) #z is the TwoVector as an array
		theta=np.arccos((dot(z, e1))/norm(z)) #here the angle to the x-axis is calculated
		return theta
		
	def Galilei(self, relativevelocity): #Relativevelocity is the velocity of S' along the x-axis
		vxprim = matmul(np.array([relativevelocity, 1]), np.array([1,self.x])) #vprim calculation on x-axis
		vyprim = matmul(np.array([0, 1]), np.array([1,self.y])) #vprim calculation on y-axis
		return TwoVector(vxprim,vyprim) #return of vprim vector
	
#%%
import matplotlib.pyplot as plt

def vector(deg): #This function creates an unitvector with "deg" degrease angle to the x-axis
	deg = pi/180 *deg
	return (np.cos(deg),np.sin(deg))

deglist = [90,80,70] #the thetha angles used in exercise 1.3

for a in range(3):
	vtransform = []
	for v in linspace(10e-4,1,100):		
		aprim = TwoVector(vector(deglist[a])[0],vector(deglist[a])[1]).Galilei(v) #transforming the vector, note that c=1
		vtransform.append(aprim.angle()) # adding all the transformed angles to a list.
		
	plt.plot(linspace(10e-4,1,100), vtransform) #ploting the angles with respect to v
	plt.legend(deglist)
	plt.xlabel('speed')	
	plt.ylabel('')

#%%

listan2 = [] #polting the analytic referense fi(v) = 90 - arctan(v/c)
for v in linspace(10e-4,1,100):
	listan2.append(1/2*pi - arctan(v)) #c=1 gives the expresion
plt.plot(linspace(10e-4,1,100),listan2, '-')

#The analytic result corespond very well with our plot for 90 degrees.  

#Harald Öhrn, Viktor Hrannar Jónsson, Johan Nilsson, Jonathan Petersson
