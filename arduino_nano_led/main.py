import time

import pyfirmata

if __name__ == '__main__':
    board = pyfirmata.ArduinoNano("/dev/cu.usbserial-1410")

    port = board.digital[3]

    while True:
        port.write(1)
        time.sleep(1)
        port.write(0)
        time.sleep(3)
