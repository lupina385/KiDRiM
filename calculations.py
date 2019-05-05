#import numpy as np
import math as m

omega1, omega2, omega3 = 2.0, -3.0, 1.0
epsilon1, espilon2, epsilon3 = 1.0, 1.5, 2.5
oa, ab, bc, cd = 0.3, 0.2, 0.15, 0.15

def positions(a1, a2, a3): #a1=angle1 and so on
    """This function calculates positions of each points of a robot, based on given angles"""
    try:
        input1 = float(a1)
        input2 = float(a2)
        input3 = float(a3)

        if input1<-60 or input1>60 or input2<-30 or input2>45 or input3<-45 or input3>30:
            return 'error'

        coordinates = {} #it has key that is a symbol of a point and its value is stored as list: [x,y]
        coordinates['A'] = [0, oa]
        coordinates['B'] = [-round(m.sin(m.radians(input1))*ab, 3), round(oa+m.cos(m.radians(input1))*ab, 3)]
        coordinates['C'] = [-round(-coordinates['B'][0]+m.sin(m.radians(input1+input2))*bc, 3), round(coordinates['B'][1]+m.cos(m.radians(input1+input2))*bc, 3)]
        coordinates['D'] = [-round(-coordinates['C'][0]+m.sin(m.radians(input1+input2+input3))*cd, 3), round(coordinates['C'][1]+m.cos(m.radians(input1+input2+input3))*cd, 3)]
        return coordinates
    except ValueError:
        return 'error'
