import serial
import time
ser = serial.Serial('COM7', 9600)
vel = [0,0,0]
velhistory = []
accelhistory = []
pos = [0,0,0]
offset = 524; #Engineering Note 8
time0 = time.time()
timef = 0
file = open("data.txt", "w")
while True:
	if(ser.in_waiting > 0):
		accel = str(ser.read(4), "UTF-8").strip() #Engineering Note 9
		accel = int(accel) - offset 
		if(abs(accel) <= 3): #Engineering Note 10
			accel = 0

		vel[0] = vel[0] + accel*1 #Engineering Note 11
		pos[0] = pos[0] + vel[0]*1
		velhistory.append(vel[0])
		accelhistory.append(accel)
		if(len(velhistory) > 100 and accel == 0): #Engineering Note 12
			if(len(set(velhistory)) <= 1):
				vel[0] = 0;
		if(len(velhistory) > 101):
			velhistory = []
		print(str(accel) + "\t" + str(vel[0]) + "\t" + str(pos[0]))
		file.write(str(accel) + "\t" + str(vel[0]) + "\t" + str(pos[0]) + "\n") #Engineering Note 13
		

		
#Engineering Note 14