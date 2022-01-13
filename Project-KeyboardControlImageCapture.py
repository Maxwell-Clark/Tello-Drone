from typing import ValuesView
from djitellopy import tello
import keyPressModule as kp
import time
import cv2


kp.init()
me = tello.Tello()
me.connect()
print(me.get_battery())
global img
me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("j"): lr = -speed
    elif kp.getKey("l"): lr = speed

    if kp.getKey("s"): ud = -speed
    elif kp.getKey("w"): ud = speed
    
    if kp.getKey("i"): fb = speed
    elif kp.getKey("k"): fb = -speed
    
    if kp.getKey("d"): yv = -speed
    elif kp.getKey("a"): yv = speed

    if kp.getKey("q"): me.land(); time.sleep(3)
    if kp.getKey("e"): me.takeoff()
    
    if kp.getKey("z"): 
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)
    
    if kp.getKey("f"): print("tello battery is: " + me.get_battery())


    return [lr, ud, fb, yv]



while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)