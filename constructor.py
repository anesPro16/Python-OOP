# Constructor

class Student:
	"""docstring for Student"""
	nis = 0
	name = ''

	def __init__(self, nis, name):
		self.nis = nis
		self.name = name

	def __str__(self):
		return f"Student : {self.nis} --- {self.name}"

	def __eq__(self, other):
		return self.nis == other.nis and self.name == other.name

student = Student(1234, "Nez")

print(student.nis)
print(student.name)

print(student)

student2 = Student(1235, "Nez")
print(student == student2)

class BankAccount:
	"""docstring for BankAccount"""
	no = ''
	balance = 0

	def __init__(self, no,  balance=0):
		self.no = no
		if balance < 0:
			try:
				print("Balance is not positive!")
			except:
				ValueError("Balance is not positive!")

		self.no = no
		self.balance = balance

nez = BankAccount("012345", 1000000)
putra = BankAccount("0123456", -1000000)