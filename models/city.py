#!/usr/bin/python3
"""
This script defines a BaseModel class for managing and persisting data.
"""


from models.base_model import BaseModel


class City(BaseModel):
    """class city"""

    state_id = ""
    name = ""
