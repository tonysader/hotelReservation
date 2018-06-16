

class Hotel:
	def __init__(self):
		self.number = 0
		self.hotel_name = ""
		self.city = ""
		self.total_rooms = 0
		self.empty_rooms =0
		self.customer = Customer()
	def set(self,number,hotel_name, city,total_rooms,empty_rooms):
		self.number = number
		self.hotel_name = hotel_name
		self.city = city
		self.total_rooms = total_rooms
		self.empty_rooms =empty_rooms
		hotelsList.append(self)
	def thereIsRoom(self):
		if self.empty_rooms > 0:
			return True
		else:
			return False
	def reserve_room (self, customer):
		if self.thereIsRoom() == True:
			self.empty_rooms -= 1
			addToReservationList(self.hotel_name,customer.customer_name)
			return True
		else:
			return False
