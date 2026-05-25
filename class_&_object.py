# CLASS AND OBJECT

class School(object):
	"""docstring for School"""
	name = ''
	address = ''
		
class Student(object):
	"""docstring for Student"""
	nis = 0
	name = ''
	address = ''

	def introduce(self):
		print("Hi, you can call me", self.name)

	def hi(self, name):
		print(f"Hi {name}, you can call me {self.name}")
		
school = School()
print(school.name)
print(school.address)

student = Student()
student.nis = 1234
student.name = "Adi"
print(student.nis)
print(student.name)
student.introduce()
student.hi("Nez")

student2 = Student()
student2.nis = 1235
student2.name = "Nez"
print(student2.nis)
print(student2.name)
student2.introduce()
student2.hi("Adi")

print(type(student))
print(type(student2))