import tkinter as tk
from tkinter import messagebox as tkmb
import on_click as oc

top = tk.Tk()

top.title('Gloryfikowany kalkulator')
top.resizable(0,0)

label_angle1 = tk.Label(top, text='Kąt 1:', font = 'Arial')
label_angle1.grid()

label_angle2 = tk.Label(top, text='Kąt 2:', font = 'Arial')
label_angle2.grid(row=1)

label_angle3 = tk.Label(top, text='Kąt 3:', font = 'Arial')
label_angle3.grid(row=2)

entry_angle1 = tk.Entry(top, width=10)
entry_angle1.grid(column=1, row=0)

entry_angle2 = tk.Entry(top, width=10)
entry_angle2.grid(column=1, row=1)

entry_angle3 = tk.Entry(top, width=10)
entry_angle3.grid(column=1, row=2)

label_results = tk.Label(top, text='', font = 'Arial', justify='left')
label_results.grid()

# image = tk.Canvas(top, width=300, height=300)
# image.grid(column=2, row=0, columnspan=5, rowspan=30)
# #Cartesian cooridnates
# image.create_line(0, 290, 300, 290, fill='#000000') #x axis
# image.create_line(20, 0, 20, 300, fill='#000000') #y axs
# #Scheme of the robot
# image.create_line(20, 300, 20, 150, fill='#FF0000') #OA
# image.create_line(20, 150, 200, 120, fill='#FF0000') #AB

a_button = tk.Button(text='Oblicz', font='arial', command=lambda: oc.positions(entry_angle1.get(), entry_angle2.get(), entry_angle3.get(), label_results))
a_button.grid(column=6, sticky='se')

top.mainloop()
