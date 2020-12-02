import pyfirmata
import time
from itertools import chain

board = pyfirmata.Arduino('COM4')

next_letter = [-300];
next_word = [-700];
dot = 100;
dash = 300;
gap = -100;

H = [dot, gap, dot, gap, dot, gap, dot];
E = [dot];
L = [dot, gap, dash, gap, dot, gap, dot];
O = [dash, gap, dash, gap, dash];
W = [dot, gap, dash, gap, dash];
R = [dot, gap, dash, gap, dot];
D = [dash, gap, dot, gap, dot];

HelloWorld_2D_list = [H, next_letter, E, next_letter, L, next_letter, L, next_letter, O, next_word, W, next_letter, O, next_letter, R, next_letter, L, next_letter, D]
HelloWorld = list(chain.from_iterable(HelloWorld_2D_list))
print(HelloWorld)

while True:
    try:
        for signal in HelloWorld:
            if signal < 0:
               board.digital[13].write(0)
               time.sleep(-signal/1000)
            else:
               board.digital[13].write(1)
               time.sleep(signal/1000)
        print("LED code sent")
        exit(0)
    except:
        exit(0)