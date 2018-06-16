class Reversation :
	def __init__(self, hotel,customer):
		self.hotel = hotel
		self.customer = customer

	def addToReversationList(self):
		subList = [self.hotel , self.customer]
		reservationList.append(subList)

	def deleteFromReversationL

	def reserveOperation (self):
		if self.hotel.thereIsRoom() == True:
			self.hotel.empty_rooms -= 1
			addToReversationList()
			return True
		else:
			return False
