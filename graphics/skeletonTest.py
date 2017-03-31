import serial
import time
import msvcrt
ser = serial.Serial('COM7', 9600)
accel_values = []
vel_values = []
vel = [0,0,0]
pos = [0,0,0]
dt = 0
time0 = time.time()
run = True

def calibrateAccel():
    running_avg = measure_accel()
    for i in range(50):
        running_avg=(running_avg + measure_accel())/2
    return running_avg

def measure_accel():
    al = ser.readline()
    al = al.decode("UTF-8")
    al = al.strip("\r\n")
    al = float(al)
    return al


offset = calibrateAccel()


#loop begins here
while run:
    accel = measure_accel()
    accel = accel - offset
    accel_values.append(accel)
    if (len(accel_values) > 1):
        if(abs(accel_values[1]-accel_values[0]) > 15):
            vel[0] += (dt)*((accel_values[0]+accel_values[1])/2.0)
    
        accel_values = []
    if (abs(vel[0] - 0) < .5):
        vel[0] = 0
    vel_values.append(vel[0])
    
    if (len(vel_values) > 1):
        if(abs(vel_values[1]-vel_values[0]) > 1):
            pos[0] += (dt)*((vel_values[0]+vel_values[1])/2.0)
     
        vel_values = [] 
    if(msvcrt.kbhit()):
        run = False
    print(str(dt))
    print("vel :" + str(vel[0]) + " accel:" + str(accel) + " pos:" + str(pos[0]))
    time1 = time.time()
    dt = (time1-time0)
    time0 = time1
   

