#!/usr/bin/python3
'''place class'''
from models.base_model import BaseModel


class Place(BaseModel):
    '''place defined
    Arg:
        city_id (String): The place's city id.
        user_id (string): The place's user id.
        name (String): The name.
        description (String): The description.
        number_rooms (Integer): The number of rooms.
        number_bathrooms (integer): The number of bathrooms.
        max_guest (Integer): The maximum number of guests.
        price_by_night (Integer): The price by night.
        latitude (Float): The place's latitude.
        longitude (Float): The place's longitude
        amenity_ids (list): An id list of all linked amenities
    '''
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = []
