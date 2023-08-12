#!/usr/bin/python3
'''amenity'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''amenity of choice
        Arg:
            name(str): name of the amenity
    '''
    name = ""
