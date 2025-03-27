#!/usr/bin/env python
# coding: utf-8

# In[4]:


# room.py
class Room:
    """Represents a hotel room with its attributes."""
    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability: bool):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__availability = availability
    
    def get_room_number(self):
        return self.__room_number
    
    def is_available(self):
        return self.__availability
    
    def update_availability(self, status: bool):
        self.__availability = status
    
    def __str__(self):
        return f"Room {self.__room_number} ({self.__room_type}) - {'Available' if self.__availability else 'Booked'}"

# guest.py
class Guest:
    """Represents a hotel guest with personal details and loyalty status."""
    def __init__(self, guest_id: int, name: str, contact_info: str, loyalty_points: int = 0):
        self.__guest_id = guest_id
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_points = loyalty_points
    
    def update_profile(self, name: str, contact_info: str):
        self.__name = name
        self.__contact_info = contact_info
    
    def add_loyalty_points(self, points: int):
        self.__loyalty_points += points
    
    def __str__(self):
        return f"Guest {self.__name}, Contact: {self.__contact_info}, Points: {self.__loyalty_points}"

# booking.py
class Booking:
    """Handles the reservation of rooms by guests."""
    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in: str, check_out: str):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        self.__status = "Pending"
    
    def confirm_booking(self):
        self.__status = "Confirmed"
        self.__room.update_availability(False)
    
    def cancel_booking(self):
        self.__status = "Cancelled"
        self.__room.update_availability(True)
    
    def __str__(self):
        return f"Booking {self.__booking_id}: {self.__guest} - Room {self.__room.get_room_number()} ({self.__status})"

# payment.py
class Payment:
    """Handles payment processing and invoice generation."""
    def __init__(self, payment_id: int, booking: Booking, payment_method: str, nightly_rate: float, additional_charges: float, discounts: float):
        self.__payment_id = payment_id
        self.__booking = booking
        self.__payment_method = payment_method
        self.__nightly_rate = nightly_rate
        self.__additional_charges = additional_charges
        self.__discounts = discounts
        self.__total_amount = self.calculate_total()
    
    def calculate_total(self):
        return self.__nightly_rate + self.__additional_charges - self.__discounts
    
    def generate_invoice(self):
        return f"Invoice: Total - ${self.__total_amount}, Payment Method - {self.__payment_method}"
    
    def __str__(self):
        return self.generate_invoice()

# feedback.py
class Feedback:
    """Allows guests to provide reviews."""
    def __init__(self, feedback_id: int, guest: Guest, rating: int, comments: str):
        self.__feedback_id = feedback_id
        self.__guest = guest
        self.__rating = rating
        self.__comments = comments
    
    def __str__(self):
        return f"Feedback from {self.__guest}: {self.__rating}/5 - {self.__comments}"

# test.py
if __name__ == "__main__":
    room1 = Room(101, "Suite", ["Wi-Fi", "TV", "Mini-bar"], 200.0, True)
    guest1 = Guest(1, "Shamma Alnuaimi", "Shamma.aln@gmail.com")
    booking1 = Booking(1, guest1, room1, "2025-04-025", "2025-04-027")
    payment1 = Payment(1, booking1, "Credit Card", 500.0, 50.0, 20.0)
    feedback1 = Feedback(1, guest1, 5, "Very clean and cozy, would visit again!")
    
    print(room1)
    print(guest1)
    print(booking1)
    booking1.confirm_booking()
    print(booking1)
    print(payment1)
    print(feedback1)


# In[ ]:




