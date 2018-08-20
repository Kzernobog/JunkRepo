import serial as comm
import pdb
path = '/dev/tty.usbserial-A5XK3RJT'
with comm.Serial(path, baudrate=38400)as ser:
    if ser.is_open:
        print("opened....")
        #command = b'$SP;' #- worked
        #command = 0x2453503B - didnt work
        command = b'\x24\x53\x50\x3B' #- worked
        ser.write(command)
        recieve = ser.read(4)
        print("reached here.....")
        print(recieve)
