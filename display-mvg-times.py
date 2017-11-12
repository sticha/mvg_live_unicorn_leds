# -*- coding: utf-8 -*-

import time
import MVGLive
import unicornhat as unicorn

unicorn.set_layout(unicorn.AUTO)
unicorn.clear()
unicorn.rotation(180)
unicorn.brightness(0.6)
width,height=unicorn.get_shape()


def getCurrentTransports():
    foo = MVGLive.MVGLive()
    liveData = foo.getlivedata("Ackermannstraße")
    times = []
    for transport in liveData:
        if transport['product'] == "Tram":
            goesToPetuelring = False
            if transport['destination'] == "Petuelring":
                goesToPetuelring = True
            times.append((transport['time'], goesToPetuelring))
    return times

departingColour = (255, 0, 0) # red
evenTimeColour = (0, 255, 255) # light blue
goingNorthColour = (0, 0, 255) # blue
goingSouthColour = (0, 255, 0) # green
defaultColour = (255, 102, 0) # orange

def visualizeTimes(width, height):
    unicorn.clear()
    i = 0
    for transport in getCurrentTransports():
        if i >= height:
            break
        time = transport[0]
        goingToPetuelring = transport[1]
        for t in range((time/2) + 1):
            if t >= width:
                break
            colourToSet = defaultColour
            if time == 0:
                colourToSet = departingColour
            elif t == ((time/2)) and time%2 == 0:
                colourToSet = evenTimeColour
            elif t <= 2:
                if goingToPetuelring:
                    colourToSet = goingNorthColour
                else:
                    colourToSet = goingSouthColour
            setColourAt(t, i, colourToSet)
        i = i+1
    unicorn.show()

def setColourAt(t, i, colour):
    unicorn.set_pixel(t, i, colour[0], colour[1], colour[2])

while 1==1:
    visualizeTimes(width, height)
    time.sleep(1)
