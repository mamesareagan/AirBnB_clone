#!/usr/bin/python3
'''user class'''
from models.base_model import BaseModel


class User(BaseModel):
    '''user's class
    Arg:
        email(str): user email
        password(str): user password
        firstname(str): user first name
        last_name(str): user last name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
