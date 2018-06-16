class Customer:
	def __init__(self):
		self.customer_name = ""
		self.mobileNumber = ""
		self.email = ""
	def set(self,name,mobileNumber,email):
		self.customer_name = name
		self.mobileNumber = mobileNumber
		self.email = email
		customersList.append(self)
