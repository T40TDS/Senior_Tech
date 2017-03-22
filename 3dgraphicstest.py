from graphics import *
import numpy as np
from numpy import cos as co
from numpy import sin as s
import math
import time
width = 500#todo add functions
height = 500
framerate = 120

def main():
    a = np.array([3,4,178.0])
    b = cameraTransform(a)
    print(b)



def cameraTransform(a): #a is of type numpy array of double
    c = np.array([5.0,0,0])
    theta = np.array([0.0,0,0])
    e = np.array([0.0,0,0])
    d = a-c
    d = np.dot(np.array([[co(theta[2]),s(theta[2]),0],[-s(theta[2]), co(theta[2]),0],[0,0,1]]),d)
    print(d)
    d = np.dot(np.array([[co(theta[1]),0,-s(theta[1])],[0,1,0],[s(theta[1]),0,co(theta[1])]]),d)
    d = np.dot(np.array([[1,0,0],[0,co(theta[0]),s(theta[0])],[0,-s(theta[0]), co(theta[0])]]),d)
    print(d)
    b = np.array([((e[2]/d[2])*d[0]-e[0]),((e[2]/d[2])*d[1]-e[1])])
    return b

main()
