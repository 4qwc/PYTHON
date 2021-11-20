from tkinter import *






class Box():
	''' Represent BOX '''

	def __init__(self, name):
		""" Imitialize the Box"""
		self.name = name

	def Set(self):
		print(self.name + " ชุดใหญ่")

	def BUTTON(self):
		GUI = Tk()
		GUI.title('การใช้ class')
		GUI.geometry('300x500')

		self.LB1 = Label(GUI, text='ปุ่มกด')
		self.LB1.pack()

		self.BT1 = Button(GUI, text='เปิดไฟ-1')
		self.BT1.pack(ipady=20,ipadx=80)

		GUI = mainloop()
		


my_box = Box('ของรางวัล')

print("นี่คิือ : " + my_box.name)
my_box.Set()



print('----------------------------')




# ( Inheritance)การสืบทอดคุณสมบัติ
class AAbox(Box):

	def __init__(self, name):
		super().__init__(name)

	def search(self):
		print(self.name + " สิ่งที่ค้นหาอยู่")

my_box = AAbox('กล่อง')

print(my_box.name + "เครื่องมือ")
my_box.Set()
my_box.search()


my_box.BUTTON()






