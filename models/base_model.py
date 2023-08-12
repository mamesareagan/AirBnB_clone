#!/usr/bin/python3
'''Base class'''
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''defines all common attributes/methods for all other classes'''
    def __init__(self, *args, **kwargs):
        '''initialization code
            Args:
                *args(unused): positional arguments
                **kwargs: key-wordd positional arguments
        '''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if not key == "__class__":
                    setattr(self, key, value)
        self.__new_instance = True
        if kwargs:
            self.__new_instance = False
        if self.__new_instance:
            models.storage.new(self)

    def __str__(self):
        '''prints class name ,self.id and self.__dict__'''
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        '''updates updated_at with current datetime'''
        self.updated_at = datetime.now()
        '''models.storage.new(self)'''
        models.storage.save()

    def to_dict(self):
        '''gives a dictionary of our class'''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = str(type(self).__name__)
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
