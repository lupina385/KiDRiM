import tkinter as tk
from tkinter import messagebox as tkmb
import calculations as calc
import numpy as np

def calculate(angle, length, omega, epsilon, sav2, result_listbox):
    """It displays all outcomes needed in given labels"""
    result_listbox.delete(0, 'end')
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

    v = calc.velocities(angle, length, omega, sav2)
    if v == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości bądź prędkości kątowej!')
        return 0
    else:
        result_listbox.insert('end','Prędkości:')
        for i in range(1, 8):
            if i==2:
                result_listbox.insert('end', 'V_A: {} => '.format(v[i]) + 'VA = {}'.format(calc.value_of_vectors(v[i])))
            elif i==3:
                result_listbox.insert('end', 'V_B: {} => '.format(v[i]) + 'VB = {}'.format(calc.value_of_vectors(v[i])))
            elif i==6:
                result_listbox.insert('end', 'V_C: {} => '.format(v[i]) + 'VC = {}'.format(calc.value_of_vectors(v[i])))
            elif i==7:
                result_listbox.insert('end', 'V_D: {} => '.format(v[i]) + 'VD = {}'.format(calc.value_of_vectors(v[i])))


    a = calc.accelerations(angle, length, omega, epsilon, sav2)
    if a == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
        return 0
    else:
        result_listbox.insert('end','Przyspieszenia:')
        for i in range(1, 8):
            if i==2:
                result_listbox.insert('end', 'a_A: {} => aA'.format(a[i]) + ' = {}'.format(calc.value_of_vectors(a[i])))
            elif i==3:
                result_listbox.insert('end', 'a_B: {} => aB'.format(a[i]) + ' = {}'.format(calc.value_of_vectors(a[i])))
            elif i==6:
                result_listbox.insert('end', 'a_C: {} => aC'.format(a[i]) + ' = {}'.format(calc.value_of_vectors(a[i])))
            elif i==7:
                result_listbox.insert('end', 'a_D: {} => aD'.format(a[i]) + ' = {}'.format(calc.value_of_vectors(a[i])))


    acm = calc.accelerations_centre_mass(angle, length, omega, epsilon, sav2)
    if acm == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end','Przyspieszenia środków ciężkości:')
        result_listbox.insert('end','a_OA: {}'.format(acm[0]))
        result_listbox.insert('end','a_AB: {}'.format(acm[1]))
        result_listbox.insert('end','a_BS: {}'.format(acm[2]))
        result_listbox.insert('end','a_SC: {}'.format(acm[3]))
        result_listbox.insert('end','a_CD: {}'.format(acm[4]))

    F = calc.fictitious_forces(length, angle, omega, epsilon, sav2)
    if F == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end','Siły bezwładności (w środkach ciężkości):')
        result_listbox.insert('end', 'F_OA: {}'.format(np.round(F[0], 3)))
        result_listbox.insert('end', 'F_AB: {}'.format(np.round(F[1], 3)))
        result_listbox.insert('end', 'F_BS: {}'.format(np.round(F[2], 3)))
        result_listbox.insert('end', 'F_SC: {}'.format(np.round(F[3], 3)))
        result_listbox.insert('end', 'F_CD: {}'.format(np.round(F[4], 3)))

    N = calc.torques(length, angle, omega, epsilon, sav2)
    if N == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end','Momenty sił bezwładności (w środkach ciężkości):')
        result_listbox.insert('end', 'N_OA: {}'.format(np.round(N[0], 8)))
        result_listbox.insert('end', 'N_AB: {}'.format(np.round(N[1], 8)))
        result_listbox.insert('end', 'N_BS: {}'.format(np.round(N[2], 8)))
        result_listbox.insert('end', 'N_SC: {}'.format(np.round(N[3], 8)))
        result_listbox.insert('end', 'N_CD: {}'.format(np.round(N[4], 8)))

    f = calc.forces_of_interactions(length, angle, omega, epsilon, sav2)
    if f == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość kąta, długości, prędkości kątowej lub przyspieszenia kątowego!')
    else:
        result_listbox.insert('end', 'Siły oddziaływań członów:')
        result_listbox.insert('end', 'f_OA: {}'.format(np.round(f[0], 3)))
        result_listbox.insert('end', 'f_AB: {}'.format(np.round(f[2], 3)))
        result_listbox.insert('end', 'f_BS: {}'.format(np.round(f[3], 3)))
        result_listbox.insert('end', 'f_SC: {}'.format(np.round(f[5], 3)))
        result_listbox.insert('end', 'f_CD: {}'.format(np.round(f[6], 3)))


    n = calc.moments_of_impact(length, angle, omega, epsilon, sav2)
    result_listbox.insert('end', 'Momenty oddziaływań członów:')
    result_listbox.insert('end', 'n_OA: {}'.format(np.round(n[0], 3)))
    result_listbox.insert('end', 'n_AB: {}'.format(np.round(n[1], 3)))
    result_listbox.insert('end', 'n_BS: {}'.format(np.round(n[2], 3)))
    result_listbox.insert('end', 'n_SC: {}'.format(np.round(n[3], 3)))
    result_listbox.insert('end', 'n_CD: {}'.format(np.round(n[4], 3)))

    df = calc.driving_forces(length, angle, omega, epsilon, sav2)
    result_listbox.insert('end', 'Siły napędowe:')
    result_listbox.insert('end', 'Sn_OA= {}'.format(round(df[0], 3)))
    result_listbox.insert('end', 'Sn_AB= {}'.format(round(df[1], 3)))
    result_listbox.insert('end', 'Sn_BS= {}'.format(round(df[2], 3)))
    result_listbox.insert('end', 'Sn_SC= {}'.format(round(df[3], 3)))
    result_listbox.insert('end', 'Sn_CD= {}'.format(round(df[4], 3)))

    dm = calc.driving_moments(length, angle, omega, epsilon, sav2)
    result_listbox.insert('end', 'Momenty napędowe (w środkach ciężkości):')
    result_listbox.insert('end', 'Mn_OA= {}'.format(np.round(dm[0], 3)))
    result_listbox.insert('end', 'Mn_AB= {}'.format(np.round(dm[1], 3)))
    result_listbox.insert('end', 'Mn_BS= {}'.format(np.round(dm[2], 3)))
    result_listbox.insert('end', 'Mn_SC= {}'.format(np.round(dm[3], 3)))
    result_listbox.insert('end', 'Mn_CD= {}'.format(np.round(dm[4], 3)))
