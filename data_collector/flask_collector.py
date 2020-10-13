from flask import Flask
import serial

app = Flask(__name__)

ser = serial.Serial(
  port = 'COM4', \
  baudrate = 9600, \
  parity = serial.PARITY_NONE, \
  stopbits = serial.STOPBITS_ONE, \
  bytesize = serial.EIGHTBITS, \
  timeout = 0)

@app.route('/')
def hello_world():
  temperature = 0.0
  try:
    temperature = float(ser.readline().decode('utf-8').rstrip("\n").rstrip("\r"))
  except:
    temperature = 0.0
  
  return { "temperature" : temperature }

if __name__ == "__main__":
  app.run('0.0.0.0', port=5000)