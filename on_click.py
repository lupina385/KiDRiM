import tkinter as tk
from tkinter import messagebox as tkmb
import calculations as calc
import numpy as np

def calculate(angle, length, omega, epsilon, label):
    """It displays all outcomes needed in given label"""
    a1 = angle[0].get_value()
    a2 = angle[1].get_value()
    a3 = angle[2].get_value()

    cords = calc.positions(angle, length)
    if  cords == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość długości lub kąta!')
        return 0
    else:
        result = 'Współrzędne członów:\nA( {} ; {} )\nB( {} ; {} )\nC( {} ; {} )\nD( {} ; {} )'.format(cords['A'][0], cords['A'][1], cords['B'][0], cords['B'][1], cords['C'][0], cords['C'][1], cords['D'][0], cords['D'][1])
        label[0].config(text=result)

    v = calc.velocities(angle, length, omega)
    if v == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości bądź prędkości kątowej!')
        return 0
    else:
        result = '\nPrędkości: '
        i=0
        for vel in v:
            result += '\n==V' + str(i) + '==\n{}'.format(vel)
            i+=1
        label[1].config(text=result)

    a = calc.accelerations(angle, length, omega, epsilon)
    if a == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
        return 0
    else:
        result = '\nPrzyspieszenia:'
        i=0
        for acc in a:
            result += '\n==a' + str(i) + '==\n{}'.format(acc)
            i+=1
        label[2].config(text=result)
