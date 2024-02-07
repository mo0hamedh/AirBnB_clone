#!/usr/bin/python3
""" base model defines all common attributes/methods for other classes. """
import uuid
from datetime import datetime
import models

class BaseModel :
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

            Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs :
            for n, s in kwargs.items():
                if n == "created_at" or n == "updated_at":
                    self.__dict__[n] = datetime.strptime(s, tform)
                else:
                    self.__dict__[n] = s
        else:
            models.storage.new()
    def save(self):
        """updates the public instance attribute,  with the current datetime"""
        self.updated_at = datetime.now() 
    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    