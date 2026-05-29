# Encapsulation

class BankAccount:
	"""docstring for BankAccount"""
	__no = ""
	__balance = 0

	def __init__(self, no):
		self.__no = no

	@property
	def balance(self):
		return self.__balance

	@property
	def no(self):
		return self.__no

	def topup(self, topup_amount):
		self.__balance += topup_amount
	
	def cashout(self, cashout_amount):
		if cashout_amount > self.__balance:
			raise ValueError("Not enough balance")
		self.__balance -= cashout_amount

bank_account = BankAccount("Nez")
print(bank_account.no)
print(bank_account.balance)

bank_account.topup(50)
print(bank_account.balance)

bank_account.cashout(10)
print(bank_account.balance)
