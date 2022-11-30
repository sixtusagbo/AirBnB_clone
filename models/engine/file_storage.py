#!/usr/bin/python3
"""
Module that contains file storage class
"""
import os
import json


class FileStorage():
    """
    Serializes instances to a JSON file and
    Deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        dict_ = {}
        for key, obj in FileStorage.__objects.items():
            dict_[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(dict_, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing.
        """
        from models.base_model import BaseModel
        from models.user import User
        dict_models = {"BaseModel": BaseModel, "User": User}

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                for value in json.load(file).values():
                    self.new(dict_models[value['__class__']](**value))
