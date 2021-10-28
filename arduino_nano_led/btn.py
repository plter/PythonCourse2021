import time

import pyfirmata
from pyfirmata import util

if __name__ == '__main__':
    board = pyfirmata.ArduinoNano("/dev/cu.usbserial-1410")
    it = util.Iterator(board)
    it.start()

    led_port = board.digital[3]
    btn_port = board.digital[4]
    btn_port.mode = pyfirmata.INPUT

    while True:
        v = btn_port.read()
        print(v)
        if v:
            led_port.write(0)
        else:
            led_port.write(1)
        time.sleep(0.1)
