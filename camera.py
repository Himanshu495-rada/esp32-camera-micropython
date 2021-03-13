import machine
from machine import Pin
import camera
import time

flash = Pin(4, Pin.OUT)
flash.value(1)
time.sleep(1)
flash.value(0)

uos.mount(machine.SDCard(), "/sd")  #mount the SD card
camera.init()
camera.quality(10)
camera.framesize(9)
count = 0
while True:
    if count == 2200:
        print("Completed")
        break
    flash.value(1)
    pic = camera.capture()
    flash.value(0)
    file = open("/sd/pics/"+str(count)+".jpg", "wb")
    file.write(pic)
    file.close()
    print(count, " done")
    count += 1
    time.sleep(1)

print("done")
