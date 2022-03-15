from tkinter import *

#akna seaded
aken = Tk()
aken.title('Tkinter "Hello World"')
aken.geometry("400x150")
aken.resizable(0, 0)

#tekst
lorem = 'Nimi: Karin Eegreid'
lorem2 = 'Rühm: A16'
lorem3 = '2016'

Label(aken, text=lorem, foreground="red", background="black", padx=30, font="Tahoma 26 bold italic").pack()
Label(aken, text=lorem2, foreground="red", background="black", padx=300, font="Tahoma 26 bold italic").pack()
Label(aken, text=lorem3, foreground="red", background="black",pady=10, padx=300, font="Tahoma 26 bold italic").pack()




aken.mainloop()