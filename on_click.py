import tkinter as tk
from tkinter import messagebox as tkmb
import calculations as calc

def calculate(angle, label):
    a1 = angle[0].get_value()
    a2 = angle[1].get_value()
    a3 = angle[2].get_value()

    if calc.positions(a1, a2, a3) == 'error':
        tkmb.showinfo('Błąd', 'Wprowadzono nieprawidłową wartość jednego lub wielu kątów!'+a1)
        return 0
    else:
        cords = calc.positions(a1, a2, a3)
        result = 'Współrzędne członów:\nA( {} ; {} )\nB( {} ; {} )\nC( {} ; {} )\nD( {} ; {} )'.format(cords['A'][0], cords['A'][1], cords['B'][0], cords['B'][1], cords['C'][0], cords['C'][1], cords['D'][0], cords['D'][1])
        label.config(text=result)

# def test():
#     import main
#     main.label_results.config(text='xd')
