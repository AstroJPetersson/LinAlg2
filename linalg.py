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
		Svelocity = [self.x, self.y] #velocity in the S system. Denoted v_0 in exersice 1.1
		transformationmatrix = np.array([[1,0],[-relativevelocity, 1]]) #the transformation matrix gamma
		V = np.array([1, Svelocity]) #the untransforemed vector
		vprim=scipy.matmul(transformationmatrix, V)
		return vprim