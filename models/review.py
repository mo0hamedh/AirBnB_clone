#!/usr/bin/env python3
"""Review Class Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class User that inherits from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
