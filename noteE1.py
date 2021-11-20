from tkinter import *
#from tkinter import ttk
import csv
from datetime import datetime


GUI = Tk()
GUI.title('โปรแกรมบันทึก')
GUI.geometry('500x400+500+50')

F1 = Frame(GUI)
F1.place(x=10, y=50)

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์',}


today = datetime.now().strftime('%a')
dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(dt)

L1 = Label(F1, text=days[today])
L1.pack()

L2 = Label(F1, text=dt)
L2.pack()







GUI.mainloop()