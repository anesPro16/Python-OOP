# Inheritance

class Vehicle:
	"""docstring for Vehicle"""
	def __init__(self, merk, year):
		self.merk = merk
		self.year = year

	def info(self):
		return f"Merk : {self.merk}, Year : {self.year}"

	def turn_on(self):
		print(f"{self.merk} is turn on")

class Car(Vehicle):
	"""docstring for Car"""
	def __init__(self, merk, year, colour):
		super().__init__(merk, year)
		self.colour = colour

	def sirine(self):
		print(f"Car {self.info()} have sirine")

class Motorcycle(Vehicle):
	"""docstring for Motorcycle"""
	def sirine(self):
		print(f"Motorcycle {self.info()} have sirine")

	def turn_on(self):
		print(f"{self.merk} is turn on by auto")
		
riyoncar = Car("Riyoncar", 2045, "White")
riyoncar.turn_on()
riyoncar.sirine()

motoRiyon = Motorcycle("MotoRiyon", 2045)
motoRiyon.turn_on()
motoRiyon.sirine()

class Employee:
	"""docstring for Employee"""
	def __init__(self, name, fee):
		self.name = name
		self.fee = fee

class EmployeeStaff(Employee):
	"""docstring for EmployeeStaff"""
	# def __init__(self, staff_id):
	# 	self.staff_id = staff_id

class Manager(EmployeeStaff):
	"""docstring for Manager"""
	# def __init__(self, manager_id):
	# 	self.manager_id = manager_id

class VicePresident(Manager):
	"""docstring for VicePresident"""
	# super(VicePresident, self).__init__()
	# self.vice_manager_id = vice_manager_id
		
john = Employee("John", 10000000)
nez = EmployeeStaff("Nez", 11000000)
outr = Manager("Outr", 12000000)
yonn = VicePresident("yonn", 12500000)

print(isinstance(john, Employee))
print(isinstance(nez, Employee))
print(isinstance(outr, Employee))
print(isinstance(yonn, Employee))

class Run(object):
	"""docstring for Run"""
	def run(self):
		print("He is running")

class Swim(object):
	"""docstring for Swim"""
	def swim(self):
		print("He is swimming")

class Athlete(Run, Swim):
	"""docstring for Athlete"""
	def __init__(self, name):
		self.name = name

outr = Athlete("Outr")
outr.run()
outr.swim()

class A:
	def method(self):
		print("Method from A")

class B(A):
	def method(self):
		print("Method from B")

class C(A):
	def method(self):
		print("Method from C")

class D(B,C):
	pass

d = D()
d.method()
