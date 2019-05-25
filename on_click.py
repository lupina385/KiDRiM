import tkinter as tk
from tkinter import messagebox as tkmb
import calculations as calc
import numpy as np

def calculate(angle, length, omega, epsilon, sav2, label):
    """It displays all outcomes needed in given labels"""
    np.set_printoptions(floatmode = 'maxprec_equal')
    cords = calc.positions(angle, length)
    if  cords == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość długości lub kąta!')
        return 0
    else:
        result = 'Współrzędne członów:\nA( {} ; {} )\nB( {} ; {} )\nC( {} ; {} )\nD( {} ; {} )'.format(cords['A'][0], cords['A'][1], cords['B'][0], cords['B'][1], cords['C'][0], cords['C'][1], cords['D'][0], cords['D'][1])
        label[0].config(text=result)

    v = calc.velocities(angle, length, omega, sav2)
    if v == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości bądź prędkości kątowej!')
        return 0
    else:
        result = 'Prędkości: '
        for i in range(1, 8):
            result += '\n===V' + str(i) + '===\n{}'.format(v[i])
        label[1].config(text=result)

    a = calc.accelerations(angle, length, omega, epsilon, sav2)
    if a == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
        return 0
    else:
        result = 'Przyspieszenia:'
        for i in range(1, 8):
            result += '\n===a' + str(i) + '===\n{}'.format(a[i])
        label[2].config(text=result)

    acm = calc.accelerations_centre_mass(angle, length, omega, epsilon, sav2)
    if acm == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result = 'Przysp. śr. ciężkości:'
        result += '\n===a01===\n{}'.format(acm[0])
        result += '\n===a23===\n{}'.format(acm[1])
        result += '\n===a34===\n{}'.format(acm[2])
        result += '\n===a45===\n{}'.format(acm[3])
        result += '\n===a67===\n{}'.format(acm[4])
        label[3].config(text=result)

    F = calc.fictitious_forces(length, angle, omega, epsilon, sav2)
    N = calc.torques(length, angle, omega, epsilon, sav2)
    if N == 'error' or F == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result = 'Siły bezwł. i momenty sił:'
        for i in range(0, 5):
            result += '\n===F' + str(i) + '===\n{}'.format(np.round(F[i], 3))
        for i in range(0, 5):
            result += '\n===N' + str(i) + '===\n{}'.format(np.round(N[i], 8))
        label[4].config(text=result)

    f = calc.forces_of_interactions(length, angle, omega, epsilon, sav2)
    if f == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result = 'Siły oddziaływań członów:'
        for i in range(0, 7):
            result += '\n===f' + str(i+1) + '===\n{}'.format(np.round(f[i], 3))
        label[5].config(text=result)

    df = calc.driving_forces(length, angle, omega, epsilon, sav2)
    result = 'Siły napędowe:'
    for i in range(0, 7):
        result += '\nSN' + str(i+1) + '= {}'.format(round(df[i], 3))
    label[6].config(text=result)
