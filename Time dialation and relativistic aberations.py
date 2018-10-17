# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 12:35:03 2018

@author: Harald Öhrn
"""
from scipy import* 
import numpy as np
import matplotlib.pyplot as plt

class FourVector:
	
	
	def __init__(self, x1, x2, x3, x4):
		self.x1 = x1
		self.x2 = x2
		self.x3 = x3
		self.x4 = x4
		self.ProductMatrix = np.array([[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
		
	def Minkowski(self, vec): #vec is the FourVector which should be multiplyed with.
		return matmul(np.array([self.x1, self.x2, self.x3, self.x4]),matmul(self.ProductMatrix, np.array([vec.x1, vec.x2, vec.x3, vec.x4])))
		#Above is based on the defenition of the Minkowski product given in excersice 2.
#note c = 1
	def Transform(self, velocity):
		gamma = 1/sqrt(1 - velocity**2) #define the gamma factor and the Lambda matrix below.
		Lambda = gamma * np.array([[1, -velocity, 0, 0], [-velocity, 1, 0, 0], [0, 0, 1/gamma, 0], [0, 0, 0, 1/gamma]])
		T = matmul(Lambda, np.array([self.x1, self.x2, self.x3, self.x4])) # Matrix multiplication of Lambda and the original
		return FourVector(T[0], T[1], T[2], T[3])
	# vector gives the transformed vector

#%%
#exercice 3.2
		
#at time t=1 (from the astronauts perspective)
astronaut = FourVector(1,0,0,0)
ylist = []
xlist = []
for n in linspace(0,1, 1000, False):
	#print(astronaut.Transform(n))
	xlist.append(n)
	ylist.append(astronaut.Transform(n)[0])
	
plt.plot(xlist, ylist)
plt.title("Astronaut time t = 1")
plt.xlabel("Velocity")
plt.ylabel("Earth time")

#%%

class VelocityVector:
	
	def __init__(self, vx, vy, vz):
		
		self.vx = vx
		self.vy = vy
		self.vz = vz

	def Transform(self, velocity):
		#Using the formula for velocity addition we derived in exercise 2.12
		vxprim = (self.vx + velocity)/(1 + self.vx * velocity)
		return VelocityVector(vxprim, self.vy, self.vz)

#%%
#reusing the framework from 1.3

def vector(deg): #This function creates an unitvector with "deg" degrease angle to the x-axis
	deg = pi/180 *deg
	return FourVector(0, np.cos(deg),np.sin(deg), 0)

deglist = [90,80,70]

for a in range(3):
	vtransform = []
	for shipspeed in linspace(10e-4,1,100):		
		aprim = vector(deglist[a]).Transform(shipspeed)
		phi = np.arccos(aprim.Minkowski(FourVector(0,1,0,0))/sqrt(aprim.x2**2 + aprim.x3**2 + aprim.x4**2))
		vtransform.append(phi)
		
	plt.plot(linspace(10e-4,1,100), vtransform) #ploting the angles with respect to v
	plt.legend(deglist)
	plt.xlabel('speed (c)')	
	plt.ylabel('angle (radians)')
	
#%%
#analytic 3.3
angle = []
for v in linspace(10e-4,1,100):
	phi = pi/2 - np.arcsin(v)
	angle.append(phi)
	
plt.plot(linspace(10e-4,1,100), angle) #ploting the angles with respect to v
plt.legend(deglist)
plt.xlabel('speed (c)')	
plt.ylabel('angle (raians)')

#%%

def vector(deg): #This function creates an directionalvector in the stars direction when our ships vector is along the x-axis
	deg = pi/180 *deg
	return VelocityVector(np.cos(deg), np.sin(deg), 0)

deglist = [90,80,70] #the theta angles

for a in range(3):
	vtransform = []
	for shipspeed in linspace(10e-4,1,100):		
		aprim = vector(deglist[a]).Transform(shipspeed)
		phi = np.arccos(dot(np.array([1,0,0]), np.array([aprim.vx,aprim.vy,aprim.vz]))) #transforming the stars directionalvector and projecting it on to the x-axis. 
		#note that in the above row, we should divide the inside of the arccos with our directional vectors norm, which is equal to 1.
		vtransform.append(phi) #collect the data in a list, which will be plotted
		
	plt.plot(linspace(10e-4,1,100), vtransform) #ploting the angles with respect to shipspeed
	plt.legend(deglist)
	plt.xlabel('speed (c)')	
	plt.ylabel('angle (radians)')
	