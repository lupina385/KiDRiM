import tkinter as tk
from tkinter import messagebox as tkmb
import on_click as oc
from PIL import ImageTk, Image

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

# Reference image
image = Image.open("robot.jpg")
image = image.resize((400, 400), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
img_label = tk.Label(top, image=img, height=400, width=400)
img_label.grid(column=2, row=0, rowspan=17, sticky='n')

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

#velocity, acceleration and movement between B and C
sav2 = []
sav2.append(el_block(top, 's2:', 14))
sav2.append(el_block(top, 'V2:', 15))
sav2.append(el_block(top, 'a2:', 16))

result_frame = tk.Frame(top)
result_frame.grid(row=17, sticky='nesw', columnspan=3)

result_listbox = tk.Listbox(result_frame, font=20, width=65)
result_listbox.grid(sticky='nesw')
scrollbar = tk.Scrollbar(result_frame)
scrollbar.grid(column=1, row=0, sticky='ns')
result_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=result_listbox.yview)

a_button = tk.Button(text='Oblicz', font='arial', command=lambda: oc.calculate(angle, length, omega, epsilon, sav2, result_listbox))
a_button.grid(column=2, sticky='se')


top.mainloop()
