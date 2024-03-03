#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """class review"""

    place_id = ""
    user_id = ""
    text = ""
