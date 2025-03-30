#!/usr/bin/env python
# coding: utf-8

# In[59]:


#room.py
class Room: #this is the first class, it is what will represent a room in the hotel and its attributes. 
    #here we are intializing the attributes of the class
    def __init__(self, room_number, room_type, amenities, price_per_night, availability):
        #here are the private attributes regarding the room details
        self.__room_number = room_number #this attribute is the number of the room
        self.__room_type = room_type #this attributr is the type of room, it could be a single room, double bed room, suite, presidential, etc..
        self.__amenities = amenities #this is the for the amenties, this included wifi, eating from the mini-bar, etc..
        self.__price_per_night = price_per_night #this attribute is the price of the room per night
        self.__availability = availability #this attribute shows the availabilty of the room, where true means that it is available and false means it is booked. 


    def get_room_number(self): #this is what wil return the room number
        return self.__room_number
    
    def is_available(self):# this is what will check if the room is available
        return self.__availability
    
    def update_availability(self, status: bool):#this is what will update the availability of the room
        self.__availability = status
    
    def __str__(self): #this string is what will return the details of the details of the room, such as if it is available, the type of room, and the room number. 
        return f"Room {self.__room_number} ({self.__room_type}) - {'Available' if self.__availability else 'Booked'}"

#guest.py
class Guest: #this is the second class, it is what represents the personal details of the guest as well as their loyal status. 
    #the attributes of the class is initalized. 
    def __init__(self, guest_id, name, contact_info, loyalty_points):
        #here are the private attributes of the guest details
        self.__guest_id = guest_id  #this attribute allows for each guest to have a unique ID
        self.__name = name  #this attribute handles the name of the guest
        self.__contact_info = contact_info  #this attribute handles the contact information of the guest such as the email, phone number, and ID. 
        self.__loyalty_points = loyalty_points #this attribute handles the loyalty points of the guest as a part of the loyalty program. 
    
    
    def update_profile(self, name, contact_info):#the profile information of the guest is updated. 
        self.__name = name #guest name is updated
        self.__contact_info = contact_info #guest contact information is updated. 
    
    def add_loyalty_points(self, points):
        self.__loyalty_points += points #the loyalty points are added to the guest's account. 
    
    def __str__(self): #this is what will return the guest's details such as the name, contact information, and the loyalty points. 
        return f"Guest {self.__name}, Contact: {self.__contact_info}, Points: {self.__loyalty_points}"

#booking.py
class Booking:#this is the third class which is the booking class, and it is responsible for the reservations of the rooms. 
    #the attributes of the class is initalized
    def __init__(self, booking_id, guest: Guest, room: Room, check_in, check_out):
        #here are the private attributes of the booking details
        self.__booking_id = booking_id #this attribute is the booking ID which is uniquew to each guest
        self.__guest = guest #this attribute is the guest who is the one responsible for the booking. 
        self.__room = room #this attribute is the room that was booked. 
        self.__check_in = check_in #this attribute respresent the date that the guest checked in
        self.__check_out = check_out #this attribute represents the date that the guest checked out. 
        self.__status = "Pending" #this attribute represents the the status of the boking.
    
    def confirm_booking(self): #the confirmation of the booking
        self.__status = "Confirmed"
        self.__room.update_availability(False)#the room is unavailable after booking is confirmed
    
    def cancel_booking(self): #the cancellation of booking
        self.__status = "Cancelled"
        self.__room.update_availability(True)# the room booking has been cancelled making it available
    
    def __str__(self):#return booking details such as the id, the guest, room number, and status. 
        return f"Booking {self.__booking_id}: {self.__guest} - Room {self.__room.get_room_number()} ({self.__status})"

#payment.py
class Payment:#this is the fourth class which is responsible for processing a payment and generating a invoice. 
        #the attributes of the class is initalized
    def __init__(self, payment_id, booking: Booking, payment_method, nightly_rate, additional_charges, discounts):
        #here are the private attributes of the payment details
        self.__payment_id = payment_id #this attribute is the payment id
        self.__booking = booking #this attribute is the booking
        self.__payment_method = payment_method #this attribute is the payment method such as debit, credit, cash..
        self.__nightly_rate = nightly_rate #this attribute is the nightly rate
        self.__additional_charges = additional_charges #this attribute is for any additional charges such as mini bar or wifi
        self.__discounts = discounts #this attribute is for the discounts
        self.__total_amount = self.calculate_total() #this attribute is for the total amount 
    
    def calculate_total(self):#this calculates the total which includes the nightly rate, wiht additional charges, and then a discount. 
        return self.__nightly_rate + self.__additional_charges - self.__discounts
    
    def generate_invoice(self):#this generates the invoice
        return f"Invoice: Total - ${self.__total_amount}, Payment Method - {self.__payment_method}"
    
    def __str__(self):
        return self.generate_invoice()#this returns the invoice

#loyalty_program.py
class LoyaltyProgram:#this is the fifth class which handles the loyalty program which allows the guests to earn and redeem points. 
    #the attributes of the class is initalized
    def __init__(self, guest: Guest, points_earned):
        #here are the private attributes of the payment details
        self.guest = guest  #this attribute is the guest that is in the loyalty program
        self.points_earned = points_earned  #this attribute is for the points the guest earned
    
    def redeem_points(self) -> str:#this processed the points that were redemeed
        return "Points redeemed."#this returns a message that says points redeemed

#guest_services.py
class GuestServices:#this is the sixth class that is responsible for service related to the uest such as transportation and programs.     
        #the attributes of the class is initalized
    def __init__(self, service_id, guest: Guest, service_type):
        #here are the private attributes of the guest services details
        self.service_id = service_id  #this attribute is a unique ID for the guest services
        self.guest = guest  #this attribute is for the guest that is requesting the service
        self.service_type = service_type  #this attribute is for the type of service needed
    
    def request_service(self, service_type: str):#here the message is sent to request for service
        return f"{service_type} requested."#returns the message for the service request

#feedback.py
class Feedback:#this is the seventh class which represents the feedback guests give after a stay at the hotel
     #the attributes of the class is initalized
    def __init__(self, feedback_id, guest: Guest, rating, comments):
        #here are the private attributes of the guest services details
        self.__feedback_id = feedback_id #this attribute is for the uniqe id for each feedback
        self.__guest = guest #this attribute is for the id of each guest that gave feedback
        self.__rating = rating #this attribute is for the rating of the stay
        self.__comments = comments #this attribute is for any comments the guests have
    
    def __str__(self):#here the feedback from the gues is returned which includes the guest id, the rating, and comments. 
        return f"Feedback from {self.__guest}: {self.__rating}/5 - {self.__comments}"
    

#testing the different payment methods
def payment_processing():
    #first guest is going to pay by debit card
    guest1 = Guest(1, "Ahmed", "Ahmed@gmail.com", 300)
    room1 = Room(1, "Suite", ["Wi-Fi", "Sauna"], 400.0, True)
    booking1 = Booking(211, guest1, room1, "2025-07-10", "2025-07-15")
    payment1 = Payment(409, booking1, "Debit", 600.0, 60.0, 30.0)
    print(f"Payment successful for {guest1}: {payment1}")

    #secomd guest is going to pay by mobile wallet
    guest2 = Guest(2, "Fatima", "Fatima@gmail.com", 800)
    room2 = Room(2, "Presidential", ["Wi-Fi", "Private Pool"], 1000.0, True)
    booking2 = Booking(212, guest2, room2, "2025-08-01", "2025-08-05")
    payment2 = Payment(500, booking2, "Mobile wallet", 1000.0, 100.0, 30.0)
    print(f"Payment unsuccessful for {guest2}: {payment2}")

payment_processing()


# In[ ]:




