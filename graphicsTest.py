from graphics import *
import numpy as np
from numpy import Cos as co
from numpy import Sin as s
import math
import time
width = 500#todo add functions
height = 500
framerate = 120

a = np.array([0,0,0])
c = np.array([0.0,0,0])
theta = np.array([0.0,0,0])
e = np.array([0.0,0,0])


d = np.dot(array([co(theta[2],s(theta[2]),0],[-s(theta[2]), co(theta[2]),0],[0,0,1]),a-c)
d = np.dot(array([co(theta[1]),0,-s(theta[1])],[0,1,0],[s(theta[1]),0,c(theta[1])]),d)
d = np.dot(array([1,0,0],[0,co(theta[0]),s(theta[0])],[0,-s(theta[0]), co(theta[0])]),d)
b = np.dot(array[((e[2]/d[2])*d[0]-e[0]),((e[2]/d[2])*d[1]-e[1])])



def main():
	win = GraphWin("Plot", width ,height,autoflush=False)
	win.setCoords(0,0,width,height)
	win.setBackground("black")

	xAxis = Line(Point(0, .02*height), Point(width, .02*height))
	yAxis = Line(Point(.02*width, 0), Point(.02*width, height))
	xAxis.setOutline("green")
	yAxis.setOutline("green")

	xAxis.draw(win)
	yAxis.draw(win)
	array = ([1,3])
	fl = open("posData.txt",'r')
	lines = linesFile("posData.txt")
	for i in range(lines):
		line_i = fl.readline()
		s = line_i.split()
		x = s[0]
		y = s[1]
		pt = Point((int(x)),(int(y)))
		pt.setOutline("blue")
		pt.draw(win)
		time.sleep(1/60.00)
		update(30)


	win.getMouse()
	win.close()
def linesFile(name):
    i = 0
    f = open(name, "r")
    for line in f:
        i+=1
    return i;




main()
