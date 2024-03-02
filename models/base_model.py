#!/usr/bin/python3
from uuid import uuid4
import datetime


"""Base model """


class BaseModel:
    """class Base"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        d_time = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, d_time)
                    else:
                        setattr(self, key, value)
        else:
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
