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



#if __name__ == '__main__':
top = tk.Tk()
top.title('Gloryfikowany kalkulator')
top.resizable(0,0)

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

label_results = tk.Label(top, text='', font = 'Arial', justify='left')
label_results.grid(columnspan=3)

a_button = tk.Button(text='Oblicz', font='arial', command=lambda: oc.calculate(angle, label_results))
a_button.grid(column=6, sticky='se')


top.mainloop()
