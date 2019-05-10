#import numpy as np
import math as m

def positions(angles, lengths): #a1=angle1 and so on
    """This function calculates positions of each points of a robot, based on given angles and lengths"""
    try:
        a=[]
        for angle in angles:
            a.append(float(angle.get_value()))

        l=[]
        for length in lengths:
            l.append(float(length.get_value()))

        if a[0]<-60 or a[0]>60 or a[1]<-30 or a[1]>45 or a[2]<-45 or a[2]>30:
            return 'error'

        coordinates = {} #it has key that is a symbol of a point and its value is stored as list: [x,y]
        coordinates['A'] = [0, l[0]]
        coordinates['B'] = [-round(m.sin(m.radians(a[0]))*l[1], 3), round(0.3+m.cos(m.radians(a[0]))*l[1], 3)]
        coordinates['C'] = [-round(-coordinates['B'][0]+m.sin(m.radians(a[0]+a[1]))*l[2], 3), round(coordinates['B'][1]+m.cos(m.radians(a[0]+a[1]))*l[2], 3)]
        coordinates['D'] = [-round(-coordinates['C'][0]+m.sin(m.radians(sum(a)))*l[3], 3), round(coordinates['C'][1]+m.cos(m.radians(sum(a)))*l[3], 3)]
        return coordinates
        
    except ValueError:
        return 'error'
