import numpy as np
from scipy import *
from scipy.linalg import *

class TwoVector:
	
	def __init__(self, x, y):
		self.x=x
		self.y=y
		
	def angle(self):
		e1=np.array([1, 0])
		z=np.array([self.x, self.y])
		theta=np.arccos((scipy.dot(z, e1))/norm(z))
		return theta
		
	def Galilei(self, relativevelocity):
		v0=np.array([1, np.array([self.x, self.y])])
		vprim=scipy.matmul(np.array([-relativevelocity, 1]), v0)
		