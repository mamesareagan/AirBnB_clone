#!/usr/bin/python3
'''serialization and decerialization class'''

import json
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel
class FileStorage:
    '''start of the filestorage class

    Attributes:
        __file_path(private): path to json file
        __objects(private): dictionary to store all objets by <classname.id>
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return the object dictionary'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects obj with key <obj class name>.id

            Args:
                obj: value to assign our key
        '''
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
        
    def save(self):
        '''serializes __ojects to the json file'''
        dictrep = {}
        for key in self.__objects:
            dictrep[key] = self.__objects[key].to_dict()

        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(dictrep, file)

    def reload(self):
        '''deserializes the json file to __objects'''
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass
