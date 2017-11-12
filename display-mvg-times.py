# -*- coding: utf-8 -*-

import time
import MVGLive
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.clear()
unicorn.rotation(180)
unicorn.brightness(0.6)
width,height=unicorn.get_shape()


def getCurrentTimes():
    foo = MVGLive.MVGLive()
    liveData = foo.getlivedata("Fröttmaning")
    times = []
    for subway in liveData:
        if subway['direction'] == "1":
            times.append(subway['time'])
    return times

def visualizeTimes(width, height):
    unicorn.clear()
    i = 0
    for time in getCurrentTimes():
        if i >= height:
            break
        for t in range((time/2) + 1):
            bb = 255
            if t >= width:
                break
            rr = 0
            if t <= 2:
                rr = 255
            gg = 0
            if t == ((time/2)):
                if time%2 == 0:
                    gg = 255
            if time == 0:
                rr = 255
                gg = 69
                bb = 0
            unicorn.set_pixel(t, i, rr, gg, bb)
        i = i+1
    unicorn.show()

while 1==1:
    visualizeTimes(width, height)
    time.sleep(1)
