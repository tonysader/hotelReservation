import smtplib
import conf
import hotel
import customer
import sendEmail
import reversation


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

def add_new_reservation(hotel, customer):

    reversation = Reversation()
    if reversation.reserveOperation(hotel, customer):
		subject = "Hotel reservation"
		msg = "Hello there your reservation has successfuly completed, Hope you enjoy!"
		recieverEmail = customer.email
		Email.sendEmail(subject,msg,recieverEmail)
		print ("confirmation")
    else:
        print ("sorry no rooms available")

def main():
	hotel1 = add_hotel(1,"hotel1", "Paris",32,6)
	hotel2 = add_hotel(2,"hotel2", "Cairo",42,7)
	customer1 = add_customer("Tony","+5324214","tony.dx.3379@gmail.com"); # Fake mobileNumber
	add_new_reservation(hotel1,customer1)
	Hotel.list_hotels_in_city("Paris")
	Hotel.list_resevrations_for_hotel("hotel1")

main()
