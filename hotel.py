

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
	@staticmethod
	def list_hotels_in_city(city_name):
	    # search for city in hotels and print hotel name, total number of rooms if found
	    for hotel in hotelsList:
	        if hotel.city == city_name:
	            print(hotel.hotel_name,hotel.total_rooms)
	@staticmethod
	def list_resevrations_for_hotel(hotel_name):
	    # search for hotel_name in reservation list and print customer name
	    for hotel in hotelsList:
	    	if hotel_name == hotel.hotel_name:
	    		for reservation in reservationList:
	    			print(reservation[1])
