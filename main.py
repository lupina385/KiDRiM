import tkinter as tk
from tkinter import messagebox as tkmb
import on_click as oc

class el_block:
    def __init__(self, window, name, i):
        self.label = tk.Label(window, text=name, font='Arial')
        self.label.grid(row=i)
        self.entry = tk.Entry(window, width=10)
        self.entry.grid(column=1, row=i)

    def get_value(self):
        return self.entry.get()

top = tk.Tk()
top.title('Gloryfikowany kalkulator')
top.resizable(0, 0)

# Angles
angle =[]
for i in range(0, 3):
    angle.append(el_block(top, 'Kąt {}:'.format(str(i+1)), i))

#Lenghts
length =[]
for i in range(0, 4):
    length.append(el_block(top, 'Długość {}. odcinka:'.format(str(i+1)), i+4))

#Angular speeds
omega =[]
for i in range(0, 3):
    omega.append(el_block(top, 'Omega {}:'.format(str(i+1)), i+8))

#Angular acceleration
epsilon =[]
for i in range(0, 3):
    epsilon.append(el_block(top, 'Epsilon {}:'.format(str(i+1)), i+11))

label_result = []
label_result.append(tk.Label(top, text='', font = 'Arial', justify='left')) #positions
label_result[0].grid(column=2, row=0, rowspan=999, sticky='nw')
label_result.append(tk.Label(top, text='', font = 'Arial', justify='left')) #velocities
label_result[1].grid(column=3, row=0, rowspan=999, sticky='nw')
label_result.append(tk.Label(top, text='', font = 'Arial', justify='left')) #accelerations
label_result[2].grid(column=4, row=0, rowspan=999, sticky='nw')

a_button = tk.Button(text='Oblicz', font='arial', command=lambda: oc.calculate(angle, length, omega, epsilon, label_result))
a_button.grid(column=10, sticky='se')


top.mainloop()
