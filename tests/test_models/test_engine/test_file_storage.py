#!/usr/bin/python3
"""
Module that contain unit tests for FileStorage
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class TestFileStorage(unittest.TestCase):
    """ Test suite for FileStorage """

    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "Test Name"
        self.my_model.my_number = 98
        self.my_model.save()

    def test_objects_access(self):
        """ cannot access objects """
        with self.assertRaises(AttributeError):
            storage.__objects

    def test_has_attributes(self):
        """ attributes must exist """
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_storage_instance(self):
        """ storage must be instance of FileStorage """
        self.assertIsInstance(storage, FileStorage)

    def test_all(self):
        """ This must return dictionary """
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new(self):
        """ A new object is added to dict objects """
        len_all_objs = len(storage.all())
        new_base = BaseModel()
        storage.new(BaseModel(**new_base.to_dict()))
        len_all_objs_2 = len(storage.all())
        self.assertTrue(len_all_objs_2 > len_all_objs)

    def test_fs_save(self):
        """ must serialize objects to file """
        filename = FileStorage._FileStorage__file_path
        try:
            os.remove(filename)
        except OSError:
            pass
        storage.save()
        self.assertTrue(os.path.exists(filename))

    def test_file_storage_reload(self):
        """ must reload json file to objects """
        filename = FileStorage._FileStorage__file_path
        storage.save()
        self.assertTrue(os.path.exists(filename))
        all_objs = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(all_objs, FileStorage._FileStorage__objects)
        storage.reload()
        for key, value in storage.all().items():
            self.assertEqual(value.to_dict(), all_objs[key].to_dict())

    def test_base_model_save(self):
        """ BaseModel save method calls storage save """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))

    def test_save_self(self):
        """ cannot pass multiple args to save """
        with self.assertRaises(TypeError):
            FileStorage.save(self, 30)

    def test_json_file(self):
        """ JSON file exists """
        self.my_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)
