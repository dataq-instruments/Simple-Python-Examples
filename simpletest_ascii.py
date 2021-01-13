import serial
import keyboard
import time
import sys

#Press key 'x' to EXIT
#since serDataq.readline waits until a line is received, low sample rate makes the program slow in response to key stroke

CONST_SER_PORT = 'COM11'   #get the com port from device manger and enter it here

serDataq = serial.Serial(CONST_SER_PORT)

serDataq.write(b"stop\r")        #stop in case device was left scanning
serDataq.write(b"eol 1\r") 
serDataq.write(b"encode 1\r")    #set up the device for ascii mode
serDataq.write(b"slist 0 0\r")   #scan list position 0 channel 0 thru channel 7
serDataq.write(b"slist 1 1\r")
serDataq.write(b"slist 2 2\r")
serDataq.write(b"slist 3 3\r")
serDataq.write(b"slist 4 4\r")
serDataq.write(b"slist 5 5\r")
serDataq.write(b"slist 6 6\r")
serDataq.write(b"slist 7 7\r")
serDataq.write(b"srate 6000\r") 
serDataq.write(b"dec 500\r") 
serDataq.write(b"deca 3\r") 
time.sleep(1)  
serDataq.read_all()              #flush all command responses
serDataq.write(b"start\r")           #start scanning

while True:
    try:
        if keyboard.is_pressed('x'):    #if key 'x' is pressed, stop the scanning and terminate the program
            serDataq.write(b"stop\r")
            time.sleep(1)           
            serDataq.close()
            print("Good-Bye")
            break
        else:
            i= serDataq.inWaiting()
            if i>0:
                line = serDataq.readline().decode("utf-8")
                print(line)
            pass
    except:
        pass
