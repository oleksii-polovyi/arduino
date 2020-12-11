from flask import Flask
from pyfirmata import Arduino, util
import time

app = Flask(__name__)
board = Arduino('COM4')

it = util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
board.analog[1].enable_reporting()

@app.route('/')
def collector():

    temperature = 0.0
    light = 0.0

    light_calibration = 125
    temperature_calibration = 150

    try:
        temperature = round(board.analog[1].read() * temperature_calibration) 
        light = round(board.analog[0].read() * light_calibration) 

    except:
        temperature = 0.0
        light = 0.0

    return {"temperature": temperature, "light": light}


if __name__ == "__main__":
    app.run('0.0.0.0', port=5000)
