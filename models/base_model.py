#!/usr/bin/python3
"""Our Base Model Module"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Definition of BaseModel Class"""
    def __init__(self, *args, **kwargs):
        """Instantiation of the class instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                if key != '__class__':
                    setattr(self, key, value)
        
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        models.storage.new(self)
        
    def __str__(self):
        """prints a user friendly representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        my_dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if type(value) != datetime:
                my_dict[key] = value
            else:
                my_dict[key] = value.isoformat()
        return my_dict