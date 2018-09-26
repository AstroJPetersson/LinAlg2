import numpy as np
from scipy import *
from scipy.linalg import *

class TwoVector:
	
	def __init__(self, x, y):
		self.x=x
		self.y=y
		
	def angle(self):
		e1=np.array([1, 0]) #creates an unitvector along x 
		z=np.array([self.x, self.y]) #z is the TwoVector as an array
		theta=np.arccos((scipy.dot(z, e1))/norm(z)) #here the angle to the x-axis is calculated
		return theta
		
	def Galilei(self, relativevelocity): #Relativevelocity is the velocity of S' along the x-axis
		vxprim = matmul(np.array([-relativevelocity, 1]), np.array([1,self.x])) #vprim calculation on x-axis
		vyprim = matmul(np.array([0, 1]), np.array([1,self.y])) #vprim calculation on y-axis
		return np.array([vxprim,vyprim]) #return of vprim vector
