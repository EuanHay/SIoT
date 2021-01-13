import time
import board
import busio
import csv
import time
import serial
import adafruit_mma8451
 
 
# Initialize I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)
 
# Initialize MMA8451 module.
sensor = adafruit_mma8451.MMA8451(i2c)

#Read Arduino serial output
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

lastUpdated = time.time() - 10

while True:
    with open('01_sleep_data.csv', mode='a') as sensor_readings:
        sensor_write = csv.writer(sensor_readings, delimiter=',', quotechar='”', quoting=csv.QUOTE_MINIMAL)
        #timeElapsed = time.time() - lastUpdated
        #if timeElapsed >= 1:
            #lastUpdated = time.time()
        x, y, z = sensor.acceleration
        print('Acceleration: x={0:0.3f}m/s^2 y={1:0.3f}m/s^2 z={2:0.3f}m/s^2'.format(x, y, z))
        orientation = sensor.orientation
        print('Orientation: ', end='')
        if orientation == adafruit_mma8451.PL_PUF:
            print('Portrait, up, front')
        elif orientation == adafruit_mma8451.PL_PUB:
            print('Portrait, up, back')
        elif orientation == adafruit_mma8451.PL_PDF:
            print('Portrait, down, front')
        elif orientation == adafruit_mma8451.PL_PDB:
            print('Portrait, down, back')
        elif orientation == adafruit_mma8451.PL_LRF:
            print('Landscape, right, front')
        elif orientation == adafruit_mma8451.PL_LRB:
            print('Landscape, right, back')
        elif orientation == adafruit_mma8451.PL_LLF:
            print('Landscape, left, front')
        elif orientation == adafruit_mma8451.PL_LLB:
            print('Landscape, left, back')
        soundArray = [100, 100]
        if ser.in_waiting > 0:
            soundArray = []
            for i in range(2):
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                soundArray.append(line)
                
        sensor_write.writerow([time.time(),x,y,z,soundArray[0],soundArray[1]])
        time.sleep(1)
