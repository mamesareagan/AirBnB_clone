#!/usr/bin/python3
'''the state of user'''
from models.base_model import BaseModel


class State(BaseModel):
    '''state
        Arg:
            name(str): name of the state
    '''
    state = ""
