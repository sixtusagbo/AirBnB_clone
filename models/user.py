#!/usr/bin/python3
"""
Module that contains User model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User model """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
