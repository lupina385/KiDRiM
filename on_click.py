import tkinter as tk
from tkinter import messagebox as tkmb
import calculations as calc
import numpy as np

def calculate(angle, length, omega, epsilon, sav2, result_listbox):
    """It displays all outcomes needed in given labels"""
    np.set_printoptions(floatmode = 'maxprec_equal')
    cords = calc.positions(angle, length)
    if  cords == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość długości lub kąta!')
        return 0
    else:
        result_listbox.insert('end', 'Współrzędne członów:')
        result_listbox.insert('end', 'A( {} ; {} )'.format(cords['A'][0], cords['A'][1]))
        result_listbox.insert('end', 'B( {} ; {} )'.format(cords['B'][0], cords['B'][1]))
        result_listbox.insert('end', 'C( {} ; {} )'.format(cords['C'][0], cords['C'][1]))
        result_listbox.insert('end', 'D( {} ; {} )'.format(cords['D'][0], cords['D'][1]))

        #label[0].config(text=result)


    v = calc.velocities(angle, length, omega, sav2)
    if v == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości bądź prędkości kątowej!')
        return 0
    else:
        result_listbox.insert('end','Prędkości:')
        for i in range(1, 8):
            result_listbox.insert('end', 'V' + str(i) + ': {}'.format(v[i]))

    a = calc.accelerations(angle, length, omega, epsilon, sav2)
    if a == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
        return 0
    else:
        result_listbox.insert('end','Przyspieszenia:')
        for i in range(1, 8):
            result_listbox.insert('end','a' + str(i) + ': {}'.format(a[i]))

    acm = calc.accelerations_centre_mass(angle, length, omega, epsilon, sav2)
    if acm == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end','Przyspieszenia środków ciężkości:')
        result_listbox.insert('end','a01: {}'.format(acm[0]))
        result_listbox.insert('end','a23: {}'.format(acm[1]))
        result_listbox.insert('end','a34: {}'.format(acm[2]))
        result_listbox.insert('end','a45: {}'.format(acm[3]))
        result_listbox.insert('end','a67: {}'.format(acm[4]))

    F = calc.fictitious_forces(length, angle, omega, epsilon, sav2)
    if F == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end','Siły bezwładności:')
        for i in range(0, 5):
            result_listbox.insert('end', 'F' + str(i) + ': {}'.format(np.round(F[i], 3)))

    N = calc.torques(length, angle, omega, epsilon, sav2)
    if N == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end','Momenty sił bezwładności:')
        for i in range(0, 5):
            result_listbox.insert('end', 'N' + str(i) + ': {}'.format(np.round(N[i], 8)))

    f = calc.forces_of_interactions(length, angle, omega, epsilon, sav2)
    if f == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end', 'Siły oddziaływań członów:')
        for i in range(0, 7):
            result_listbox.insert('end', 'f' + str(i+1) + ': {}'.format(np.round(f[i], 3)))


    n = calc.moments_of_impact(length, angle, omega, epsilon, sav2)
    result_listbox.insert('end', 'Momenty oddziaływań członów:')
    for i in range(0, 7):
        result_listbox.insert('end', 'n' + str(i+1) + ': {}'.format(np.round(n[i], 3)))

    df = calc.driving_forces(length, angle, omega, epsilon, sav2)
    result_listbox.insert('end', 'Siły napędowe:')
    for i in range(0, 7):
        result_listbox.insert('end', 'SN' + str(i+1) + '= {}'.format(round(df[i], 3)))

    dm = calc.driving_moments(length, angle, omega, epsilon, sav2)
    result_listbox.insert('end', 'Momenty napędowe:')
    for i in range(0, 7):
        gitresult_listbox.insert('end', 'Mo' + str(i+1) + '= {}'.format(np.round(dm[i], 3)))
