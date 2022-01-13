from typing import ValuesView
from djitellopy import tello
import keyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("j"): lr = -speed
    elif kp.getKey("l"): lr = speed

    if kp.getKey("s"): ud = -speed
    elif kp.getKey("w"): ud = speed
    
    if kp.getKey("i"): fb = -speed
    elif kp.getKey("k"): fb = speed
    
    if kp.getKey("d"): yv = -speed
    elif kp.getKey("a"): yv = speed

    if kp.getKey("q"): me.land()
    if kp.getKey("e"): me.takeoff()

    return [lr, ud, fb, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
