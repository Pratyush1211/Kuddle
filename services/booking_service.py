from . import UserService
from . import Yoga
from . import Dance
from . import Gym
from . import Booking

class BookingService:
    def __init__(self):
        
        # to hold bookings data
        # key will be username
        # and value will be booking model
        # it is assumed that only one registration per user
        self._bookings = {}
        
        self._booking_id_counter = 1
        self._user_service = UserService()
        
        # dummy capacity values as 50 for each class
        self._yoga_classes = Yoga(50, 150)
        self._dance_classes = Dance(50, 160)
        self._gym_classes = Gym(50, 130)
    
    def book_new_class(self, class_type, username):
            if class_type == "yoga":
                return self._register_in_yoga_class(username)
            if class_type == "dance":
                return self._register_in_dance_class(username)
            if class_type == "gym":
                return self._register_in_gym_class(username)
    
    def cancel_class(self, username):
        # allow cancellation only if it is cancelled before 30 minutes of class start time
        
        # dummy current time
        current_time = 140
        if username in self._bookings:
            if self._bookings[username].start_time - current_time <= 30:
                return True
            else:
                return False
        else:
            return False
    
    def _register_in_yoga_class(self, username):
        # TODO: authenticate user first
        # TODO: set timestamp
        timestamp = 123
        
        # create new booking and register in yoga class
        booking = Booking(username, timestamp, "yoga")
        yoga_classes = self._yoga_classes
        capacity = yoga_classes.get_capacity()
        total_registrations = yoga_classes.get_total_registration()
        
        if(capacity >= total_registrations):
            yoga_classes.add_to_waiting(username)
        
        else:
            self._yoga_classes.add_registartion()
            booking.set_booked()
        
        self._bookings[username] = booking
        return booking
    
    def _register_in_dance_class(self, username):
        # TODO: authenticate user first
        # TODO: set timestamp
        timestamp = 123
        
        # create new booking and register in yoga class
        booking = Booking(username, timestamp, "yoga")
        dance_classes = self._dance_classes
        capacity = dance_classes.get_capacity()
        total_registrations = dance_classes.get_total_registration()
        
        if(capacity >= total_registrations):
            dance_classes.add_to_waiting(username)
        
        else:
            self._yoga_classes.add_registartion()
            booking.set_booked()
        
        self._bookings[username] = booking
        return booking

    def _register_in_gym_class(self, username):
        # TODO: authenticate user first
        # TODO: set timestamp
        timestamp = 123
        
        # create new booking and register in yoga class
        booking = Booking(username, timestamp, "yoga")
        gym_classes = self._yoga_classes
        capacity = gym_classes.get_capacity()
        total_registrations = gym_classes.get_total_registration()
        
        if(capacity >= total_registrations):
            gym_classes.add_to_waiting(username)
        
        else:
            self._yoga_classes.add_registartion()
            booking.set_booked()
        
        self._bookings[username] = booking
        return booking
    
    def _increment_booking_count(self):
        self._booking_id_counter += 1
        