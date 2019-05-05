#import numpy as np
import math as m

omega1, omega2, omega3 = 2.0, -3.0, 1.0
epsilon1, espilon2, epsilon3 = 1.0, 1.5, 2.5
oa, ac, bc, cd = 0.3, 0.2, 0.15, 0.15

def positions(a1, a2, a3): #a1=angle1 and so on
#"""This function calculates positions of each points of a robot, based on given angles"""
    try:
        input1 = float(a1)
        input2 = float(a2)
        input3 = float(a3)
        cooridnates = {} #it has key that is a symbol of a point and its value is stored as list: [x,y]
        cooridnates['A'] = [0, oa]
        cooridnates['B'] = [round(m.sin(m.radians(input1)), 3), round(m.cos(m.radians(input1)), 3)]
        cooridnates['C'] = [round(m.sin(m.radians(input1-input2)), 3), round(m.cos(m.radians(input1-input2)), 3)]
        cooridnates['D'] = [round(m.sin(m.radians(input1-input2+input3)), 3), round(m.cos(m.radians(input1-input2+input3)), 3)]
        return cooridnates
    except ValueError:
        return 'error'
