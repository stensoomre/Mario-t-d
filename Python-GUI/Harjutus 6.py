#graafiline
#Sten Soomre
#15.03.22

from tkinter import *

#akna seaded
aken = Tk()
aken.title('taani')


#lõuendi loomine
louend = Canvas(aken, width=500, height=500)
louend.pack()


louend.create_rectangle(15, 20, 200, 120, fill='red', )
louend.create_line(90, 20, 90, 120, fill='white', width=20)
louend.create_line(15, 70, 200, 70, fill='white', width=20)

#pildi lisamine
minu_pilt = PhotoImage(file='taanilinn.png')
louend.create_image(150, 150, anchor=NW, image=minu_pilt)

aken.mainloop()


