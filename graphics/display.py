import pygame
import time
import math
import random
import numpy as np
import serial
import time
#all sorts of initializations
startingPoint = 0
ser = serial.Serial('COM5', 9600)
vel = [0,0,0]
velhistory = []
accelhistory = []
accel_values = []
graphPoints = []
pos = [0,0,0]
offset = 524; #Engineering Note 8
time0 = time.time()
timef = 0
pygame.font.init()
myfont = pygame.font.Font("fonts/CMUSerif-Roman.ttf", 15)

clock = pygame.time.Clock()
width = 400
height = 400
fps = 60
deltax = 200
deltay = 200
newTransform = False
scaleFactor = 1
originalVectors = []


class Particle:
    def __init__(self, location, size):
        self.x = location[0]
        self.y = location[1]
        self.size = size
        self.colour = (0,255,0)
        self.thickness = 1
        self.velocity = (0,0)
    def draw(self):
        pygame.draw.circle(screen, self.colour, (int(self.x),int(self.y)), self.size, self.thickness)
    def setSpeed(self,velocity,):
        self.velocity = velocity #in units of pixels/tick
    def getSpeed(self):
        return self.velocity
    def move(self,timepassed):
        self.x = self.x + self.velocity[0] * timepassed/20
        self.y = self.y + self.velocity[1] * timepassed/20
    def getLocation(self):
        return (self.x,self.y)

def linesFile(name):
    i = 0
    f = open(name, "r")
    for line in f:
        i+=1
    return i;

def applyTransformation(x,dx,dy,scaleFactor):
    #p = -math.pi/4
    #A = np.array([[math.cos(p),-math.sin(p)],[math.sin(p),math.cos(p)]])
    #x = applyTranslation(x,200,200)
    A = np.array([[1,-4],[1,1]])
    A = np.multiply(scaleFactor,A)
    x_bar = np.array([[x[0]],[x[1]]])
    b = np.dot(A,x_bar)
    b_tuple = b[0][0],b[1][0]
    b_tuple = applyTranslation(b_tuple,dx,dy)
    return b_tuple

def applyTranslation(x,dx,dy): #this is a computationally stupid way to do this
    x_bar = np.array([[x[0]],[x[1]],[1]])
    A = np.array([[1,0,dx],[0,1,dy]])
    b = np.dot(A,x_bar)
    return (b[0][0],b[1][0])

fl = open("posData.txt","r")
points = []
lines = linesFile("posData.txt")
for i in range(lines):
	line_i = fl.readline()
	s = line_i.split()
	x = s[0]
	y = s[1]
	points.append(applyTransformation((int(x),int(y)),deltax,deltay,scaleFactor))

print(points)
white = (0,0,0) #white means black
green = (0,255,0)
blue = (0,0,255)
dt = fps
screen = pygame.display.set_mode((800,600))
screen.fill(white)
balls = {1: 'null'}
for n in range(1000):
    x = 500*(random.random()) + 1
    y = 500*(random.random()) + 1
    balls[n] = Particle((x,y),2)
    balls[n].setSpeed((3,3))
ball = Particle((10,10),2)
ball.setSpeed((5,5))
ball.draw()

run = True
while run:

    accel = ser.readline()
    accel = accel.decode("UTF-8")
    accel = accel.strip("\r\n")
    accel = float(accel)
    accel = accel - 540
    accel_values.append(accel)

    if (len(accel_values) > 1):
        if(abs(accel_values[1]-accel_values[0]) > 10):
            vel[0] += (dt)*((accel_values[0]+accel_values[1])/2.0)

        graphPoints.append((startingPoint,100-accel_values[0]))
        graphPoints.append((startingPoint + dt, 100-accel_values[1]))
        startingPoint = startingPoint + dt
        if(startingPoint>400):
            startingPoint = 0
            graphPoints = []

        accel_values = []


    screen.fill(white)

    #text rendering

    scaleLabel = myfont.render("scaleFactor " + str(scaleFactor), 1, (0,255,0))
    dtLabel = myfont.render("dt " + str(dt), 1, (0,255,0))
    velLabel = myfont.render("vel " + str(vel), 1, (0,255,0))
    accelLabel = myfont.render("accel " + str(accel), 1, (0,255,0))
    accelValuesLabel = myfont.render("accel_values" + str(accel_values), 1, (0,255,0))

    screen.blit(dtLabel, (150,20))
    screen.blit(scaleLabel,(20,20))
    screen.blit(velLabel, (215, 20))
    screen.blit(accelLabel, (350,20))
    screen.blit(accelValuesLabel, (500,20))

    #basis vectors
    for n in range(int(width/10) + 1):
        pygame.draw.line(screen,blue,applyTransformation((0+10*n,0),deltax,deltay,scaleFactor),applyTransformation((0+10*n,height),deltax,deltay,scaleFactor))
    for n in range(int(height/10) + 1):
        pygame.draw.line(screen,blue,applyTransformation((0,0+10*n),deltax,deltay,scaleFactor),applyTransformation((width,0+10*n),deltax,deltay,scaleFactor))

    #for imsomature in balls:
    #    balls[imsomature].move(dt)
#        balls[imsomature].draw()
#    for c in balls:
#        if balls[c].getLocation()[0] > 800 or  balls[c].getLocation()[1] > 400 or balls[c].getSpeed()[1] == 0 or balls[c].getSpeed()[0] == 0:
#            x = random.randrange(350,410)
#            y = random.randrange(150,210)
#            balls[c] = Particle((x,y),2)
#            speed = (random.randrange(-5,6),random.randrange(-5,6))
#            balls[c].setSpeed(speed)


    #camera movement scaling and quit
    if(pygame.key.get_pressed()[pygame.K_w]): #negative of what you exepct because we want to move the "camera" not the object
        deltay += 10
        newTransform = True
    if(pygame.key.get_pressed()[pygame.K_s]):
        deltay -= 10
        newTransform = True
    if(pygame.key.get_pressed()[pygame.K_a]):
        deltax += 10
        newTransform = True
    if(pygame.key.get_pressed()[pygame.K_d]):
        deltax -= 10
        newTransform = True
    for a in pygame.event.get():
        if a.type == pygame.MOUSEBUTTONDOWN:
            if a.button == 4: scaleFactor = scaleFactor + .25
            if a.button == 5: scaleFactor = scaleFactor - .25
            newTransform = True
        if a.type == pygame.QUIT:
            run = False

    originalVectors.append((random.randrange(0,401),random.randrange(0,401)))
    points.append(applyTransformation(originalVectors[len(originalVectors) - 1],deltax,deltay,scaleFactor))
    #print(originalVectors)
    if(newTransform):
        points = []
        for c in originalVectors:
            points.append(applyTransformation(c,deltax,deltay,scaleFactor))
        newTransform = False

    #drawing lines on display
    if(len(points) > 1):
        pygame.draw.lines(screen,green,False, points,1)
    #drawing input graph
    if(len(graphPoints) > 1):
        pygame.draw.lines(screen,green,False,graphPoints,1)


    pygame.display.set_caption(str(clock.get_fps()))
    pygame.display.flip()
    dt = clock.tick_busy_loop(fps)
