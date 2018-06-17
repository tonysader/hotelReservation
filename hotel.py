import customer

class Hotel:
	hotelsList = []
	def __init__(self):
		self.number = 0
		self.hotel_name = ""
		self.city = ""
		self.total_rooms = 0
		self.empty_rooms =0
		self.customer = customer.Customer()
	def set(self,number,hotel_name, city,total_rooms,empty_rooms):
		self.number = number
		self.hotel_name = hotel_name
		self.city = city
		self.total_rooms = total_rooms
		self.empty_rooms =empty_rooms
		Hotel.hotelsList.append(self)
	def thereIsRoom(self):
		if self.empty_rooms > 0:
			return True
		else:
			return False
	@staticmethod
	def list_hotels_in_city(city_name):
	    # search for city in hotels and print hotel name, total number of rooms if found
	    for hotel in Hotel.hotelsList:
	        if hotel.city == city_name:
	            print "Hotel Name: " , hotel.hotel_name , " Hotel Total Rooms", hotel.total_rooms
	@staticmethod
	def list_resevrations_for_hotel(hotel_nameToSearch,revList):
	    # search for hotel_name in reservation list and print customer name
		for h in revList:
			if h[0].hotel_name == hotel_nameToSearch:
				print "Hotel Name: " , h[0].hotel_name , " --> Customer Name:" , h[1].customer_name
