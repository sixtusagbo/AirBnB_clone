#!/usr/bin/python3
"""
Module that contains the base model from which other classes inherit from
"""
import uuid
from datetime import datetime


class BaseModel():
    """ Common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """ Initialize attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    fmt = '%Y-%m-%dT%H:%M:%S.%f'
                    kwargs[key] = datetime.strptime(value, fmt)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.name = "Temp"
            self.my_number = 98
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Printable string representation """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ Updates `updated_at` with current datetime """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary of __dict__ of the instance modified """
        dict_ = {}

        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                dict_[key] = value.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                dict_[key] = value
        dict_['__class__'] = self.__class__.__name__

        return dict_
