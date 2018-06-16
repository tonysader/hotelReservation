import smtplib
import conf
import hotel
import customer
import sendEmail


hotelsList = []
customersList = []
reservationList = []


def add_hotel(number,hotel_name, city,total_rooms,empty_rooms):
	h = Hotel()
	h.set(number,hotel_name,city,total_rooms,empty_rooms)
	return h

def add_customer(customer_name,mobile,email):
    # add customer_name to customers list
    c = Customer()
    c.set(customer_name,mobile,email)
    return c

def addToReservationList(hotelName,customer):
	subList = [hotelName,customer]
	reservationList.append(subList)

def add_new_reservation(hotel, customer):
    	if hotel.reserve_room(customer):
			subject = "Hotel reservation"
			msg = "Hello there your reservation has successfuly completed, Hope you enjoy!"
			recieverEmail = customer.email
			Email.sendEmail(subject,msg,recieverEmail)
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



def main():
	hotel1 = add_hotel(1,"hotel1", "Paris",32,6)
	hotel2 = add_hotel(2,"hotel2", "Cairo",42,7)
	customer1 = add_customer("Tony","+5324214","tony.dx.3379@gmail.com"); // Fake mobileNumber
	add_new_reservation(hotel1,customer1)
	list_hotels_in_city("Paris")
	list_resevrations_for_hotel("hotel1")

main()
