#!/usr/bin/python3
""" Module that contain unit test for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """ Before each test """
        self.my_model = BaseModel()
        self.my_model.name = 'Test Name'
        self.my_model.my_number = 89
        self.my_model.save()

    def test_base_model(self):
        """ Test creation with all arguments """
        my_model_dict = self.my_model.to_dict()

        self.assertEqual(self.my_model.id, my_model_dict['id'])
        self.assertEqual(self.my_model.name, my_model_dict['name'])
        self.assertEqual(self.my_model.my_number, my_model_dict['my_number'])
        self.assertEqual('BaseModel', my_model_dict['__class__'])

    def test_str(self):
        """ Test printable string representation """
        self.assertTrue(str(self.my_model).startswith('[BaseModel]'))

    def test_save(self):
        """ check update on updated_at """
        last_update = self.my_model.updated_at
        self.my_model.name = "Flex Name"
        self.my_model.save()
        self.assertTrue(self.my_model.updated_at > last_update)
        self.assertTrue(self.my_model.updated_at != last_update)

    def test_to_dict(self):
        """ ensure class is serialized to dictionary """
        my_model_dict = self.my_model.to_dict()
        datetime_fmt = '%Y-%m-%dT%H:%M:%S.%f'

        self.assertEqual(self.my_model.id, my_model_dict['id'])
        self.assertEqual(self.my_model.name, my_model_dict['name'])
        self.assertEqual(self.my_model.my_number, my_model_dict['my_number'])
        self.assertEqual('BaseModel', my_model_dict['__class__'])
        self.assertEqual(self.my_model.created_at.strftime(datetime_fmt),
                         my_model_dict['created_at'])
        self.assertEqual(self.my_model.updated_at.strftime(datetime_fmt),
                         my_model_dict['updated_at'])
