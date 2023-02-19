#!/usr/bin/python3
"""
Test for console.py
"""
import unittest
from models import storage
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from io import StringIO
from unittest.mock import patch
import os


class TestHBNBCommand(unittest.TestCase):
    """ Test Suite for HBNBCommand() """

    def setUp(self):
        """ Before each test """
        try:
            os.remove(storage._FileStorage__file_path)
        except OSError:
            pass

    def test_quit(self):
        """ Test quit """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual(f.getvalue(), "")

    def test_eof(self):
        """ Test EOF exits """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(f.getvalue(), "")

    def test_help(self):
        """ Test help documentation """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertTrue("Documented commands" in f.getvalue())

    def test_empty_line(self):
        """ Test empty line does nothing """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_base_model(self):
        """ Create BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIsInstance(f.getvalue(), str)

    def test_all_base_model(self):
        """ all BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            a = f.getvalue()
            HBNBCommand().onecmd("all BaseModel")
            self.assertTrue(a in f.getvalue())

    def test_show_base_model(self):
        """ show BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            a = f.getvalue()
            HBNBCommand().onecmd("show BaseModel {}".format(a))
            self.assertTrue(a in f.getvalue())
            self.assertTrue('id' in f.getvalue())

    def test_update_base_model(self):
        """ update BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            a = f.getvalue()
            HBNBCommand().onecmd("show BaseModel {}".format(a))
            self.assertFalse('first_name' in f.getvalue())
            HBNBCommand().onecmd('update BaseModel {} first_name "Betty"'.format(a))
            HBNBCommand().onecmd("show BaseModel {}".format(a))
            self.assertTrue('first_name' in f.getvalue())

    def test_destroy_base_model(self):
        """ destroy BaseModel """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            a = f.getvalue()
            HBNBCommand().onecmd("show BaseModel {}".format(a))
            self.assertTrue(a in f.getvalue())
            HBNBCommand().onecmd("destroy BaseModel {}".format(a))
            HBNBCommand().onecmd("show BaseModel {}".format(a))
            self.assertTrue(f.getvalue().endswith('** no instance found **\n'))

    def test_base_model_all(self):
        """ BaseModel.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('BaseModel.all()')
            self.assertTrue('BaseModel' in f.getvalue())
            self.assertFalse('User' in f.getvalue())

    def test_user_all(self):
        """ User.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('User.all()')
            self.assertTrue('User' in f.getvalue())
            self.assertFalse('BaseModel' in f.getvalue())

    def test_state_all(self):
        """ State.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            HBNBCommand().onecmd('create State')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('State.all()')
            self.assertTrue('State' in f.getvalue())
            self.assertFalse('BaseModel' in f.getvalue())

    def test_city_all(self):
        """ City.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            HBNBCommand().onecmd('create City')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('City.all()')
            self.assertTrue('City' in f.getvalue())
            self.assertFalse('BaseModel' in f.getvalue())

    def test_amenity_all(self):
        """ Amenity.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            HBNBCommand().onecmd('create Amenity')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('Amenity.all()')
            self.assertTrue('Amenity' in f.getvalue())
            self.assertFalse('BaseModel' in f.getvalue())

    def test_place_all(self):
        """ Place.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            HBNBCommand().onecmd('create Place')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('Place.all()')
            self.assertTrue('Place' in f.getvalue())
            self.assertFalse('BaseModel' in f.getvalue())

    def test_review_all(self):
        """ Review.all() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            HBNBCommand().onecmd('create Review')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('Review.all()')
            self.assertTrue('Review' in f.getvalue())
            self.assertFalse('BaseModel' in f.getvalue())

    def test_base_model_count(self):
        """ BaseModel.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('create BaseModel')
            HBNBCommand().onecmd('BaseModel.count()')
            self.assertTrue('2' in f.getvalue())

    def test_user_count(self):
        """ User.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('create User')
            HBNBCommand().onecmd('User.count()')
            self.assertTrue('2' in f.getvalue())

    def test_state_count(self):
        """ State.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create State')
            HBNBCommand().onecmd('create State')
            HBNBCommand().onecmd('State.count()')
            self.assertTrue('2' in f.getvalue())

    def test_city_count(self):
        """ City.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create City')
            HBNBCommand().onecmd('create City')
            HBNBCommand().onecmd('City.count()')
            self.assertTrue('2' in f.getvalue())

    def test_amenity_count(self):
        """ Amenity.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Amenity')
            HBNBCommand().onecmd('create Amenity')
            HBNBCommand().onecmd('Amenity.count()')
            self.assertTrue('2' in f.getvalue())

    def test_place_count(self):
        """ Place.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Place')
            HBNBCommand().onecmd('create Place')
            HBNBCommand().onecmd('Place.count()')
            self.assertTrue('2' in f.getvalue())

    def test_review_count(self):
        """ Review.count() """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('create Review')
            HBNBCommand().onecmd('create Review')
            HBNBCommand().onecmd('Review.count()')
            self.assertTrue('2' in f.getvalue())

    def test_base_model_show_id(self):
        """ BaseModel.show('id') """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(id))
            self.assertTrue('BaseModel' in f.getvalue())
