from microbit import *
import WOM_Sensor_Kit

display.off()

while True:
    WOM_Sensor_Kit.WOM_rgb(1023, 1023, 1023)
    sleep(100)
