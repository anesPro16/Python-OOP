# Decorator

class SimpleCount:
	"""docstring for SimpleCount"""
	@staticmethod
	def add(a, b):
		return a + b

print(SimpleCount.add(3,3))

class BankAccount:
	"""docstring for BankAccount"""
	no = ''
	balance = 0
	active = True

	def __init__(self, no, balance):
		self.no = no
		self.balance = balance

	@classmethod
	def disabled(cls, no, balance):
		result = cls(no, balance)
		result.active = False
		return result

bank_account = BankAccount("12345", 1000000)
bank_account.balance = -100000
print(f"{bank_account.no}, {bank_account.balance}, {bank_account.active}")

bank_account2 = BankAccount.disabled("12345", 1000000)
print(f"{bank_account2.no}, {bank_account2.balance}, {bank_account2.active}")

class Category:
	"""docstring for Category"""
	__name = ""

	@property
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if name == "":
			raise ValueError("name can\'t be empty")
		self.__name = name

category = Category()
category.name = "Food"
print(category.name)
print(category.name)