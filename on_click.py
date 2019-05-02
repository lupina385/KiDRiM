import tkinter as tk
from tkinter import messagebox as tkmb
import calculations as calc

def positions(a1, a2, a3):
    if calc.positions(a1, a2, a3) == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość!')
    else:
        cords = calc.positions(a1, a2, a3)
        tkmb.showinfo('Wyniki', 'A( {} ; {} )\nB( {} ; {} )\nC( {} ; {} )\nD( {} ; {} )'.format(cords['A'][0], cords['A'][1], cords['B'][0], cords['B'][1], cords['C'][0], cords['C'][1], cords['D'][0], cords['D'][1]))
