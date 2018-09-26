import numpy as np
from scipy import *

class TwoVector:
	
	def __init__(self, x, y):
		self.x=x
		self.y=y
		
	def angle(self):
		e1=np.array([1, 0])
		z=np.array([self.x, self.y])
		theta=np.arccos((dot(z, e1))/norm(z))
		return theta
		
	def Galilei(self, relativevelocity):
		vxprim = matmul(np.array([relativevelocity, 1]), np.array([1,self.x])) 
		vyprim = matmul(np.array([0, 1]), np.array([1,self.y])) 
		return TwoVector(vxprim,vyprim)
	
#%%
import matplotlib.pyplot as plt

def vector(deg):
	deg = pi/180 *deg
	return (np.cos(deg),np.sin(deg))

deglist = [90,80,70]


for a in range(3):
	listan = []
	for v in linspace(10e-4,1,100):		
		aprim = TwoVector(vector(deglist[a])[0],vector(deglist[a])[1]).Galilei(v)
		listan.append(aprim.angle())
		
	plt.plot(linspace(10e-4,1,100), listan)
	plt.legend(deglist)
	plt.xlabel('speed')	
	plt.ylabel('')

listan2 = []
for v in linspace(10e-4,1,100):
	listan2.append(1/2*pi - arctan(v))
plt.plot(linspace(10e-4,1,100),listan2, '-')
