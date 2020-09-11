import serial
from time import sleep

ser = serial.Serial(
  port = 'COM4', \
  baudrate = 9600, \
  parity = serial.PARITY_NONE, \
  stopbits = serial.STOPBITS_ONE, \
  bytesize = serial.EIGHTBITS, \
  timeout = 0)

try:
  while True:
    line = ser.readline().decode('utf-8').rstrip("\n")
    if line != '':
      print(line)
  
      with open("data.txt", "a") as data_txt:
        data_txt.write(line)

except KeyboardInterrupt:
  pass

ser.close()
