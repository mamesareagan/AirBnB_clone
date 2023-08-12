#!/usr/bin/python3
'''city class'''
from models.base_model import BaseModel


class City(BaseModel):
    '''city of choice
        Arg:
            state_id(str): state id
            name(str): name of the city
    '''
    state_id = ""
    name = ""
