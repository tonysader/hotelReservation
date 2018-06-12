import smtplib
import conf

hotelsList = []
customersList = []
reservationList = []

def addToReservationList(hotelName,customer):
	subList = [hotelName,customer]
	reservationList.append(subList)
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


def add_hotel(number,hotel_name, city,total_rooms,empty_rooms):
	h = Hotel()
	h.set(number,hotel_name,city,total_rooms,empty_rooms)
	return h
def add_customer(customer_name):
    # add customer_name to customers list
    c = Customer()
    c.setCustomer(customer_name)
    return c
def reserve_room (hotel, customer):
    	# loop and check if there is empty_rooms in hotel_name 
    # if no rooms, 
    #     return False
    # else reserve a new room in hotel_name for customer_name
    #         add new reservation into the reservation list
    #          update the empty rooms in hotel_name
    #          return True
    return hotel.reserve_room(customer)
def add_new_reservation(hotel, customer):
    	if reserve_room(hotel, customer):
			subject = "Hotel reservation"
			msg = "Hello there your reservation has successfuly completed, Hope you enjoy!"
			recieverEmail = customer.email
			sendEmail(subject,msg,recieverEmail) 
			print ("confirmation")
    	else:
   	    	print ("sorry no rooms available")

def list_hotels_in_city(city_name):
    # search for city in hotels and print hotel name, total number of rooms if found
    for hotel in hotelsList:
        if hotel.city == city_name:
            print(hotel.hotel_name,hotel.total_rooms)
def list_resevrations_for_hotel(hotel_name):
    # search for hotel_name in reservation list and print customer name
    for hotel in hotelsList:
    	if hotel_name == hotel.hotel_name:
    		for reservation in reservationList:
    			print(reservation[1])

def sendEmail(subject,msg,recieverEmail):
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(conf.email,conf.pas)
		message = 'Subject: {}    {}'.format(subject,msg)
		server.sendmail(conf.email, recieverEmail ,message)
		server.quit()
		print("Email was sent successfuly")
	except:
		print("Error in sending the email")

def main():
	hotel1 = add_hotel(1,"hotel1", "Paris",32,6)
	hotel2 = add_hotel(2,"hotel2", "Cairo",42,7)
	customer1 = Customer()
	#not real mobile number
	customer1.set("Tony","+5324214","tony.dx.3379@gmail.com")
	add_new_reservation(hotel1,customer1)
	list_hotels_in_city("Paris")
	list_resevrations_for_hotel("hotel1")

main()