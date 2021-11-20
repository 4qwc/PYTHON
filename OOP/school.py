#school.py
# ตั้งชื่อ class

class Student:
	def __init__(self, name, lastname):
		self.name = name
		self.lastname = lastname
		self.exp = 0 # คะแนนประสบการณ์
		self.lesson = 0 # จำนวนคลาสที่เรียน



	def fullname(self):
		return 'ชื่อ:{} สกุล:{}'.format(self.name, self.lastname)


	def Coding(self):
		self.AddEXP()
		print('กำลังเขียนโปรแกรม...'.format(self.fullname()))

	def ShowEXP(self):
		print('{} ได้คะแนน {} exp (เรียนไป {} ครั้ง )'.format(self.name, self.exp, self.lesson))
	

	def AddEXP(self):
		self.exp += 10 # self.exp = self.exp + 10
		self.lesson += 1




# การสืบทอด คลาส สามารถใช้ฟังก์ชั่นใน class Student ได้
class SpecialStudent(Student):
	def __init__(self,name, lastname, father):
		super().__init__(name, lastname)

		self.father =father
		print('รู้ไหมฉันลูกใคร...! พ่อฉันชื่อ {}'.format(self.father))

		# สร้างทับฟังก์ชั่นด้านบน
	def AddEXP(self):
		self.exp += 30
		self.lesson += 2

######################## ส่วนนำไปแสดงผล ###########
# Day 1
print('----- Day 1 -----')
st1 = Student('Albert', 'Einstein')
print(st1.fullname())# การเรียกใช้

	 
#Day 2

print('----- Day 2 -----')
st2 = Student('Steve', 'Jobs')
print(st2.fullname())



#Day 3 
print('------ Day 3 -----')
for i in range(3):
	st1.Coding()

st2.Coding()	 
st1.ShowEXP()
st2.ShowEXP()



#Day 4 
print('------ Day 4 -----')
stp1 = SpecialStudent('Thomas', 'Eidson','Hitler')
print(stp1.fullname())


stp1.exp = 20
stp1.Coding()
stp1.ShowEXP()


