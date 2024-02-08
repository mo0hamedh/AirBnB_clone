#!/usr/bin/env python3
"""User Class Module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
